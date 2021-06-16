import cv2
import os
import argparse


def resize_img(img, scale_percent = 50):
    # scale_percent = percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height) 
    
    # resize image
    resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    resized_dim = resized_img.shape
    
    return resized_img,resized_dim

def _main_(args):
    
    img_dir = args["img_dir"]
    dst_dir = args["dst_dir"]

    if dst_dir == None:
        dst_dir = os.path.join(os.getcwd(),"resized")

    os.makedirs(dst_dir,exist_ok=True)

    images = [img_name for img_name in os.listdir(img_dir) if img_name.lower().endswith((".jpg",".jpeg",".png"))]
    
    for img_name in images:
        img_path = os.path.join(img_dir, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        print(f'Original Dimensions of {img_name}: {img.shape}')
        resized_img,resized_dim = resize_img(img,int(args["scale_percent"]))
        print(f'Resized Dimensions : {resized_img.shape}')
        cv2.imwrite(os.path.join(dst_dir,"resized_"+img_name),resized_img)
    
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    
    ap.add_argument("-f", "--img_dir", required=True, help="Image Directory")
    ap.add_argument("-d", "--dst_dir", required=False, help="Destination Directory")
    ap.add_argument("-p", "--scale_percent", required=False, default = 50, help="Scaling Percentage of image")
    args = vars(ap.parse_args())
    _main_(args)
 
 #USAGE
#  python3 resize_images.py -f "/home/mayro/Documents/My_Computer/Multi Proessing and Threading"
#  python3 resize_images.py -f "/home/mayro/Documents/My_Computer/Multi Proessing and Threading" -d "/home/mayro/Documents/My_Computer/Multi Proessing and Threading/resized"
#  python3 resize_images.py -f "/home/mayro/Documents/My_Computer/Multi Proessing and Threading" -p 10
#  python3 resize_images.py -f "/home/mayro/Documents/My_Computer/Multi Proessing and Threading" -d "/home/mayro/Documents/My_Computer/Multi Proessing and Threading/resized" -p 40
