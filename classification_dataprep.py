# Balancing Classification Data

import os
from random import sample
from shutil import copy, copytree

def get_no_imgs(dir):
    """Returns number of files in the directory.

    Args:
        dir (str): directory path

    Returns:
        int: total number of files in the directory.
    """
    return len(os.listdir(dir))

def get_min_no(root_dir):
    """Calculates the minimum number of images needed for balancing the classification dataset 
    on the basis of number of images in each class.

    Args:
        root_dir (str): directory path of image classification dataset, assuming that every sub-directory is a class.

    Returns:
        tuple: class with minimum of images, minimum number of images
    """
    classes = []   #append class(sub-dir) name here
    no_imgs = []   #append no. of images in class(sub-dir) here
    for sub_dir in os.listdir(root_dir):
        classes.append(sub_dir)
        no_imgs.append(get_no_imgs(os.path.join(root_dir,sub_dir)))
    return classes[no_imgs.index(min(no_imgs))], min(no_imgs)

def get_rand_imgs(dir,n):
    """Fetch random number of images or files from a directory, assuming there is no subdirectory in the directory.

    Args:
        dir (str): directory path
        n (int): number of random images or files desired

    Returns:
        list: list of images or files randomly choosen.
    """
    return sample(os.listdir(dir),n)

def balance_classes(root_dir):
    
    """Balances the classification dataset by finding the sub-directory with minimum number of images
    and randomly fetching that amount of images from other sub-directories.

    Args:
        root_dir (str): directory path of image classification dataset, assuming that every sub-directory is a class.
    """
    root_dir = "./exp"
    skip_dir, n = get_min_no(root_dir)
    dstn = os.path.join(os.path.dirname(os.path.abspath(root_dir)),root_dir.split('/')[-1] + '_balanced')

    if os.path.isdir(dstn):
        print(f"Destination Folder already exist. \nDelete {dstn} and retry.")

    else:
        for sub_dir in os.listdir(root_dir):
            print(f"INFO: Working on {sub_dir}")
            if sub_dir == skip_dir:
                copytree(os.path.join(root_dir,sub_dir),os.path.join(dstn,sub_dir))
            else:
                os.makedirs(os.path.join(dstn,sub_dir),exist_ok = True)
                for img_path in get_rand_imgs(os.path.join(root_dir,sub_dir),n):
                    copy(os.path.join(root_dir,sub_dir,img_path),os.path.join(dstn,sub_dir))

        print(f"INFO: Balancing Complete. Each class is balanced at {n} images. \nBalanced Dataset location: {dstn}")

# implementation
data_folder = "./exp"
balance_classes(data_folder)
