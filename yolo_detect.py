import cv2
import numpy as np
import os
import random
import imutils
import time
import glob
import numba

from numba import jit, cuda 
from timeit import default_timer as timer  

net = cv2.dnn.readNet("yolov3_last.weights", "yolov3.cfg")
output_path = os.path.join("output", "out_img.jpg")
# Name custom object
classesFile = "obj.names";

classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# @jit(target ="cuda") 
def detect_image(img):

    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
            cv2.putText(img, label, (x, y-2), font, 1, color, 2)
    # output_image = img[y:(y+h), x:(x+w), :]
    
    # Store image
    cv2.imwrite(output_path, img)   

    return img, output_path

def detect_video(video_path):
    # start detect video
    cap = cv2.VideoCapture(video_path)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    ret, frame = cap.read()
    WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    writer = cv2.VideoWriter("output/Vid.avi",codec,15,(WIDTH,HEIGHT))
    cap.release()
    counts = 0
    cap = cv2.VideoCapture(video_path)
    while (True):
        ret, frame = cap.read() 
        height, width, channels = frame.shape

        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)

        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    print(class_id)
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                cv2.putText(frame, label, (x, y-2), font, 1, color, 2)
    
        counts += 1
        # cv2.imshow('detection', frame)
        writer.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if not os.path.exists("output"):
        os.mkdir("output")

    # # Detect video
    # detect_video('input/Vid.mp4')

    # Detec image
    start = timer()
    image, image_path = detect_image(cv2.imread('input/in_img.jpg'))
    cv2.imshow('Images', image)
    print('No use GPU: ', timer()-start)


    # cuda.select_device(0)
    # start = timer()
    # image, image_path = detect_image(cv2.imread('input/data_33.jpeg'))
    # # cv2.imshow('Images', image)
    # print('Use GPU', timer()-start)
    # cuda.close()

    # cv2.waitKey(0)