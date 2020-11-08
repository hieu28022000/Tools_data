import cv2
import numpy as np
import os
import glob


def detect_oval(image):
    img = cv2.imread(image)
    img_1 = img[:,:,0]
    # print(type(img))
    # print(img_1)
    # print(np.unique(img_1))
    # print(img_1.shape)

    X=[]
    Y=[]
    for y in range(img_1.shape[0]):
        for x in range(img_1.shape[1]):
            if (img_1[y][x] != 0):
                X.append(x)
                Y.append(y)
                # print(x, y)

    x_min = 800
    y_min = 540
    x_max = 0
    y_max = 0
    for x in X:
        if x_min > x:
            x_min = x
        if x_max < x:
            x_max = x
    for y in Y:
        if y_min > y:
            y_min = y
        if y_max < y:
            y_max = y

    w = x_max - x_min
    h = y_max - y_min
    x_center = int((x_min + x_max) / 2)
    y_center = int((y_min + y_max) / 2)

    # print('Min', x_min, y_min)
    # print('Max', x_max, y_max)
    # print('X_Center', x_center)
    # print('Y_Center', y_center)
    # print('Width', w)
    # print('Higth', h)

    # visualize = cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (100,0,0))
    # cv2.imshow('Visualize', visualize)
    name = image.split('.')[0]
    name = str(name + '.txt')
    with open(name, 'a', encoding = 'utf-8') as f:
        f.write(str(0)+" ") 
        f.write(str(x_center/800) +" ")
        f.write(str(y_center/540)+" ")
        f.write(str(w/800)+" ")
        f.write(str(h/540))     
        f.write("\n")

    return img, name

if __name__ == '__main__':
    for img in glob.glob('images/*.png'):
        images, path = detect_oval(img)

        cv2.waitKey(0)