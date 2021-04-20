# encoding: utf-8

import math
from PIL import Image
import numpy as np
import random
import cv2

def GRPC(img_path):
    img = Image.open(img_path)

    new = img.convert("L")
    np_img = np.array(new, dtype=np.uint8)
    img_gray = np.dstack([np_img, np_img, np_img])

    # if random.uniform(0, 1) >= 0.2:
    #     # return img
    #     img.show()

    for attempt in range(100):
        area = img.size[0] * img.size[1] # 原图的面积
        target_area = random.uniform(0.02, 0.4) * area # 待灰度区域的面积
        aspect_ratio = random.uniform(0.3, 1/0.3) # 待灰度区域的形状

        h = int(round(math.sqrt(target_area * aspect_ratio)))
        w = int(round(math.sqrt(target_area / aspect_ratio)))

        if w < img.size[1] and h < img.size[0]:
            x1 = random.randint(0, img.size[0]-h)
            y1 = random.randint(0, img.size[1]-w)
            img = np.asarray(img).astype('float')

            img[y1:y1 + h, x1:x1 + h, 0] = img_gray[y1:y1 + h, x1:x1 + h, 0]
            img[y1:y1 + h, x1:x1 + h, 1] = img_gray[y1:y1 + h, x1:x1 + h, 1]
            img[y1:y1 + h, x1:x1 + h, 2] = img_gray[y1:y1 + h, x1:x1 + h, 2]

            img_new = Image.fromarray(img.astype('uint8'))
            img_new.show()


if __name__ == '__main__':
    img_path = "../qixing3.jpg"
    GRPC(img_path)






