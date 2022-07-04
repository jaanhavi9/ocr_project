import re
import re
import cv2
import pytesseract as pt
im = cv2.imread('test_image.png')

ret, bw_img = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
text = pt.image_to_string(bw_img)
print(text)
word = 'こんにちは'
reg = re.compile(r'[a-zA-Z]')

if reg.match(word):
    print("It is an alphabet")
else:
    print("It is not an alphabet")

word = "أهلا"
reg = re.compile(r'[a-z]')
if reg.match(word):
    print("It is an alphabet")
else:
    print("It is not an alphabet")
