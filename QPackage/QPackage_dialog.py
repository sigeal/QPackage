# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QPackageDialog
                                 A QGIS plugin
 QPackage
                             -------------------
        begin                : 2014-12-16
        git sha              : $Format:%H$
        copyright            : (C) 2014 by CREASIG
        email                : contact@creasig.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import codecs
import shutil
import xml.dom.minidom
import logging

from xml.dom.minidom import parse
from PyQt4 import QtGui, uic, QtCore
from qgis.core import QgsMapLayerRegistry, QgsMapLayer, QgsProject, QgsVectorFileWriter, QgsCoordinateReferenceSystem, QgsVectorLayer, QgsRasterLayer,QgsRasterFileWriter, QgsRasterPipe, QgsCoordinateTransform
from ModeleListeCouches import ModeleListeCouches

try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str

# from PyQt4.QtCore import QFileInfo
# from PyQt4.QtCore import QString
from PyQt4.QtGui import QMessageBox

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'QPackage_dialog_base.ui'))


class QPackageDialog(QtGui.QDialog, FORM_CLASS):

    def __init__(self, iface, parent=None):
        """Constructor."""

        super(QPackageDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.iface = iface

    def chercherRepertoire(self):
        """Choose the destination directory"""

        filename = QtGui.QFileDialog.getExistingDirectory(parent=None, caption=QtGui.QApplication.translate("select destination", "Select directory to Fling from..."), directory=QtCore.QDir.currentPath())
        if filename:
            self._repertoire.setText(filename)

    def chargerCouches(self):
        """Load layers of the current project"""

        # Add the mains projections used by the user
        self._listeprojections.addItem(QtGui.QApplication.translate("select crs", "- Select CRS -"))
        for e in QtCore.QSettings().value('UI/recentProjectionsAuthId'):
            self._listeprojections.addItem(e + ' - ' + str(QgsCoordinateReferenceSystem(e).description()), e)

        # Add layers to the list
        # The vector layers are selected by default
        layers = QgsMapLayerRegistry.instance().mapLayers()
        data = []
        for name, layer in layers.iteritems():
            casecocher = QtGui.QCheckBox(layer.originalName())
            if layer.type() == QgsMapLayer.VectorLayer:
                casecocher.setChecked(True)
            data.append(casecocher)
        self._tableau.setModel(ModeleListeCouches(data))

    def copierCouches(self):
        """Project processing"""

        # Save the current project
        QgsProject.instance().write()
        model = self._tableau.model()
        data = []
        layers = QgsMapLayerRegistry.instance().mapLayers()

        # Initialise the progress bar and the steps 
        self._progression.setValue(0)
        nbrecouches = 0
        for row in model.getDonnees():
            if row.isChecked():
                nbrecouches += 1
        pas = float(100 / nbrecouches)
        progression = float(0)
        messageerreuraffiche = False

        # Manage the layers selected
        for row in model.getDonnees():
            if row.isChecked():
                for name, layer in layers.iteritems():
                    # Problematic special characters replacement (/)
                    name = layer.name().replace('/', '_')

                    if layer.originalName() == row.text():

                        # If the layer is a vector
                        if layer.type() == QgsMapLayer.VectorLayer:
                            layer.__class__ = QgsVectorLayer
                            if self._repertoire.text() != "":
                                # Load the destination projection. if the selected item of the gui list is empty, we use the layer's one
                                projection = layer.crs().authid()
                                if self._listeprojections.currentText() != QtGui.QApplication.translate("select crs", "- Select CRS -"):
                                    projection = self._listeprojections.itemData(self._listeprojections.currentIndex())
                                # Write the vector layer to the destination directory
                                QgsVectorFileWriter.writeAsVectorFormat(layer, self._repertoire.text() + "\\" +  name  + ".shp", "utf-8", QgsCoordinateReferenceSystem(projection), "ESRI Shapefile")
                                # Change the projections of the layer in the project
                                layer.setCrs(QgsCoordinateReferenceSystem(projection))
                                # Change datasource in the project
                                layer.setDataSource(self._repertoire.text() + "\\" +  name  + ".shp", name, "ogr")

                                # Update progression
                                progression += float(pas)
                                self._progression.setValue(progression)

                            # Error message if no directory has been selected
                            else:
                                if False == messageerreuraffiche:
                                    QMessageBox.critical(self, QtGui.QApplication.translate("QPackage", "QPackage"), QtGui.QApplication.translate("choosedestination", "You must choose the destination directory"), QMessageBox.Ok)
                                    messageerreuraffiche = True

                        # If the layer is a raster, the plugin must copy the file
                        elif layer.type() == QgsMapLayer.RasterLayer:
                            layer.__class__ = QgsRasterLayer
                            if self._repertoire.text() != "":
                                shutil.copy2(layer.publicSource(), self._repertoire.text() + "\\" + os.path.basename(layer.publicSource()))
                               
                                # Update progression
                                progression += float(pas)
                                self._progression.setValue(progression)

                            # Error message if no directory has been selected
                            else:
                                if (False == messageerreuraffiche):
                                    QMessageBox.critical(self, QtGui.QApplication.translate("QPackage", "QPackage"), QtGui.QApplication.translate("choosedestination", "You must choose the destination directory"), QMessageBox.Ok)
                                    messageerreuraffiche = True

        # If no error
        if messageerreuraffiche == False:
            # Change current project CRS before saving it
            srcCrs = self.iface.mapCanvas().mapSettings().destinationCrs()
            dstCrs = QgsCoordinateReferenceSystem(projection)
            self.iface.mapCanvas().setDestinationCrs(dstCrs)
            ext = self.iface.mapCanvas().extent()
            trCrs = QgsCoordinateTransform(srcCrs, dstCrs)
            self.iface.mapCanvas().setExtent(trCrs.transformBoundingBox(ext))

            # Set project's name
            fichierprojet = self._repertoire.text() + "\\" + os.path.basename(QgsProject.instance().fileName())
            if not os.path.isfile(QgsProject.instance().fileName()):
                if self._projectname.text() != "":
                    strproject = self._projectname.text()
                    if strproject[-4:] == ".qgs":
                        fichierprojet = self._repertoire.text() + "\\" + strproject
                    else:
                        fichierprojet = self._repertoire.text() + "\\" + strproject + ".qgs"
                else:
                    fichierprojet = self._repertoire.text() + "\\project.qgs"

            # Save the project to the new directory
            QgsProject.instance().write(QtCore.QFileInfo(fichierprojet))
            # We change the path of the layers
            DOMTree = xml.dom.minidom.parse(fichierprojet)
            collection = DOMTree.documentElement
            maplayers = collection.getElementsByTagName("maplayer")
            #logging.basicConfig(filename='myapp.log', level=logging.INFO)
            #logging.info( "coucou")

            for row in model.getDonnees():
                if row.isChecked():
                    for name, layer in layers.iteritems():
                        # Problematic special characters replacement
                        name = layer.name().replace('/', '_')
                        if layer.originalName() == row.text():
                            if self._repertoire.text() != "":
                                if layer.type() == QgsMapLayer.VectorLayer:
                                    #head, tail = os.path.split(layer.source())
                                    for coucheprojet in maplayers:
                                        coucheprojetnom = coucheprojet.getElementsByTagName('layername')[0].childNodes[0].data
                                        if coucheprojetnom == layer.originalName():
                                            projection = layer.crs().authid()
                                            if self._listeprojections.currentText() != QtGui.QApplication.translate("select crs", "- Select CRS -"):
                                                projection = self._listeprojections.itemData(self._listeprojections.currentIndex())

                                            replaceText(coucheprojet.getElementsByTagName('datasource')[0], name + ".shp")
                                            replaceText(coucheprojet.getElementsByTagName('provider')[0], "ogr")
                                            pr = "<spatialrefsys>"
                                            pr = pr+"<proj4>"+str(QgsCoordinateReferenceSystem(projection).toProj4())+"</proj4>"
                                            pr = pr+"<srsid>"+str(QgsCoordinateReferenceSystem(projection).srsid())+"</srsid>"
                                            pr = pr+"<srid>"+str(QgsCoordinateReferenceSystem(projection).postgisSrid())+"</srid>"
                                            pr = pr+"<epsg>"+str(QgsCoordinateReferenceSystem(projection).authid())+"</epsg>"
                                            pr = pr+"<description>"+str(QgsCoordinateReferenceSystem(projection).description())+"</description>"
                                            pr = pr+"<projectionacronym>"+str(QgsCoordinateReferenceSystem(projection).projectionAcronym())+"</projectionacronym>"
                                            pr = pr+"<ellipsoidacronym>"+str(QgsCoordinateReferenceSystem(projection).ellipsoidAcronym())+"</ellipsoidacronym>"
                                            pr = pr+"</spatialrefsys>"
                                            #logging.info( pr)
                                            coucheprojet.getElementsByTagName('srs')[0] = pr

                                elif layer.type() == QgsMapLayer.RasterLayer:
                                    for coucheprojet in maplayers:
                                        coucheprojetnom = coucheprojet.getElementsByTagName('layername')[0].childNodes[0].data
                                        if coucheprojetnom == layer.originalName():
                                            replaceText(coucheprojet.getElementsByTagName('datasource')[0], os.path.basename(layer.publicSource()))
            file_handle = codecs.open(fichierprojet, "w", encoding="utf_8")
            #logging.info(DOMTree.toxml())
            file_handle.write(DOMTree.toxml())
            file_handle.close()
            self._progression.setValue(100)
            QMessageBox.warning(self, QtGui.QApplication.translate("QPackage", "QPackage"), QtGui.QApplication.translate("mustclose", "Layers export completed. You can to re-open project to check changes."))


def replaceText(node, newText):
    """XML node text replacement"""

    if node.firstChild.nodeType != node.TEXT_NODE:
        raise Exception("Node does not contain text.")

    node.firstChild.replaceWholeText(newText)
