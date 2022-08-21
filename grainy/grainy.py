# Importing the OpenCV, Numpy and Matplotlib libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading image from folder where it is stored
img_input = cv2.imread('zira.jpg', cv2.IMREAD_UNCHANGED)
  
# Denoising of image saving it into dst image
dst = cv2.fastNlMeansDenoisingColored(img_input, None, 10, 10, 7, 15)

# Display the images
cv2.imwrite('After.jpg',dst)

cv2.imshow('Before', img_input)
cv2.imshow('After', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()