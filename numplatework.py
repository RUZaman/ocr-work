'''How to create number plate detection on python'''
import cv2
import numpy as np
import pytesseract
import imutils


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread("scan.jpg")


text = pytesseract.image_to_string(image, lang='eng')
print("Result : ", text)



# cv2.imshow('Gray Image', gray)
# cv2.imshow('Smoother', gray)
# cv2.imshow("canny image", edge)
# cv2.imshow("Canny after contours", image1)
# cv2.imshow("Top 30 contours",image2)
cv2.imshow("Final Image", image)
cv2.waitKey(0)