# KissingBugsRf


This Repository stores all the python scripts I used to process the data, and the ipynb scripts for training models and making predictions.

This projects has three aims:


* Data: collect infectious disease and climate data.
* Model: develop open-sourced infectious disease modelling softwares.
* Application: Spread the knowledge of infectious disease to the public and generate impacts.


## Design

### Overall Structure
* Use a grid with $0.05˚\times0.05˚$ cells to vectorize all the variables in raster formats and store the average value for each cell in the attribute table, with zonal statistics function of pyQGIS.
* Use the buffer method to generate psudo absence cells, to match up with the presence cells.
* Feed the attribute table (getting rid of the latitutes and longitudes, of course) into Random Forest for training and making prediction.

### Buffer Method for selecting pseudo absence cells


**Presence Cells**


Use the select-by-location function of pyQGIS to get the presence cells on the grid from presence points.


**Buffer**


Use the buffer and select-by-location function of pyQGIS to get the buffer cells on the grid from presence points.


**Get psuedo absence cells**



When preparing the training set, randomly select cells from the cells that are not marked as touched by the buffer, and mark these cells as psuedo absence cells. The number of psuedo absence cells is equal to the number of presence cells.


Details about calculation is explained in the .py scripts.




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


**Get the present cells and buffers**

* Download **presence_points_buffer.py**.
* Follow the instruction noted in the scripts to get the corresponding .csv files exported from the grid vector's attribute table. The .csv files have 1 stored in column 'count' and customized buffer name, for cells containing the presence points and buffer.


## 3. Random Forest Model Training


The following scripts are written in .ipynb.


* Make sure all the packages imported are installed.



**You should edit the following sessions in the script to make sure you only calculate and save the items you need.**

For each species with specific buffer:

* Load the count.csv (**presence_path**, presence cells), buffer.csv (**buffer_path**, buffer cells), zonal_stats.csv (**zonal_path**, the variables for each cell).
* Merge these dataframes and we have our raw dataframe **raw_df**, with keys (column titles): variable names (climate and land cover), cell information (id, the longitude and latitute of four vertexs), 'count', buffer name, 'Unnamed: 0' (an useless column which is created automatically when generating new csv).

* The **presence cells** are those raw_df['count']=1 and have no NA values in every column, and are stored as **species_data**. Give them a new column 'presence' and make the values 1.
* The **cells cover the whole North Americas** are the cells that have no NA values in every column, and are stored as **final_testing_group**.
* **The pool of psuedo absence cells** are the cells which has no value in the 'buffer' column from **final_testing_group**, and they are stored as **buffer_background**.

* Create a dictionary for **cross-validation TSS score, x_label, x_list (all the variables, before training-testing split), y_list (all the corresponding results, before training-testing split), x_train_list (all the variables that has been used in the training), gini importance scores, AUC, ROC, shapely values, boruta rank** and save it under dictionary_path.
* *ROC graph** is plotted and stored under ROC_dir.
* **gini importance graph** is plotted and stored under gini_dir.
* **boruta importance graph** is plotted and stored under boruta_dir.
* **shapely value graph** is plotted and stored under shap_dir.
* The **random forests** in all interations are stored under save_tree_dir.
* In each iteration, the prediction of suitable habitat distribution over the whole North America is made by feeding all the valid cells (with non-NA value for all variables) to the trained random forest model. The **average prediction of suitable habitat distribution over the whole north america** is made by averaging the prediction from all iterations, and the corresponding .csv file is stored under pre_dir.

