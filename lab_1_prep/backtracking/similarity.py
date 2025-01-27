import numpy as np
import cv2


def similarity_transform(x, y, tx, ty, angle, scale_x, scale_y):
    x_scaled = x * scale_x
    y_scaled = y * scale_y

    angle_rad = np.deg2rad(angle)
    x_rot = x_scaled * np.cos(angle_rad) - y_scaled * np.sin(angle_rad)
    y_rot = x_scaled * np.sin(angle_rad) + y_scaled * np.cos(angle_rad)

    x_translated = x_rot + tx
    y_translated = y_rot + ty

    return x_translated, y_translated


image = cv2.imread("small_image_1.jpg", cv2.IMREAD_GRAYSCALE)

size_x, size_y = image.shape
tx = int(input("Translation in x-direction: "))
ty = int(input("Translation in y-direction: "))
angle = float(input("Rotation angle (in degrees): "))
scale_x = float(input("Scaling factor in x-direction: "))
scale_y = float(input("Scaling factor in y-direction: "))


new_x = int(size_x * scale_y) + abs(ty)
new_y = int(size_y * scale_x) + abs(tx)
mtx2 = np.zeros((new_x, new_y), dtype=np.uint8)

for i in range(new_x):
    for j in range(new_y):
        x, y = similarity_transform(i, j, tx, ty, angle, scale_x, scale_y)
        x = int(round(x))
        y = int(round(y))

        if 0 <= x < size_x and 0 <= y < size_y:
            mtx2[i, j] = image[x, y]

cv2.imshow("Input", image)
cv2.imshow("Transformed Image (Similarity)", mtx2)
cv2.waitKey(0)
cv2.destroyAllWindows()