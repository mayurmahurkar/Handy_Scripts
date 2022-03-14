import shutil
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("--src_dir", required = True, help = "File path of file to be copy" )
ap.add_argument("--dst_dir",required = True,help = " Folder path of copy files to be save")
ap.add_argument("--num", required = True, help = " No of times files to be copy")
args = vars(ap.parse_args())

for i in range(int(args["num"])):
	shutil.copy2(args['src_dir'],os.path.join(args["dst_dir"], "300_131_{}.xml").format(i+1402))