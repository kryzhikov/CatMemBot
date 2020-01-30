import cv2
import pytesseract

img = cv2.imread("/Users/kirillryzikov/Desktop/ML/Projects/CatMembot/downloads/ kitten/260.maxresdefault.jpg")
print(pytesseract.image_to_string(img))