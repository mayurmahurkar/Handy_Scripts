import os
import shutil
import argparse

def _main_(args):
    
    filename = args["wanted"]
    target_folder = args["trg_fol"]
    dstn_folder = args["dst_fol"]
    
    if dstn_folder == None:
        dstn_folder = os.path.join(os.getcwd(),"matched")

    os.makedirs(dstn_folder,exist_ok=True)

    with open(filename) as file:
        files_list = [line.strip() for line in file]
        
    target_list = os.listdir(target_folder)

    files_set = set(files_list)
    target_set = set(target_list)
    output_set = files_set & target_set

    print(f'Found {len(output_set)} matches.')

    [shutil.copy(os.path.join(target_folder,file),dstn_folder) for file in list(output_set)]


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    
    ap.add_argument("-t", "--trg_fol", required=True, help="Target Directory")
    ap.add_argument("-d", "--dst_fol", required=False, help="Destination Directory")
    ap.add_argument("-w", "--wanted", required=True, help=".txt file of wanted files")
    args = vars(ap.parse_args())
    _main_(args)
    
# USAGE
# python3 extract_matching.py -t "/home/mayro/Documents/Nsemble/Cars Project/API_testing_mayur/Mayur" -w "imgs.txt"
# python3 extract_matching.py -t "/home/mayro/Documents/Nsemble/Cars Project/API_testing_mayur/Mayur" -d "./wanted" -w "imgs.txt"