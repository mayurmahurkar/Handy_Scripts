import os
import glob
import shutil
import zipfile
import fnmatch
from natsort import natsorted

rootPath = r"./copart/"
# pattern = '*.zip'

# def bulk_unzip(rootPath):
#     files_list = []
#     for root, dirs, files in os.walk(rootPath):
#         for filename in fnmatch.filter(files, '*.zip'):
#             print('Unzipping : ',os.path.join(root, filename))
#             zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root,'unzipped',os.path.splitext(filename)[0]))
#             files_list.append(os.path.join(root,'unzipped',os.path.splitext(filename)[0]))
#     return files_list

def list_zips(root_folder):
    return glob.glob(os.path.join(root_folder,'*zip'))

zips_list = list_zips(rootPath)
print(zips_list)
       
# def pick_collect(folder_path):
#     dstn_folder = os.path.join(os.getcwd(),'first4collection')
#     os.makedirs(dstn_folder, exist_ok=True)
#     for root, dirs, files in os.walk(folder_path):
#         for wanted in natsorted(files)[:4]:                 
#             wanted = os.path.join(root,wanted)
            
#             print(f'Copying : {wanted}')
#             shutil.copy(wanted,dstn_folder)
    
# folder_list = bulk_unzip(rootPath)
# # print(folder_list)

# for folder in folder_list:
#     pick_collect(folder)

# dstn_folder = os.path.join(os.getcwd(),'first4collection')
# print(f'Process Completed !!! Collection of images can be found in {dstn_folder}.')