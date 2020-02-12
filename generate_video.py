# AppDemoVideoGenerator
# generate_video 
# Created by Yigang Zhou on 2020-02-12.
# Copyright © 2020 Yigang Zhou. All rights reserved.
import cv2
from util import load_mask
from util import generate_masked_frame
import argparse

# python3.6 generate_image.py -device "iPhone 11 Pro.png" -screen "app.mp4"
parser = argparse.ArgumentParser()
parser.add_argument('-device', help='device background')
parser.add_argument('-screen', help='screen record')
args = parser.parse_args()

# load device background image and convert to hsv
background = cv2.cvtColor(cv2.imread(args.device), cv2.COLOR_BGR2RGB)
background_hsv = cv2.cvtColor(background, cv2.COLOR_RGB2HSV)

# load mask
mask, mask_rect = load_mask(background_hsv)
x, y, w, h = mask_rect

# load video
cap = cv2.VideoCapture(args.screen)
four_cc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
print("Video frame rate", fps)

# generate video
out = cv2.VideoWriter("out.mp4", four_cc, fps, (background.shape[1], background.shape[0]))
print("Generating  video")

while cap.isOpened():

    ret, frame = cap.read()

    if ret:
        masked_frame, final_image = generate_masked_frame(background, mask, mask_rect, frame)
        out.write(cv2.cvtColor(final_image, cv2.COLOR_RGB2BGR))

    else:
        break

print("success")
cap.release()
out.release()
