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


QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
print("Processing")

from os import listdir
from os.path import isfile, join

"""
for rasters from AdaptWest
"""
climate_name = "ssp585_2071_2100"
mypath = '/Users/huangliting/Desktop/kissing_bugs_stats/future_reprojection/'+climate_name+'/'
#mypath = "/Users/huangliting/Desktop/kissing_bugs_stats/reprojection/" ##modified
#N_length = len(mypath)+9
raster_list = [mypath+f for f in listdir(mypath) if (isfile(join(mypath, f)) and (f[-3:]=='tif'))]
name_list = []


for this_raster in raster_list:
    name_list = np.append(name_list, this_raster[len(mypath):-4])


print(name_list)
print(len(name_list))

vector_path = '/Users/huangliting/Desktop/kissing_bugs_stats/reproject_grid/grid_005d.shp'


temporary_path = '/Users/huangliting/Desktop/kissing_bugs_stats/future_reprojection/'+climate_name+'/trythis.csv'
saving_csv_path = '/Users/huangliting/Desktop/kissing_bugs_stats/future_reprojection/'+climate_name+'/5km.csv'

for i in range(len(raster_list)):
    # Run zonal statistics and store the output csv file in the temporary path
    print(i)
    name_this = name_list[i]
    print(name_this)
    file_output = temporary_path
    file_input = raster_list[i]
    feedback = QgsProcessingFeedback()
    Processing.initialize()
    processing.run("native:zonalstatisticsfb", {'INPUT':vector_path,'INPUT_RASTER':file_input,'RASTER_BAND':1,'COLUMN_PREFIX':'_','STATISTICS':[2],'OUTPUT':file_output})

    print(os.path.exists(saving_csv_path))


    if os.path.exists(saving_csv_path):
        print('exist')
        data_add = pd.read_csv(file_output)
        data_saving = pd.read_csv(saving_csv_path)
        key_column = 'id'
        # #Get the set of unwanted keys
        keyset_add = data_add.keys().drop([key_column,'_mean'])
        #Drop these unwanted columns
        data_add.drop(columns=keyset_add, inplace=True)
        #Rename the column we are interested in
        data_add.rename(columns={'_mean':name_this},inplace=True)
        #Merge two datasets
        df = pd.merge(data_add, data_saving, on='id')
        #save
        df.drop(['Unnamed: 0'], axis=1,inplace=True)
        df.to_csv(saving_csv_path)
        os.remove(file_output)
    else:
        print('create_new')
        data_add = pd.read_csv(file_output)
        data_add.rename(columns={'_mean':name_this},inplace=True)
        #data_add.drop(['Unnamed: 0'], axis=1,inplace=True)
        data_add.to_csv(saving_csv_path)
        os.remove(file_output)

"""
for rasters from Guangzhao Chen et al.
"""
climate_name = "global_SSP5_RCP85_2085"
mypath = '/Users/huangliting/Desktop/kissing_bugs_stats/future_reprojection/'+climate_name+'/'
raster_list = [mypath+f for f in listdir(mypath) if (isfile(join(mypath, f)) and (f[-3:]=='tif'))]
name_list = []


for this_raster in raster_list:
    name_list = np.append(name_list, this_raster[len(mypath):-4])


print(name_list)

vector_path = '/Users/huangliting/Desktop/kissing_bugs_stats/reproject_grid/grid_005d.shp'


"""modify"""


temporary_path = '/Users/huangliting/Desktop/kissing_bugs_stats/future_reprojection/'+climate_name+'/trythis.csv'
saving_csv_path = '/Users/huangliting/Desktop/kissing_bugs_stats/future_reprojection/'+climate_name+'/5km.csv'

for i in range(len(raster_list)):
    # Run zonal statistics and store the output csv file in the temporary path
    print(i)
    name_this = name_list[i]
    print(name_this)
    file_output = temporary_path
    file_input = raster_list[i]
    feedback = QgsProcessingFeedback()
    Processing.initialize()
    processing.run("native:zonalstatisticsfb", {'INPUT':vector_path,'INPUT_RASTER':file_input,'RASTER_BAND':1,'COLUMN_PREFIX':'_','STATISTICS':[2],'OUTPUT':file_output})

    print(os.path.exists(saving_csv_path))


    if os.path.exists(saving_csv_path):
        print('exist')
        data_add = pd.read_csv(file_output)
        data_saving = pd.read_csv(saving_csv_path)
        key_column = 'id'
        # #Get the set of unwanted keys
        keyset_add = data_add.keys().drop([key_column,'_mean'])
        #Drop these unwanted columns
        data_add.drop(columns=keyset_add, inplace=True)
        #Rename the column we are interested in
        data_add.rename(columns={'_mean':name_this},inplace=True)
        #Merge two datasets
        df = pd.merge(data_add, data_saving, on='id')
        #save
        df.drop(['Unnamed: 0'], axis=1,inplace=True)
        df.to_csv(saving_csv_path)
        os.remove(file_output)
    else:
        print('create_new')
        data_add = pd.read_csv(file_output)
        data_add.rename(columns={'_mean':name_this},inplace=True)
        #data_add.drop(['Unnamed: 0'], axis=1,inplace=True)
        data_add.to_csv(saving_csv_path)
        os.remove(file_output)
print("Add zonal stats data success!")



"""
Exit QGIS at the end.
"""

qgs.exitQgis()
