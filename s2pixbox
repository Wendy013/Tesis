import numpy as np
import rasterio as rio
import pathlib 
import re
import shutil
from src.utils import list_files

s2pixbox = pathlib.Path("data/raw/Sentinel-2_L1C/")
output = pathlib.Path("data/output/s2_pixbox/")

tci_files = list_files(s2pixbox, pattern=r".*_TCI\.jp2$", full_names=True, recursive=True)

for file in tci_files:
    file = pathlib.Path(file)
    print("Processing: ", file.stem)
    
    # creating output folder
    outputfolder = (output / file.stem)
    outputfolder.mkdir(parents=True, exist_ok=True) 

    # copy band TCI carpet using pathlib
    shutil.copy(file, outputfolder)
            

# convertion table to geopackage
import geopandas as gpd
import pandas as pd

dataset = pd.read_csv("data/raw/PixBox-S2-CMIX/pixbox_sentinel2_cmix_20180425.csv")
dataset2 = dataset[["LATITUDE", "LONGITUDE", "SHADOW_ID", "SURFACE_ID"]]
dataset.keys()
# convert to dataframe to geopandas
gdf = gpd.GeoDataFrame(dataset2, geometry=gpd.points_from_xy(dataset2.LONGITUDE, dataset2.LATITUDE))
gdf.crs = "EPSG:4326"
# write to file geojson
gdf.to_file("data/output/s2_pixbox/pixbox_sentinel2_cmix_20180425.shp")
