import cv2
import numpy as np

# Load an image in grayscale mode
image = cv2.imread(r'C:\Users\Kelzang\OneDrive\Desktop\Computer Vision\Lab\ThirdWeek\ti1.png', cv2.IMREAD_GRAYSCALE)

threshold_value = 197
max_value = 255
_, binary_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

# Display the original and binary images
cv2.imshow('Original Image', image)
cv2.imshow('Binary Image', binary_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()