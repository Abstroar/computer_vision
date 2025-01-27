import cv2
import numpy as np

def back_scaling_12(x, y, cx, cy):
    scale = [[1/cx, 0, 0], [0, 1/cy, 0], [0, 0, 1]]
    mat_input = ([x, y, 1])
    output = np.matmul(scale, mat_input)
    return int(output[0]), int(output[1])

def back_scaling(image, cx, cy):
    height, width = image.shape
    scaled_height = int(height * cy)
    scaled_width = int(width * cx)
    scaled_image = np.zeros((scaled_height, scaled_width), dtype=np.uint8)

    for y in range(scaled_height):
        for x in range(scaled_width):
            a,b = back_scaling_12(x,y,cx,cy)
            if 0 <= a < height and 0 <= b < width:
                scaled_image[y, x] = image[b, a]
    return scaled_image

image = cv2.imread("small_image_1.jpg", cv2.IMREAD_GRAYSCALE)

cx = float(input("Scaling for x axis :"))
cy = float(input("Scaling for y axis :"))
scaled_image = back_scaling(image, cx, cy)

cv2.imshow("Original Image", image)
cv2.imshow("Scaled Image", scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
