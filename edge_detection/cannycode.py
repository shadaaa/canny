import cv2
import numpy as np
image = cv2.imread("C:/Users/ASUS/OneDrive/Desktop/bean.jpg", cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(image, (5,5),0)
edges = cv2.Canny(blurred, threshold1=30,threshold2=100)
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
