import numpy as np
import cv2
import os
from PIL import Image
from PIL import ImageEnhance

import numpy as np
import warnings
import random
old_path = "C:/Users/11409/Desktop/88/yes"
new_path = "C:/Users/11409/Desktop/88/yes1"

# if not exist make dir
if not os.path.exists(new_path):
    os.mkdir(new_path)
# get the image list
img_list = os.listdir(old_path)

for i in range(len(img_list)):
    print(i)
    # get the path of every image
    old_image_path = os.path.join(old_path, img_list[i])
    img = cv2.imread(old_image_path, cv2.IMREAD_UNCHANGED)
    img=img
    rows, cols, dims = img.shape
    # add noise to image
    for j in range(1000):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        img[x, y, :] = 255
    for k in range(1000):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        img[x, y, :] = 0
    # save the new image
    new_image_path = os.path.join(new_path, img_list[i])
    cv2.imwrite(new_image_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    # show the image
    # cv2.imshow("Demo", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
