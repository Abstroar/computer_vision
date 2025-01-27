import cv2
import numpy as np

image = cv2.imread("small_image_1.jpg", cv2.IMREAD_GRAYSCALE)

size_x,size_y = image.shape

segmented_img = np.zeros((size_x, size_y), dtype=np.uint8)
Thresh = 127


for i in range(size_x):
    for j in range(size_y):
        if image[i][j] > Thresh:
            segmented_img[i][j] = 255
        else:
            segmented_img[i][j] = 0

cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented_img)
cv2.waitKey(0)
cv2.destroyAllWindows()