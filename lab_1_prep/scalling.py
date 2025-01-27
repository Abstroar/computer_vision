import cv2
import numpy as np

def scalling_12(x, y, cx, cy):
    scale = [[cx, 0, 0], [0, cy, 0], [0, 0, 1]]
    mat_input = ([x, y, 1])
    output = np.matmul(scale, mat_input)
    return int(output[0]), int(output[1])

def scaling(image, cx, cy):
    height, width = image.shape
    scaled_height = int(height * cy)
    scaled_width = int(width * cx)
    scaled_image = np.zeros((scaled_height, scaled_width), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            a,b = scalling_12(x,y,cx,cy)
            if 0 <= a < scaled_width and 0 <= b < scaled_height:
                scaled_image[b, a] = image[y, x]
    return scaled_image


def nd_neighborhood_interpolation(image):
    height, width = image.shape
    interpolated_image = np.zeros_like(image, dtype=np.uint8)

    for x in range(1, height - 1):
        for y in range(1, width - 1):
            up_left = int(image[x - 1, y - 1])
            down_left = int(image[x + 1, y - 1])
            up_right = int(image[x - 1, y + 1])
            down_right = int(image[x + 1, y + 1])

            interpolated_value = (up_left + down_left + up_right + down_right) // 4
            interpolated_image[x, y] = np.clip(interpolated_value, 0, 255)  # Ensure value stays within valid range

    return interpolated_image

image = cv2.imread("small_image_1.jpg", cv2.IMREAD_GRAYSCALE)

cx = float(input("Scaling for x axis :"))
cy = float(input("Scaling for y axis :"))
scaled_image = scaling(image, cx, cy)

cv2.imshow("Original Image", image)
cv2.imshow("Scaled Image", scaled_image)
cv2.imshow("Scaled interpolated Image", nd_neighborhood_interpolation(scaled_image))
cv2.waitKey(0)
cv2.destroyAllWindows()
