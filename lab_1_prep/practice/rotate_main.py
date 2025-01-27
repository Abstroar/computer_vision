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

size = 502

mtx2 = np.zeros((size, size), dtype=np.uint8)
mt1 = np.zeros((size, size), dtype=np.uint8)
for i in range(230, 270):
    for j in range(230, 270):
        mt1[i, j] = random.randint(0,255)

cv2.imshow("input", mt1)
offset = size // 2
# cx=float(input("enter cx"))
# cy=float(input("enter cy"))
cx = 60

for i in range(len(mt1)):
    for j in range(len(mt1)):
        x, y = Roatation(i - offset, j - offset, math.radians(cx))
        x = int(round(x)) + offset
        y = int(round(y)) + offset

        if 0 <= x < size and 0 <= y < size:
            mtx2[x][y] = mt1[i, j]
        else:
            pass
print(mtx2)
resized_image = cv2.warpAffine(mt1, mtx2, (size, size), flags=cv2.INTER_LINEAR)
cv2.imshow("image", resized_image)
key = cv2.waitKey(0)
if key == 27:  # "Esc" key
    cv2.destroyAllWindows()