import numpy as np
import cv2




def inverse_translate(x, y, tx, ty):
    """Inverse translation of a point (x, y) by (tx, ty)."""
    inverse_translation = [[1, 0, -tx], [0, 1, -ty], [0, 0, 1]]
    mat_input = [x, y, 1]
    output = np.matmul(inverse_translation, mat_input)
    return output[0], output[1]


image = cv2.imread("small_image_1.jpg", cv2.IMREAD_GRAYSCALE)

size_x, size_y = image.shape
tx = int(input("Translation in x-direction: "))
ty = int(input("Translation in y-direction: "))

new_x = size_x + abs(ty)
new_y = size_y + abs(tx)
mtx2 = np.zeros((new_x, new_y), dtype=np.uint8)

for i in range(new_x):
    for j in range(new_y):
        x, y = inverse_translate(i, j, tx, ty)
        x = int(round(x))
        y = int(round(y))

        if 0 <= x < size_x and 0 <= y < size_y:
            mtx2[i, j] = image[x, y]

cv2.imshow("Input", image)
cv2.imshow("Translated Image (Backward Wrapping)", mtx2)
cv2.waitKey(0)
cv2.destroyAllWindows()
