import cv2
import numpy as np

# Step 1: Load the image
image = cv2.imread('small_image_1.jpg')


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_image = np.float32(gray_image)


dst = cv2.cornerHarris(gray_image, 2, 3, 0.04)

#
dst = cv2.dilate(dst, None)


image[dst > 0.01 * dst.max()] = [0, 0, 0]

# side_by_side = np.hstack((image, image_with_corners))
# cv2.imshow('Original vs Corner Detection', side_by_side)
cv2.imshow('Harris Corner Detection', image)

# Step 8: Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
