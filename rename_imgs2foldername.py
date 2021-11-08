import os
import shutil
import argparse

def _main_(args):

    root_dir = args["root_dir"]
    dstn_dir = args["dstn_dir"]

    if dstn_dir == None:
        dstn_dir = os.path.join(os.getcwd(),"prepared_data")
        
    os.makedirs(dstn_dir,exist_ok=True)
    og_paths = []
    new_paths = []

    for dirpath, dirname, files in os.walk(root_dir):
        i = 1
        for filename in files:
            # if filename.endswith(('jpeg','JPEG','jpg','JPG','png','PNG')):
            og_paths.append(os.path.join(dirpath,filename)) 
            new_paths.append(os.path.join(dstn_dir,(os.path.basename(dirpath)+"_image_"+str(i)+
                                                    "."+os.path.basename(filename).split(".")[-1])))
            i+=1
            # else:
            #     continue
            
    print(f'Copying a total of {len(og_paths)} images.')
    
    [shutil.copy(src,dstn) for src,dstn in zip(og_paths,new_paths)]
    
    print(f'Process Completed !!! Collection of images can be found in {dstn_dir}.')
    
if __name__ == '__main__':
    ap = argparse.ArgumentParser()

    ap.add_argument("-r", "--root_dir", required=True, help="root_dir having categories as subdirectory within which images are")
    ap.add_argument("-d", "--dstn_dir", required=False, help="Destination Directory")
    
    args = vars(ap.parse_args())
    _main_(args)
    
## USAGE ###

# python image_rename.py -r "dummy"
# python image_rename.py -r "dummy" -d "output"