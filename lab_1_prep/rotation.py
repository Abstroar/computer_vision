import math
import random

import numpy as np
import cv2

def Roatation(input_x, input_y, rx):
    cos_value = math.cos(rx)
    sine_value = math.sin(rx)
    scale = [[cos_value, sine_value, 0], [-sine_value, cos_value, 0], [0, 0, 1]]
    mat_input = [input_x, input_y, 1]
    output = np.matmul(scale, mat_input)
    return output[0], output[1]

image = cv2.imread("small_image_1.jpg", cv2.IMREAD_GRAYSCALE)

size_x, size_y = image.shape

rx = 45

new_x = math.sqrt((size_x*size_x)+(size_y*size_y))
new_y = math.sqrt((size_x*size_x)+(size_y*size_y))
mtx2 = np.zeros((int(new_x), int(new_y)), dtype=np.uint8)

for i in range(size_x):
    for j in range(size_y):
        x, y = Roatation(i, j, rx)
        x = int(round(x))
        y = int(round(y))
        if 0 <= x < new_x and 0 <= y < new_y:
            mtx2[x, y] = image[i, j]


cv2.imshow("Original image", image)
cv2.imshow("Translated Image", mtx2)
cv2.waitKey(0)
cv2.destroyAllWindows()