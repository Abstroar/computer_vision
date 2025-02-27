import cv2
import numpy as np


def region_growing(image, seed, threshold=100):
    h, w = image.shape
    visited = np.zeros_like(image, dtype=bool)
    region = np.zeros_like(image, dtype=np.uint8)

    # Define 4-connected neighbors (or 8-connected for diagonal inclusion)
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0),
                 (1, 1), (-1, -1), (1, -1), (-1, 1) ]

    # Start with the seed pixel
    seed_value = image[seed]
    stack = [seed]

    while stack:
        x, y = stack.pop()

        if visited[x, y]:
            continue

        visited[x, y] = True

        # Check intensity difference
        if abs(int(image[x, y]) - int(seed_value)) < threshold:
            region[x, y] = 255  # Mark as part of the region

            # Check neighbors
            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx, ny]:
                    stack.append((nx, ny))

    return region


# Load grayscale image
image = cv2.imread("x1.jpg", cv2.IMREAD_GRAYSCALE)

# # Define seed point
seed = (450, 620)  # Change based on your object location
# edges = cv2.Canny(image, 50, 150)  # Detect edges
# y, x = np.where(edges > 0)  # Get nonzero edge points
# seed = (y[0], x[0])  # Pick first edge point
# Apply region growing
result = region_growing(image, seed, threshold=120)

# Show result
cv2.imshow("Region Growing Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
