import os
import shutil
# import fnmatch
from natsort import natsorted

rootPath = "/home/mayro/Documents/Nsemble/Cars Project/car_type/copart_dwnlds/ALL_HATCHBACK/unzipped"
# dstn_folder = os.path.join(os.getcwd(),rootPath.split('/')[-1])
start = 4
# pattern = '*.zip'

def pick_collect(folder_path, dstn_folder = None, start = 0, upto = -1):
    if dstn_folder is None:
        dstn_folder = os.path.join(os.getcwd(),'collection')
    os.makedirs(dstn_folder, exist_ok=True)
    # print(folder_path)
    for root, dirs, files in os.walk(folder_path):
        # print(files)
        for wanted in natsorted(files)[start:upto]:                 
            wanted = os.path.join(root,wanted)
            
            print(f'Copying : {wanted}')
            shutil.copy(wanted,dstn_folder)
            
# for folder in os.listdir(rootPath):
#     pick_collect(folder_path = folder)

pick_collect(folder_path = rootPath, start = start)    
# pick_collect(folder_path = rootPath, start = start, dstn_folder = dstn_folder)

try:
    adrs = dstn_folder
except: 
    adrs = os.path.join(os.getcwd(),'collection')
print(f'Process Completed !!! Collection of images can be found in {adrs}.')