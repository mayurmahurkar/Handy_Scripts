# Importing all necessary libraries
import cv2
import os
# from functools import partial
import concurrent.futures
  
def video2img(video_path):
    # Read the video from specified path
    cam = cv2.VideoCapture(video_path)
    video_name = os.path.basename(video_path).split(".")[0]
    os.makedirs(video_name,exist_ok=True)
    
    # frame
    currentframe = 0
    
    while(True):
        
        # reading from frame
        ret,frame = cam.read()
    
        if ret:
            # if video is still left continue creating images
            name = os.path.join(video_name, str(currentframe) + '.jpg')
            print ('Creating...' + name)
    
            # writing the extracted images
            cv2.imwrite(name, frame)
    
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
    
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()

def get_vidlist(video_folder):
    vid_list = [os.path.join(dirpath, f)
                    for dirpath,dirnames, files in os.walk(video_folder)
                    for f in files if f.endswith('mp4')]
    return vid_list

#--------------------------------------------------------------------------------------------------------
video_folder = 'new_videos'
vid_list = get_vidlist(video_folder)
# print(vid_list)
dstn = video_folder.split("/")[-1]
# for i in vid_list:
#     video2img(i)

# part_func = partial(video2img, dstn_dir = dstn) 

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(video2img, vid_list)