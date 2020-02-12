# AppDemoVideoGenerator
# main 
# Created by Yigang Zhou on 2020-02-12.
# Copyright © 2020 Yigang Zhou. All rights reserved.

import cv2
import numpy as np
import matplotlib.pyplot as plt
from util import load_mask
from util import generate_masked_frame

background = cv2.cvtColor(cv2.imread("iPhone 11 Pro.png"),cv2.COLOR_BGR2RGB)
background_hsv = cv2.cvtColor(background, cv2.COLOR_RGB2HSV)

mask, mask_rect = load_mask(background_hsv)
x, y, w, h = mask_rect

frame = cv2.imread("frame.png")
masked_frame, final_image = generate_masked_frame(background, mask, mask_rect, frame)


f, ax = plt.subplots(1,4,figsize=(20,10))
ax[0].imshow(background)
ax[1].imshow(mask)
ax[2].imshow(masked_frame)
ax[3].imshow(final_image)

# plt.show()
f.savefig("fig.png")
#
cv2.imwrite("1.png", cv2.cvtColor(final_image, cv2.COLOR_RGB2BGR))

#
cap = cv2.VideoCapture('app.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
print("Video frame rate", fps)

out = cv2.VideoWriter("out.mp4", fourcc, int(fps), (background.shape[1], background.shape[0]))


while (cap.isOpened()):

    ret, frame = cap.read()

    if ret == True:
        frame_h = frame.shape[0]
        frame_w = frame.shape[1]
        frame = cv2.resize(frame, (w, h))

        masked_frame = np.zeros(background.shape, np.uint8)
        masked_frame[y:y + h, x:x + w] = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        masked_frame[mask != 255] = [0, 0, 0]

        crop_background = background.copy()
        crop_background[mask == 255] = [0, 0, 0]

        final_image = crop_background + masked_frame
        out.write(cv2.cvtColor(final_image, cv2.COLOR_RGB2BGR))

    else:
        break

print("success")
cap.release()
out.release()
