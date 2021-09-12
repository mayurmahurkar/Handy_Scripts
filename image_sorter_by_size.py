import os
import shutil
import argparse
from skimage import io

# def check_size(image):
#     img = io.imread(image) 
#     img_w = img.shape[0]
#     img_h = img.shape[1]
    
#     return img_w,img_h
    
def flag(image,sep, by = "w"):
    
    img = io.imread(image)
         
    lwr = sep[0]
    upr = sep[-1]
    
    if by == "w" or by == "width":
        choice = img.shape[1]
        subfolder_prefix = "width"
    
    elif by == "h" or by == "height":
        choice = img.shape[0]
        subfolder_prefix = "height"
        
    elif by == "both":
        img_h, img_w = img.shape[0],img.shape[1]
        subfolder_prefix = "both_width_height"
        
    else:
        img_h, img_w = img.shape[0],img.shape[1]
        subfolder_prefix = "any_width_height"
    
    try:
        if choice < lwr:
            subfolder = f"{subfolder_prefix}_less_than_{lwr}px"
            
        elif choice > upr:
            subfolder = f"{subfolder_prefix}_more_than_{upr}px"
        
        else:
            for i in range(1,len(sep)):
                # print(f"Checking if between {sep[i-1]}px and {sep[i]}px.") 
                if choice < sep[i]:
                    subfolder = f"{subfolder_prefix}_between_{sep[i-1]}_{sep[i]}px"
                    
    except:
        if img_h < lwr and :
            subfolder = f"{subfolder_prefix}_less_than_{lwr}px"
                
        
            

    return subfolder
    # elif by == "h" or by == "height":
    #     if img_h < lwr:
    #         subfolder = f"H_less_than_{lwr}px"
            
    #     elif img_h > upr:                 
    #         subfolder = f"H_more_than_{upr}px"
        
    #     else:
    #         for i in range(1,len(sep)):
    #             # print(f"Checking if between {sep[i-1]}px and {sep[i]}px.") 
    #             if img_h < sep[i]:
    #                 subfolder = f"H_between_{sep[i-1]}_{sep[i]}px"
    
    # return subfolder   

            
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
        
        subdir = flag(image = im, sep = sep, by = args["by"])
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
    ap.add_argument("-b", "--by", required=False, choices = ["w","h","width","height"], default = "w", help="sort by image width or height")
    ap.add_argument("-s", "--sep", nargs='+', required= False, 
		help="List of pixel values to be sorted in, MULTIPLE Px VALUES MUST BE PASSED WITHOUT QUOTES & SEPARATED BY SPACE;")

    args = vars(ap.parse_args())
    _main_(args)
    
## USAGE
# python image_sorter_by_size.py -t "/home/mayro/Documents/Nsemble/Useful Scripts/collection" -d "./new_result" -b h
# python image_sorter_by_size.py -t "/home/mayro/Documents/Nsemble/Useful Scripts/collection" -d "./new_result" -s 750 1000