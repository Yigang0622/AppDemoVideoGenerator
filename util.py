# AppDemoVideoGenerator
# background 
# Created by Yigang Zhou on 2020-02-12.
# Copyright © 2020 Yigang Zhou. All rights reserved.
import cv2
import numpy as np


def load_mask(background_hsv):
    mask = cv2.inRange(background_hsv, (35, 43, 46), (77, 255, 255))
    mask_i = np.where(mask == 255)
    y = np.min(mask_i[0])
    x = np.min(mask_i[1])
    w = np.max(mask_i[1]) - np.min(mask_i[1])
    h = np.max(mask_i[0]) - np.min(mask_i[0])
    return mask, (x, y, w, h)


def generate_masked_frame(background, mask, mask_rect, frame):
    x, y, w, h = mask_rect
    frame = cv2.resize(frame, (w, h))
    masked_frame = np.zeros(background.shape, np.uint8)
    masked_frame[y:y+h, x:x+w] = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    masked_frame[mask != 255] = [0, 0, 0]

    crop_background = background.copy()
    crop_background[mask == 255] = [0, 0, 0]

    final_image = crop_background + masked_frame

    return masked_frame, final_image