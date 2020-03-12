import cv2, os
import numpy as np

ROOT_DIR = os.getcwd()
TEST_DIR = os.path.join(ROOT_DIR, 'tests')
image_list = [i for i in os.listdir(TEST_DIR) if i.endswith('.png')]
image_list.sort(key=lambda a:int(a.split('_')[2]))


RAW_DIR = '/home/ocakirog/Desktop/ozanc-projects/data-preprocessing/istanbul'
raw_image_list = [i for i in os.listdir(RAW_DIR) if i.endswith('leftImg8bit.jpg')]
raw_image_list.sort(key=lambda a:int(a.split('_')[2]))


dummy_image_path = os.path.join(TEST_DIR, image_list[0])
dummy_image = cv2.imread(dummy_image_path)

width, height, channels = dummy_image.shape

output_dir = 'monodepth_ozan.avi'
fourcc =  cv2.VideoWriter_fourcc('M','J','P','G')
fps = 30
out = cv2.VideoWriter(output_dir, fourcc, fps, (width//4, height//2))

for ind, image_name in enumerate(image_list):
    if ind >15:
        break
    image_path = os.path.join(TEST_DIR, image_name)
    frame = cv2.imread(image_path)
    frame = cv2.resize(frame, (frame.shape[1]//4, frame.shape[0]//4))

    raw_image_path = os.path.join(RAW_DIR, raw_image_list[ind])
    raw_image = cv2.imread(raw_image_path)
    raw_image = cv2.resize(raw_image, (raw_image.shape[1]//4, raw_image.shape[0]//4))

    both_images = cv2.vconcat([raw_image, frame])
    print(both_images.shape)
    out.write(both_images)

    cv2.imshow('frame',both_images)
    cv2.waitKey(1)
# When everything done, release the video capture and video write objects
out.release()

# Closes all the frames
cv2.destroyAllWindows() 
