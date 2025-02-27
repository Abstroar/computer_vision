import cv2
import numpy as np


def region_growing(image, seed, threshold=80):
    h, w = image.shape
    visited = np.zeros_like(image, dtype=bool)
    region = np.zeros_like(image, dtype=np.uint8)

    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0),
                 (1, 1), (-1, -1), (1, -1), (-1, 1)]

    seed_value = image[seed]
    stack = [seed]

    while stack:
        x, y = stack.pop()
        if visited[x, y]:
            continue

        visited[x, y] = True

        if abs(int(image[x, y]) - int(seed_value)) < threshold:
            region[x, y] = 255

            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx, ny]:
                    stack.append((nx, ny))

    return region



image = cv2.imread("x1.jpg", cv2.IMREAD_GRAYSCALE)


seeds = [
 (450, 620),   # chair
 (120, 500), # bulb
    (100, 900)   # window
]


thresholds = [
     80,   #chair
     100,   # bulb
     100,   # window
]
x= 3

final_result = np.zeros_like(image, dtype=np.uint8)

for i in range(0,x):
    region = region_growing(image, seeds[i], thresholds[i])
    final_result = cv2.bitwise_or(final_result, region)
final_result = cv2.bitwise_not(final_result)

cv2.imshow("Region Growing Result (Multiple Objects)", final_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
