import cv2
import numpy as np
import pytesseract as py

cap = cv2.VideoCapture('testvideo.mp4')

def getFrames(sec):
    cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    result, frame = cap.read()
    if result:
        cv2.imwrite("img" + str(count) + ".png", frame)
        return result


sec = 0
frameRate = 2
count = 1
obj1 = getFrames(sec)

similarity_ratio = []
while obj1:
    count += 1
    sec = sec + frameRate
    sec = round(sec, 2)
    obj1 = getFrames(sec)

for i in range(1, count +1):
    img = cv2.imread('img{}.png'.format(i))
    output = py.image_to_string(img)
    print('output: ', output)

# if:
#     u =10
# elif: