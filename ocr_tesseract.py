import cv2
import numpy as np
import pytesseract as py
import re
import textblob
from textblob import TextBlob
from autocorrect import Speller
import time
from gtts import gTTS
import PIL
from PIL import Image

start = time.time()


cap = cv2.VideoCapture('testvideo.mp4')
print("Creating Frames")

def getFrames(sec):
     cap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
     result, frame = cap.read()
     if result:
         cv2.imwrite("testimage_" + str(count) + ".png", frame)
         return result
sec = 0
frameRate = 1/24
count = 0
obj1 = getFrames(sec)


similarity_ratio = []
while obj1:
     count += 1
     sec = sec + frameRate
     sec = round(sec, 2)
     obj1 = getFrames(sec)

print("Frames created")

print("Determining Similarity Ratios")
for i in range(1, count-1):
     im1 = cv2.imread('testimage_{}.png'.format(i))
     im2 = cv2.imread('testimage_{}.png'.format(i+1))
     img1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
     img2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
     arr1 = np.array(img1)
     arr2 = np.array(img2)
     dim1 = np.shape(arr1)
     dim2 = np.shape(arr2)
     total_elements1 = dim1[0]*dim1[1]
     total_elements2 = dim2[0]*dim2[1]
     sub = arr1 -arr2
     z = np.count_nonzero(sub)
     dim3 = np.shape(sub)
     total_elements3 = dim3[0]*dim3[1]
     zero_elements = total_elements3 - z
     sim_ratio = total_elements3/zero_elements
     # print(sim_ratio)
     similarity_ratio.append(sim_ratio)
print(similarity_ratio)

length = len(similarity_ratio)
ofl = int((12*length)/100)
temp_to_be_added = []

print(length)
for i in range(0, length, ofl):
     for j in range(i, (i+ofl) and length):
          if 1.0 <= similarity_ratio[j] <= 1.09:
               temp_to_be_added = temp_to_be_added + [j]


print(temp_to_be_added)

for i in temp_to_be_added:
    img = Image.open('testimage_{}.png'.format(i))
    output = py.image_to_string(img)
    print(output)

text = output


word = text
reg = re.compile(r'[a-zA-Z]')

if reg.match(word):
    print("language is english")
else:
    print("language is not english")
lang = 'en'
obj = gTTS(text = word, lang = lang, slow = False)
obj.save('testaudio.mp3')

end = time.time() - start
print(end)
