import numpy as np
import rasterio as rio
import pathlib 
import re
import shutil
from src.utils import list_files

l8whucloud = pathlib.Path("data/raw/WhuCloud-L8/paper/cloud detection/Train/masked")
output = pathlib.Path("data/output/l8_whucloud")

masked_files = list_files(l8whucloud, pattern=r".*\.tif$", full_names=True, recursive=True)

for path in l8whucloud.glob("*"):
    print("Processing: ", path.stem)
    # creating output folder
    outputfolder = (output / path.stem)
    outputfolder.mkdir(parents=True, exist_ok=True) 
    
    print (output)
    # Obtener el archivo que coincide con el nombre de la carpeta mask
    mask_coincidente = next((archivo for archivo in masked_files if pathlib.Path(archivo).name == path.stem + ".tif"), None) 

    # Rutear hacia la carpeta overall-mask
    overall_folder = pathlib.Path("data/raw/WhuCloud-L8/paper/cloud detection/Train/overall-mask")
    overall_files = list_files(overall_folder, pattern=r".*\.tif$", full_names=True, recursive=True)

    # Obtener el archivo que coincide con el nombre de la carpeta overall
    overall_find = next((archivo for archivo in overall_files if pathlib.Path(archivo).name == path.stem + ".tif"), None)

    overall_coincidente = "MASK_" + pathlib.Path(overall_find).name
    
    # Mover el archivo a la carpeta de salida
    shutil.copy(str(overall_find), str(outputfolder / pathlib.Path(overall_coincidente).name))
    shutil.copy(str(mask_coincidente), str(outputfolder / pathlib.Path(mask_coincidente).name))
