# KissingBugsRf


This Repository stores all the python scripts I used to process the data, and the ipynb scripts for training models and making predictions.

This projects has three aims:


* Data: collect infectious disease and climate data.
* Model: develop open-sourced infectious disease modelling softwares.
* Application: Spread the knowledge of infectious disease to the public and generate impacts.


## Design Idea


* Use a grid with $0.05˚\times0.05˚$ cells to vectorize all the variables in raster formats and store the average value for each cell in the attribute table. 
* Use the buffer method to generate psudo absence cells, to match up with the presence cells.
* Feed the attribute table (getting rid of the latitutes and longitudes, of course) into Random Forest for training and making prediction.


## Prerequisites

Install QGIS, Python and Jupyter-lab

## 1.Set up QGIS python console for all the python scripts using QGIS.

* Open QGIS application and go to Plugins-PythonConsole. In the command line, type:


    ```
    import os
    import sys
    print(os.environ)
    print(sys.path)
    ```
    
* Using the results to fill-in 'env = {}' and 'paths = {}'.

* In your system's folder, check if the paths for the following os.environ settings are correct:
```
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/Applications/QGIS.app/Contents/PlugIns'
os.environ['DYLD_INSERT_LIBRARIES'] = '/Applications/QGIS.app/Contents/MacOS/lib/libsqlite3.dylib'
os.environ['PYTHONPATH'] = '/Applications/QGIS.app/Contents/MacOS/bin/python3.9'
```


* Check QgsApplication.setPrefixPath

```
QgsApplication.setPrefixPath("/Applications/QGIS.app/Contents/MacOS",True)
```

* Make sure this uses the python3.9 in the QGIS console. You can change it in your python editor's setting.
(e.g. /Applications/QGIS.app/Contents/MacOS/bin/python3.9 {file})

**Trouble-shooting: Probelms with QGIS can often be solved by re-installing the newest version of QGIS.**


## 2. Data Preparation

* Download Climate and Land Cover data from [AdaptWest](https://adaptwest.databasin.org) and [Guangzhao Chen et al.](https://zenodo.org/record/4584775#.Y-KIMy9w1QL). Note their projection coordinates from inspecting their rasters in QGIS.

**Each climate and land cover variable needs to be stored in a separate raster file with EPSG:4326 Projection.**

* Download **change_projection.py**, which has the codes to change the projection of rasters from AdaptWest and Guangzhao Chen et al. to **EPSG:4326**.
* Setup QGIS python cosole and change the file paths in **change_projection.py** for each raster.

**Vectorize these rasters to vectors with cell size 5 km * 5 km with grids**

* The Grids can be downloaded from DesignSafe (will publish that later). These grids are large and cannot be stored at GitHub Repository.
* Download **zonal_stas.py**
* The **zonal_stas.py** vectorizes each raster with the Grid by calculating an average value for each grid cell and store the avearge value in the Grid Vector's attribute table.


**Get the present cells**
