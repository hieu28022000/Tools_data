import cv2
import glob
import os

for img in glob.glob('*.jpg'):
    name = img
    img = cv2.imread(img) 
    (h, w, d) = img.shape 
    center = (w // 2, h // 2) 
    M = cv2.getRotationMatrix2D(center, 180, 1.0) 
    rotated = cv2.warpAffine(img, M, (w, h))
    cv2.imwrite(str(name), rotated)
    print(name)