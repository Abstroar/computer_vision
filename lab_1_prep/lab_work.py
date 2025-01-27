import numpy as np
import cv2
def scalling(x, y, cx, cy):
    scale = [[cx, 0, 0], [0, cy, 0], [0, 0, 1]]
    mat_input = ([x, y, 1])
    output = np.matmul(scale, mat_input)
    return output[0], output[1]

image = cv2.imread("small_image_1.jpg", cv2.IMREAD_GRAYSCALE)
size_x,size_y = image.shape
cx = float(input("Scale in x-axis"))
cy = float(input("Scale in y-axis"))

new_x = int(size_x * cx)
new_y = int(size_y * cy)
mtx2 = np.zeros((new_x, new_y), dtype=np.uint8)
for i in range(size_x):
    for j in range(size_y):
        x, y = scalling(i, j, cx, cy)
        x = int(round(x))
        y = int(round(y))
        if x < new_x and y < new_y:
            mtx2[int(x)][int(y)] = image[i, j]

cv2.imshow("Input",image)
cv2.imshow("image", mtx2)
key = cv2.waitKey(0)
if key == 27:  # "Esc" key
    cv2.destroyAllWindows()