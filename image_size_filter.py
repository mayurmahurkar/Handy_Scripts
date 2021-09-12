import os
from skimage import io
import shutil
import argparse

def check_size(image,size = 1000,any = True):
    img = io.imread(image) 
    img_w = img.shape[0]
    img_h = img.shape[1]
    
    if any:
        if img_w >= size or img_h >= size:
            return True
    else:
        if img_w >= size and img_h >= size:
            return True
   
    
def _main_(args):
    
    target_folder = args["trg_fol"]
    dstn_folder = args["dst_fol"]
    
    if dstn_folder == None:
        dstn_folder = os.path.join(os.getcwd(),"collection")

    os.makedirs(dstn_folder,exist_ok=True)
  
    image_list = [os.path.join(dirpath, f)
                       for dirpath,dirnames, files in os.walk(target_folder)
                       for f in files if f.endswith(('jpeg','JPEG','jpg','JPG','png','PNG'))]
    
    print(f'Reading a total of {len(image_list)} images.')
    cnt = 0
    for im in image_list:
        
        print("Checking : ",im)
        
        if args["size"] == None:
            size = 1000
        else:
            size = int(args["size"])
        
        if args["any"] == None:
            any = True
        else:
            any = False
        
        if check_size(image = im,size = size,any = any):
            cnt += 1
            print("...Copying...")
            shutil.copy(im,dstn_folder)
        else:
            print("...Skipping...")

    # [shutil.copy(os.path.join(target_folder,file),dstn_folder) for file in list(image_list) if check_size(image)]
    
    print(f'Process Completed !!! Collection of {cnt} image(s) can be found in {dstn_folder}.')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    
    ap.add_argument("-t", "--trg_fol", required=True, help="Target Directory")
    ap.add_argument("-d", "--dst_fol", required=False, help="Destination Directory")    
    ap.add_argument("-s", "--size", required=False, help="filter images of size above or equal to")
    ap.add_argument("-a", "--any", required=False, choices = ["True","False"],help="any of width or height is above specified size")
    args = vars(ap.parse_args())
    _main_(args)
    
## USAGE
# python image_size_filter.py -t "/home/mayro/Documents/Nsemble/Useful Scripts/collection" -d "./new_result" -a False
# python image_size_filter.py -t "/home/mayro/Documents/Nsemble/Useful Scripts/collection" -d "./new_result" -s 1500