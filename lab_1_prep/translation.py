
import numpy as np
import cv2

def translate(x, y, tx, ty):
    translation = [[1, 0, tx], [0, 1, ty], [0, 0, 1]]
    mat_input = [x, y, 1]
    output = np.matmul(translation, mat_input)
    return output[0], output[1]

image = cv2.imread("small_image_1.jpg", cv2.IMREAD_GRAYSCALE)

size_x, size_y = image.shape
tx = int(input("Translation in x-direction: "))
ty = int(input("Translation in y-direction: "))

new_x = size_x + abs(ty)
new_y = size_y + abs(tx)
mtx2 = np.zeros((new_x, new_y), dtype=np.uint8)

for i in range(size_x):
    for j in range(size_y):
        x, y = translate(i, j, tx, ty)
        x = int(round(x))
        y = int(round(y))
        if 0 <= x < new_x and 0 <= y < new_y:
            mtx2[x, y] = image[i, j]

cv2.imshow("Input", image)
cv2.imshow("Translated Image", mtx2)
cv2.waitKey(0)
cv2.destroyAllWindows()
