import os
import shutil
import argparse
from skimage import io

# def check_size(image):
#     img = io.imread(image) 
#     img_w = img.shape[0]
#     img_h = img.shape[1]
    
#     return img_w,img_h

# def get_info(image):
    
#     img = io.imread(image)
#     img_h, img_w = img.shape[0],img.shape[1]

def get_val(img_h, img_w, by = "w"):
    
    values = {"w":[img_w,"width"],   
                "h":[img_h,"height"],
                "both":[(img_h, img_w),"both_width_height"], 
                "any":[(img_h, img_w),"any_width_height"]}
    
    return values[by]  # value(s) to compare, prefix of destination folder
        
def get_flag(image, sep, by):
    
    img = io.imread(image)
    img_h, img_w = img.shape[0],img.shape[1]
    
    sep = sorted(sep) 
    
    lwr = sep[0]
    upr = sep[-1]
    
    val = get_val(img_h, img_w, by)
    
    flag = None
    
    if type(val[0]) == int:
        if val[0] < lwr:
            flag = f"{val[1]}_less_than_{lwr}px"
            
        elif val[0] > upr:
            flag = f"{val[1]}_more_than_{upr}px"
        
        else:
            for i in range(1,len(sep)):
                # print(f"Checking if between {sep[i-1]}px and {sep[i]}px.") 
                if val[0] <= sep[i]:
                    flag = f"{val[1]}_between_{sep[i-1]}_{sep[i]}px"
                # elif val[0] == sep[i]:
                #     flag = f"{val[1]}_{sep[i]}px"

    
    elif type(val[0]) == tuple:
        if by == "both":
            if val[0][0] < lwr and val[0][1] < lwr:
                flag = f"{val[1]}_less_than_{lwr}px"
            
            elif val[0][0] > upr and val[0][1] > upr:
                flag = f"{val[1]}_more_than_{upr}px"
            
            else:
                for i in range(1,len(sep)):
                    # print(f"Checking if between {sep[i-1]}px and {sep[i]}px.") 
                    if val[0][0] < sep[i] and val[0][1] < sep[i]:
                        flag = f"{val[1]}_between_{sep[i-1]}_{sep[i]}px"
        else:
            # if val[0][0] < lwr or val[0][1] < lwr:
            #     flag = f"{val[1]}_less_than_{lwr}px"
            
            # elif val[0][0] > upr or val[0][1] > upr:
            #     flag = f"{val[1]}_more_than_{upr}px"
            
            # else:
            #     for i in range(1,len(sep)):
            #         # print(f"Checking if between {sep[i-1]}px and {sep[i]}px.") 
            #         if val[0][0] < sep[i] or val[0][1] < sep[i]:
            #             flag = f"{val[1]}_between_{sep[i-1]}_{sep[i]}px"
                        
            if min(val[0][0], val[0][1]) < lwr:
                flag = f"{val[1]}_less_than_{lwr}px"
            
            elif min(val[0][0], val[0][1]) > upr:
                flag = f"{val[1]}_more_than_{upr}px"
        
            else:
                for i in range(1,len(sep)):
                    # print(f"Checking if between {sep[i-1]}px and {sep[i]}px.") 
                    if min(val[0][0], val[0][1]) <= sep[i]:
                        flag = f"{val[1]}_between_{sep[i-1]}_{sep[i]}px"

    return flag           

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
    
    for im in image_list:
        
        print("Checking : ",im)
                      
        if not args["sep"] == None:
            sep = list(map(int, list(args["sep"])))
            
        else:
            sep = [500,650,750,900,1080]   #sepcifying separator pixel values or sizes
        
        # print(sep)
        
        subdir = get_flag(image = im, sep = sep, by = args["by"])
        os.makedirs(os.path.join(dstn_folder,subdir), exist_ok=True)
        final_dstn_folder = os.path.join(dstn_folder,subdir)
        
        print(f"...Copying to {final_dstn_folder}...")
        shutil.copy(im,final_dstn_folder)
        
    # [shutil.copy(os.path.join(target_folder,file),dstn_folder) for file in list(image_list) if check_size(image)]
    
    print(f'\nProcess Completed !!! Sorted images can be found in {dstn_folder}.')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    
    ap.add_argument("-t", "--trg_fol", required=True, help="Target Directory")
    ap.add_argument("-d", "--dst_fol", required=False, help="Destination Directory")    
    ap.add_argument("-b", "--by", required=False, choices = ["w","h","both","any"], default = "w", help="sort by image width or height")
    ap.add_argument("-s", "--sep", nargs='+', required= False, 
		help="List of pixel values to be sorted in, MULTIPLE Px VALUES MUST BE PASSED WITHOUT QUOTES & SEPARATED BY SPACE;")

    args = vars(ap.parse_args())
    _main_(args)
    
## USAGE
# python image_sorter_by_sizeV3.py -t "/home/mayro/Documents/Nsemble/Useful Scripts/collection"
# python image_sorter_by_sizeV3.py -t "/home/mayro/Documents/Nsemble/Useful Scripts/collection" -d "./new_result" -b h
# python image_sorter_by_sizeV3.py -t "/home/mayro/Documents/Nsemble/Useful Scripts/collection" -d "./new_result" -s 600 750 1000