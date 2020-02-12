# AppDemoVideoGenerator
# main 
# Created by Yigang Zhou on 2020-02-12.
# Copyright © 2020 Yigang Zhou. All rights reserved.

import cv2
import numpy as np
import matplotlib.pyplot as plt
from util import load_mask
from util import generate_masked_frame

background = cv2.cvtColor(cv2.imread("/Users/mike/PycharmProjects/AppDemoVideoGenerator/test/color_spectrum.png"),cv2.COLOR_BGR2RGB)
background_hsv = cv2.cvtColor(background, cv2.COLOR_RGB2HSV)

mask, mask_rect = load_mask(background_hsv)
x, y, w, h = mask_rect


f, ax = plt.subplots(2,1,figsize=(15,10))
ax[0].imshow(background)
ax[1].imshow(mask)


plt.show()
# f.savefig("spectrum.png")
