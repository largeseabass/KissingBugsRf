import pandas as pd
import csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.utils import resample, shuffle
from sklearn import metrics
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import accuracy_score
from sklearn import datasets
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import label_binarize
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
import os

import time
from scipy.stats import spearmanr
from sklearn.model_selection import GridSearchCV

import os
import sys
import subprocess
import os.path



env = {'USER': 'huangliting', 'MallocNanoZone': '0', '__CFBundleIdentifier': 'org.qgis.qgis3', 'COMMAND_MODE': 'unix2003', 'LOGNAME': 'huangliting', 'PATH': '/usr/bin:/bin:/usr/sbin:/sbin', 'PYQGIS_STARTUP': 'pyqgis-startup.py', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.eUuD4OkY4J/Listeners', 'SHELL': '/bin/zsh', 'MallocSpaceEfficient': '0', 'HOME': '/Users/huangliting', 'QT_AUTO_SCREEN_SCALE_FACTOR': '1', '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x2', 'TMPDIR': '/var/folders/lh/t7fjqv3j791d2wjbckpwg5480000gn/T/', 'XPC_SERVICE_NAME': 'application.org.qgis.qgis3.38543067.38544250', 'XPC_FLAGS': '0x0', 'GDAL_DRIVER_PATH': '/Applications/QGIS.app/Contents/MacOS/lib/gdalplugins', 'GDAL_DATA': '/Applications/QGIS.app/Contents/Resources/gdal', 'PYTHONHOME': '/Applications/QGIS.app/Contents/MacOS', 'GDAL_PAM_PROXY_DIR': '/Users/huangliting/Library/Application Support/QGIS/QGIS3/profiles/default/gdal_pam/', 'GISBASE': '/Applications/QGIS.app/Contents/MacOS/grass', 'GRASS_PAGER': 'cat', 'LC_CTYPE': 'UTF-8', 'SSL_CERT_DIR': '/Applications/QGIS.app/Contents/Resources/certs', 'SSL_CERT_FILE': '/Applications/QGIS.app/Contents/Resources/certs/certs.pem'}

paths = ['/Applications/QGIS.app/Contents/MacOS/../Resources/python', '/Users/huangliting/Library/Application Support/QGIS/QGIS3/profiles/default/python', '/Users/huangliting/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins', '/Applications/QGIS.app/Contents/MacOS/../Resources/python/plugins', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/opencv_contrib_python-4.3.0.36-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/patsy-0.5.1-py3.9.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/statsmodels-0.11.1-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/matplotlib-3.3.0-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/numba-0.50.1-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/rasterio-1.1.5-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/Pillow-7.2.0-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/pandas-1.3.3-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/geopandas-0.8.1-py3.9.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python39.zip', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/cftime-1.2.1-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/GDAL-3.3.2-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/netCDF4-1.5.4-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/numpy-1.20.1-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/Fiona-1.8.13.post1-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/Rtree-0.9.7-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/pyproj-3.2.0-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/site-packages/scipy-1.5.1-py3.9-macosx-10.13.0-x86_64.egg', '/Applications/QGIS.app/Contents/MacOS/lib/python3.9/lib-dynload', '/Users/huangliting/Library/Application Support/QGIS/QGIS3/profiles/default/python']

for k,v in env.items():
    os.environ[k] = v

for p in paths:
    sys.path.insert(0,p) #insert the p at the front of list of the path


os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/Applications/QGIS.app/Contents/PlugIns'

os.environ['DYLD_INSERT_LIBRARIES'] = '/Applications/QGIS.app/Contents/MacOS/lib/libsqlite3.dylib'

os.environ['PYTHONPATH'] = '/Applications/QGIS.app/Contents/MacOS/bin/python3.9'


from qgis.core import *
import qgis.utils
from qgis.utils import *
from qgis.gui import *
from qgis.PyQt import QtGui
from PyQt5.QtWidgets import QApplication


#qgs = QApplication ([])
qgs = QgsApplication([], False)
QgsApplication.setPrefixPath("/Applications/QGIS.app/Contents/MacOS",True)
print("Ready")
#QgsApplication.initQgis()
qgs.initQgis()
import processing
from processing.core.Processing import Processing
from qgis.analysis import QgsNativeAlgorithms
from qgis.core import QgsVectorLayer
from PyQt5.QtCore import QVariant

QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

print("Processing!")

from os import listdir
from os.path import isfile, join

feedback = QgsProcessingFeedback()
Processing.initialize()

"""
Presence Cells
(1) Open species presence points .csv as a vector layer, open the grid as a vector layer.
* expect each .csv file has columns 'longitudes' and 'latitudes', and use EPSG:4326 to record the coordinates.
* The grid is stored at vector_grid_path.
* Each species presence points .csv file is stored at csv_file_path.
* The sp_rare_name_list is to help you iterate through all the species.
(2) Create a new attribute in the Grid Vector, named 'count'.
(3) Use the select-by-location pyQGIS function to select the cells containing more than one presence points, and give them a value 1 in the 'count' column.
(4) Export the grid as a .csv file to the path save_count_csv_path.
(5) Remove selection and the attribute 'count' for the Grid Vector.
"""

# This list depends on how you save your species presence points
sp_rare_name_list = ['San','San_10','Rub','Rub_10','Rec','Rec_10','Pro','Pro_10','Neo','Neo_10','Mex','Mex_10','Maz','Maz_10','Lon','Lon_10','Lec','Lec_10','Ind','Ind_10','Ger','Ger_10','Dim','Dim_10']

for this_species_name in sp_rare_name_list:
    sp_rare_name = this_species_name
    sp_name = '_g5'
    vector_grid_path = '/Users/huangliting/Desktop/kissing_bugs_stats/reproject_grid/grid_005d_process.shp'
    save_name = sp_rare_name+sp_name
    csv_file_path = '/Users/huangliting/Desktop/kissing_bugs_stats/Rarefied_Data/'+sp_rare_name+'_rarefied_points.csv'

    uri = 'file:///%s?crs=%s&delimiter=%s&xField=%s&yField=%s&useHeader=yes' % (csv_file_path, 'EPSG:4326', ',', 'longitudes', 'latitudes')

    #Make a vector layer
    sp_layer=QgsVectorLayer(uri,"san10","delimitedtext")
    #Check if layer is valid
    if not sp_layer.isValid():
        print("csv Layer not loaded")
    else:
        QgsProject.instance().addMapLayer(sp_layer)

    grid_layer = QgsVectorLayer(vector_grid_path, 'grid', 'ogr') ##change here

    if not grid_layer.isValid():
        print("grid Layer failed to load!")
    else:
        QgsProject.instance().addMapLayer(grid_layer)

    """
    select by location, save the presence cells
    0 — intersect
    1 — contain
    2 — disjoint
    3 — equal
    4 — touch
    5 — overlap
    6 — are within
    7 — cross
    """
    layer_provider=grid_layer.dataProvider()
    layer_provider.deleteAttributes([5])

    grid_layer.updateFields()
    print(grid_layer.fields().names())

    layer_provider.addAttributes([QgsField('count',QVariant.Int)])
    grid_layer.updateFields()
    print(grid_layer.fields().names())

    processing.run("qgis:selectbylocation", {'INPUT':grid_layer,'PREDICATE':[0,1,5,6],'INTERSECT':sp_layer,'METHOD':0})

    count = 0

    selected = grid_layer.selectedFeatures()

    grid_layer.startEditing()

    for feat in selected:
        count = count+1
        feat['count'] = 1
        grid_layer.updateFeature(feat)
        # grid_layer.changeAttributeValue(feat.id(), 5, (1))
        # print(type(feat.attributes()[5]))
        #print('id'+str(feat.attributes()[0])+'--l'+str(feat.attributes()[1])+'--t'+str(feat.attributes()[2])+'--r'+str(feat.attributes()[3])+'--b'+str(feat.attributes()[4])+'--san'+str(feat.attributes()[5]))

    grid_layer.commitChanges()
    #print("--------------------------------------------------------------------------------------------------")
    print('number of presence cells: '+str(count))
    #print("--------------------------------------------------------------------------------------------------")


    # for f in grid_layer.selectedFeatures():
    #     print('2id'+str(feat.attributes()[0])+'--l'+str(feat.attributes()[1])+'--t'+str(feat.attributes()[2])+'--r'+str(feat.attributes()[3])+'--b'+str(feat.attributes()[4])+'--san'+str(feat.attributes()[5]))
    save_options = QgsVectorFileWriter.SaveVectorOptions()
    save_options.driverName = "CSV"
    save_options.fileEncoding = "UTF-8"
    transform_context = QgsProject.instance().transformContext()
    save_count_csv_path = '/Users/huangliting/Desktop/kissing_bugs_stats/presence_point/'+save_name+'.csv'

    QgsVectorFileWriter.writeAsVectorFormatV3(grid_layer,save_count_csv_path,transform_context,save_options)
    print('save to: '+ save_count_csv_path)
    print("--------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------")
    layer_provider.deleteAttributes([5])
    grid_layer.updateFields()
    grid_layer.commitChanges()
    grid_layer.removeSelection()
    grid_layer.updateFields()
    grid_layer.commitChanges()
    print(grid_layer.fields().names())

"""
Create Buffer 1 55km, 0.5 degree (b05) for 0.05˚ (5km) grid.

(1) Open species presence points .csv as a vector layer, open the grid as a vector layer.
* expect each .csv file has columns 'longitudes' and 'latitudes', and use EPSG:4326 to record the coordinates.
* The grid is stored at vector_grid_path.
* Each species presence points .csv file is stored at csv_file_path.
* The sp_rare_name_list is to help you iterate through all the species.
(2) Create a new attribute in the Grid Vector, named save_buffer.
(3) Use the buffer pyQGIS function to create a buffer around each precense point with diameter buffer_size˚, and store this vector to output_buffer_path.
(4) Use the select-by-location pyQGIS function to select the cells containing with the buffers, and give them a value 1 in the 'save_buffer' column.
(5) Export the grid as a .csv file to the path save_count_csv_path.
(6) Remove selection and the attribute 'save_buffer' for the Grid Vector. Delete the buffer vector from output_buffer_path.
"""

sp_rare_name_list = ['San','San_10','Rub','Rub_10','Rec','Rec_10','Pro','Pro_10','Neo','Neo_10','Mex','Mex_10','Maz','Maz_10','Lon','Lon_10','Lec','Lec_10','Ind','Ind_10','Ger','Ger_10','Dim','Dim_10']

for name_this_sp in sp_rare_name_list:
    sp_rare_name = name_this_sp
    sp_name = '_g05_'
    save_buffer = 'b_05'
    buffer_size = 0.5
    vector_grid_path = '/Users/huangliting/Desktop/kissing_bugs_stats/reproject_grid/grid_005d_process3.shp'
    save_name = sp_rare_name+sp_name+save_buffer
    csv_file_path = '/Users/huangliting/Desktop/kissing_bugs_stats/Rarefied_Data/'+sp_rare_name+'_rarefied_points.csv'

    uri = 'file:///%s?crs=%s&delimiter=%s&xField=%s&yField=%s&useHeader=yes' % (csv_file_path, 'EPSG:4326', ',', 'longitudes', 'latitudes')


    #Make a vector layer
    sp_layer=QgsVectorLayer(uri,"san10","delimitedtext")
    #Check if layer is valid
    if not sp_layer.isValid():
        print("csv Layer not loaded")
    else:
        QgsProject.instance().addMapLayer(sp_layer)


    grid_layer = QgsVectorLayer(vector_grid_path, 'grid', 'ogr') ##change here



    if not grid_layer.isValid():
        print("grid Layer failed to load!")
    else:
        QgsProject.instance().addMapLayer(grid_layer)

    # Make sure we don't have anything selected for this vector.
    grid_layer.removeSelection()
    layer_provider=grid_layer.dataProvider()

    """
    !!! delete additional attributes if we have more than 6 columns.
    """
    #layer_provider.deleteAttributes([5])
    grid_layer.updateFields()

    layer_provider.addAttributes([QgsField(save_buffer,QVariant.Int)])
    grid_layer.updateFields()
    print('checking:')
    print(grid_layer.fields().names())
    print('create buffer ...')

    output_buffer_path = '/Users/huangliting/Desktop/kissing_bugs_stats/buffers/temporary.shp'
    processing.run("native:buffer", { 'DISSOLVE' : True, 'DISTANCE' : buffer_size , 'END_CAP_STYLE' : 0, 'INPUT' : sp_layer, 'JOIN_STYLE' : 0, 'MITER_LIMIT' : 2, 'OUTPUT' : output_buffer_path, 'SEGMENTS' : 5 })

    output_buffer = QgsVectorLayer(output_buffer_path, "buffer", "ogr")

    print('create selection ...')
    processing.run("qgis:selectbylocation", {'INPUT':grid_layer,'PREDICATE':[0,1,5,6],'INTERSECT':output_buffer,'METHOD':0})

    selected = grid_layer.selectedFeatures()
    print('update values ...')

    grid_layer.startEditing()

    for feat in selected:
        feat[save_buffer] = 1
        grid_layer.updateFeature(feat)

    grid_layer.commitChanges()

    print('save buffer ...')

    save_options = QgsVectorFileWriter.SaveVectorOptions()
    save_options.driverName = "CSV"
    save_options.fileEncoding = "UTF-8"
    transform_context = QgsProject.instance().transformContext()
    save_count_csv_path = '/Users/huangliting/Desktop/kissing_bugs_stats/buffers/'+save_name+'.csv'

    QgsVectorFileWriter.writeAsVectorFormatV3(grid_layer,save_count_csv_path,transform_context,save_options)
    print('save to: '+ save_count_csv_path)
    layer_provider.deleteAttributes([5])
    grid_layer.updateFields()
    grid_layer.commitChanges()
    grid_layer.removeSelection()
    os.remove(output_buffer_path)



"""
Exit QGIS at the end.
"""
#QgsApplication.exitQgis()
qgs.exitQgis()
