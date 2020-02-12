# AppDemoVideoGenerator
# generate_image.py 
# Created by Yigang Zhou on 2020-02-12.
# Copyright © 2020 Yigang Zhou. All rights reserved.
import cv2
import matplotlib.pyplot as plt
from util import load_mask
from util import generate_masked_frame
import argparse

# python3.6 generate_image.py -device "iPhone 11 Pro.png" -screen "frame.png"
parser = argparse.ArgumentParser()
parser.add_argument('-device', help='device background')
parser.add_argument('-screen', help='screenshot')
args = parser.parse_args()

# load device background image and convert to hsv
background = cv2.cvtColor(cv2.imread(args.device),cv2.COLOR_BGR2RGB)
background_hsv = cv2.cvtColor(background, cv2.COLOR_RGB2HSV)

# generate mask
mask, mask_rect = load_mask(background_hsv)
x, y, w, h = mask_rect

# apply mask to screenshot
frame = cv2.imread(args.screen)
masked_frame, final_image = generate_masked_frame(background, mask, mask_rect, frame)

f, ax = plt.subplots(1, 4, figsize=(20, 10))
ax[0].imshow(background)
ax[1].imshow(mask)
ax[2].imshow(masked_frame)
ax[3].imshow(final_image)
f.savefig("fig.png")
cv2.imwrite("out.png", cv2.cvtColor(final_image, cv2.COLOR_RGB2BGR))