# Install packages
import numpy as np
import rasterio as rio
import pathlib 
import re
import shutil
l8pixbox = pathlib.Path("data/raw/PixBox-L8-CMIX/")
output = pathlib.Path("data/output/")

for path in l8pixbox.glob("*"):
    print("Processing: ", path.stem)
    # creating output folder
    outputfolder = (output / path.stem)
    outputfolder.mkdir(parents=True, exist_ok=True) 

    # select only B2, B3 and B4 bands 
    regex_compile = re.compile(r".*_B[2-4]\.TIF$")
    rgbands = [p for p in path.glob("*") if regex_compile.match(str(p))] 
    rgbands.reverse() # reverse order to B4, B3, B2

    # reading rgb bands 
    container_rgb = list()
    for band in rgbands:
        with rio.open(band) as src:
            metadata = src.profile
            container_rgb.append(src.read(1))
    rgb_array = np.dstack(container_rgb)
    rgb_array2 = np.moveaxis(rgb_array, 2, 0)
    
    # writing the results
    metadata.update(count=3, dtype=rgb_array.dtype)
    with rio.open(outputfolder / "RGB.tif", "w", **metadata) as dst:
        dst.write(rgb_array2)

    # copy band BQA using pathlib
    regex_compile = re.compile(r".*_BQA\.TIF$")
    bqa = [p for p in path.glob("*") if regex_compile.match(str(p))]
    shutil.copy(bqa[0], outputfolder / "BQA.TIF")

# convertion table to geopackage
import geopandas as gpd
import pandas as pd

dataset = pd.read_csv("data/raw/L8-PixBox/pixbox_landsat8_cmix_20150527.csv")
dataset2 = dataset[["LATITUDE", "LONGITUDE", "CLOUD_SHADOW_ID", "PIXEL_SURFACE_TYPE_ID"]]

# convert to dataframe to geopandas
gdf = gpd.GeoDataFrame(dataset2, geometry=gpd.points_from_xy(dataset2.LONGITUDE, dataset2.LATITUDE))
gdf.crs = "EPSG:4326"

# write to file geojson
gdf.to_file("data/output/pixbox_landsat8_cmix_20150527.shp")
