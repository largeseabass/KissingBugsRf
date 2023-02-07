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
from qgis.utils import *
from qgis.gui import *
from qgis.PyQt import QtGui

qgs = QgsApplication([], False)
QgsApplication.setPrefixPath("/Applications/QGIS.app/Contents/MacOS",True)
print("Ready")
qgs.initQgis()
import processing

from processing.core.Processing import Processing

from qgis.analysis import QgsNativeAlgorithms

from qgis.analysis import QgsRasterCalculatorEntry,QgsRasterCalculator


QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
print("Processing!")

from os import listdir
from os.path import isfile, join
from PyQt5.QtCore import QFileInfo



"""
AdaptWest Format
* Move the downloaded rasters under the directory: "/Users/huangliting/Desktop/kissing_bugs_stats/future_climate/"
* all the raw rasters in this example are under the path with name like "/Users/huangliting/Desktop/kissing_bugs_stats/future_climate/ensemble_8GCMs_ssp585_2071_2100/ensemble_8GCMs_ssp585_2071_2100_bioclim/"
* the rasters reprojected to EPSG:4326 are stored under output_raster_dir.
"""
climate_name = "ssp585_2071_2100"
mypath = "/Users/huangliting/Desktop/kissing_bugs_stats/future_climate/ensemble_8GCMs_"+climate_name+"/ensemble_8GCMs_"+climate_name+"_bioclim/" ##modified
raster_list = [mypath+f for f in listdir(mypath) if (isfile(join(mypath, f)) and (f[-3:]=='tif'))]
name_list = ['resample_'+f for f in listdir(mypath) if (isfile(join(mypath, f)) and (f[-3:]=='tif'))]

# Create output dir for the rasters after reprojection.
output_raster_dir = '/Users/huangliting/Desktop/kissing_bugs_stats/future_reprojection/'+climate_name+'/'
if not os.path.exists(output_raster_dir):
    os.makedirs(output_raster_dir)


print(raster_list)

for i in range(len(raster_list)):
    input_raster_path = raster_list[i]
    output_raster_path = output_raster_dir + name_list[i]
    print(input_raster_path)
    print(output_raster_path)
    feedback = QgsProcessingFeedback()
    Processing.initialize()
    processing.run("gdal:warpreproject", {'INPUT':input_raster_path,'TARGET_CRS':'EPSG:4326','OUTPUT':output_raster_path,'TARGET_RESOLUTION' : 0.01})


print("AdaptWest: Change projection of layer successful!")


"""
Guangzhao Chen et al. Format
* The rasters before reprojection are stored in mypath. One Raster for each year, comprising of 7 layers.
* The 7 layers are taken out and stored as 7 separate rasters under: /Users/huangliting/Desktop/land-cover/global_SSP1_RCP26_2025/ (directory created by the script)
* Each of the 7 rasters are reprojected to EPSG:4326 and stored under output_raster_dir.
"""

climate_name = "global_SSP1_RCP26_2025"


mypath = "/Users/huangliting/Desktop/land-cover/Global_7-land-types_LULC_projection_dataset_under_SSPs-RCPs/SSP1_RCP26/"+climate_name+".tif" ##modified

# Create the directory to store the 7 land cover layer.
if not os.path.exists("/Users/huangliting/Desktop/land-cover/"+climate_name):
    os.makedirs("/Users/huangliting/Desktop/land-cover/"+climate_name)

# Create output dir for the rasters after reprojection.
output_raster_dir = '/Users/huangliting/Desktop/kissing_bugs_stats/future_reprojection/'+climate_name+'/'
if not os.path.exists('/Users/huangliting/Desktop/kissing_bugs_stats/future_reprojection/'+climate_name):
    os.makedirs('/Users/huangliting/Desktop/kissing_bugs_stats/future_reprojection/'+climate_name)


x_index = ['water','forest','grassland','barren','cropland','urban','permanent_snow_ice']

for i in range(len(x_index)):
    this_layer_num = i+1
    input_raster_path = "/Users/huangliting/Desktop/land-cover/"+climate_name+'/'+x_index[i]+'.tif'

    output_raster_path = output_raster_dir+x_index[i]+'.tif'
    feedback = QgsProcessingFeedback()
    Processing.initialize()
    fileInfo = QFileInfo(mypath)
    this_rpath = fileInfo.filePath()
    baseName = fileInfo.baseName()


    this_raster = QgsRasterLayer(this_rpath,baseName)

    entries = []
    ras = QgsRasterCalculatorEntry()
    ras.ref = climate_name+'@1'
    ras.raster = this_raster
    ras.bandNumber = 1
    entries.append(ras)

    # take the one land cover layer out and store it as a separate raster.
    that_item = climate_name+'@1='+str(this_layer_num)
    print(that_item)
    calc = QgsRasterCalculator(that_item, input_raster_path, 'GTiff', this_raster.extent(), int(this_raster.width()), int(this_raster.height()), entries)
    calc.processCalculation()

    # reproject the raster.
    processing.run("gdal:warpreproject", {'INPUT':input_raster_path,'TARGET_CRS':'EPSG:4326','OUTPUT':output_raster_path,'TARGET_RESOLUTION' : 0.01})



print("Change projection of layer successful!")

"""
Exit QGIS at the end.
"""

qgs.exitQgis()
