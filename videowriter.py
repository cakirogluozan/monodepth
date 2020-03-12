import cv2, os
import numpy as np

write = False

ROOT_DIR = os.getcwd()
DATA_DIR = os.path.join(ROOT_DIR, 'data')
OUTPUT_DIR = os.path.join(DATA_DIR, 'output')
INPUT_DIR = os.path.join(DATA_DIR, 'input')


input_image_list = [i for i in os.listdir(INPUT_DIR) if i.endswith('leftImg8bit.jpg')]
input_image_list.sort(key=lambda a:int(a.split('_')[2]))

output_image_list = [i for i in os.listdir(OUTPUT_DIR) if i.endswith('.png')]
output_image_list.sort(key=lambda a:int(a.split('_')[2]))

if write:
    dummy_image_path = os.path.join(INPUT_DIR, input_image_list[0])
    dummy_image = cv2.imread(dummy_image_path)

    width, height, channels = dummy_image.shape

    output_dir = 'monodepth_ozan.avi'
    fourcc =  cv2.VideoWriter_fourcc('M','J','P','G')
    fps = 30
    out = cv2.VideoWriter(output_dir, fourcc, fps, (height//2, width//4))

for ind, image_name in enumerate(input_image_list):
    input_image_path = os.path.join(INPUT_DIR, image_name)
    input_image = cv2.imread(input_image_path)
    input_image = cv2.resize(input_image, (input_image.shape[1]//4, input_image.shape[0]//4))

    output_image_path = os.path.join(OUTPUT_DIR, output_image_list[ind])
    output_image = cv2.imread(output_image_path)
    output_image = cv2.resize(output_image, (output_image.shape[1]//4, output_image.shape[0]//4))

    both_images = cv2.hconcat([input_image, output_image])
    if write:
        out.write(both_images)

    cv2.imshow('frame',both_images)
    cv2.waitKey(1)
# When everything done, release the video capture and video write objects
out.release()

# Closes all the frames
cv2.destroyAllWindows() 
