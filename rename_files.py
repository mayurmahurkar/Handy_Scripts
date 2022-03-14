#python code to rename multiple files in a folder

#imports
import os
import argparse
from natsort import natsorted
import re

ap = argparse.ArgumentParser()
ap.add_argument("--name",required = True, help = "common name for all the files in the folder")
ap.add_argument("--extension", required = True, 
	help = "extension for all the files in the folder. Example - .jpg" )
ap.add_argument("--folder_path", required = True, help = "path of the folder")
ap.add_argument("--number", required = True, help = "from which numbering of images is to start")
args = vars(ap.parse_args())

def rename_files(path,fix_name,numb,extension):
	#only rename
	i = numb
	path = path + '/'
	#if number in filename is to maintain
	# r = re.compile("([a-zA-Z]+)([0-9]+)")
	
	for filename in natsorted(os.listdir(path)):
		# i = r.match(filename)
		# new_name = args["name"] + str(i.group(2)) + args["extension"]
		new_name = fix_name + str(i) + extension
		old_path = path + filename
		new_path = path + new_name
		# print(old_path, new_path) 
        
		os.rename(old_path,new_path)
		i +=1

if __name__ == '__main__': 
	rename_files(args["folder_path"],args["name"],int(args["number"]),args["extension"])