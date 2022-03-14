import os
import argparse



ap = argparse.ArgumentParser()
ap.add_argument("--dir1", required = True, help = "directory path from which file is to be remove")
ap.add_argument("--dir2", required = True, help = "directory path to compare file")
ap.add_argument("--extension", required =True, help = "extension for all the files in the folder. Example - .jpg")
args = vars(ap.parse_args())

#list of files without extension from dir1
list_dir1 = [os.path.splitext(filename)[0] for filename in os.listdir(args["dir1"])]
#list of files without extension from dir2
list_dir2 = [os.path.splitext(filename)[0] for filename in os.listdir(args["dir2"])]

#if the file from dir1 is not in dir2 then remove it from dir1
for file in list_dir1:
    if file not in list_dir2:
        remove_file = os.path.join(args["dir1"],file + args["extension"])
        print("This file is being deleted:",remove_file)
        os.remove(remove_file)