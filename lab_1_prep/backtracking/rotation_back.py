import numpy as np
import cv2
import math

def Roatation(input_x, input_y, rx):
    rx = math.radians(rx)
    cos_value = math.cos(rx)
    sine_value = math.sin(rx)
    rotate = [[cos_value, sine_value, 0], [-sine_value, cos_value, 0], [0, 0, 1]]
    mat_input = [input_x, input_y, 1]
    output = np.matmul(rotate, mat_input)
    return output[0], output[1]


def inverse_rotate(x,y, rx,center_x, center_y):
    rx = math.radians(rx)
    cos_value = math.cos(rx)
    sine_value = math.sin(rx)

    x_translated = x - center_x
    y_translated = y - center_y


    rotate = [[cos_value, sine_value, 0], [-sine_value, cos_value, 0], [0, 0, 1]]
    mat_input = [x_translated, y_translated, 1]
    output = np.matmul(rotate, mat_input)

    x_rotated = output[0] + center_x
    y_rotated = output[1] + center_y

    return output[0], output[1]

image = cv2.imread("small_image_1.jpg", cv2.IMREAD_GRAYSCALE)

size_x, size_y = image.shape
rx = int(input("Rotation in angle: in degree "))

new_x = int(math.sqrt((size_x*size_x)+(size_y*size_y)))
new_y = int(math.sqrt((size_x*size_x)+(size_y*size_y)))
# new_x = size_x
# new_y = size_y
mtx2 = np.zeros((int(new_x), int(new_y)), dtype=np.uint8)

original_center_x = size_x / 2
original_center_y = size_y / 2
new_center_x = size_x
new_center_y = 0

for i in range(new_x):
    for j in range(new_y):
        x, y = inverse_rotate(i, j, rx, new_center_x, new_center_y)
        x = int(round(x))
        y = int(round(y))

        if 0 <= x < size_x and 0 <= y < size_y:
            mtx2[i, j] = image[x, y]

cv2.imshow("Input", image)
cv2.imshow("Translated Image (Backward Wrapping)", mtx2)
cv2.waitKey(0)
cv2.destroyAllWindows()
