import numpy as np


def n4_neighbourhood(image, x, y):
    up = image[x - 1, y]
    down = image[x + 1, y]
    left = image[x, y - 1]
    right = image[x, y + 1]
    return (up + down + left + right) // 4

def nd_neighbourhood(image, x, y):
    up_left = image[x - 1, y - 1]
    down_left = image[x + 1, y - 1]
    up_right = image[x - 1, y + 1]
    down_right = image[x + 1, y + 1]
    return (up_left + down_left + up_right + down_right) // 4

def n8_neighbourhood(image, x, y):
    up_left = image[x - 1, y - 1]
    down_left = image[x + 1, y - 1]
    up_right = image[x - 1, y + 1]
    down_right = image[x + 1, y + 1]
    up = image[x - 1, y]
    down = image[x + 1, y]
    left = image[x, y - 1]
    right = image[x, y + 1]
    return (up_left + down_left + up_right + down_right + up + down + left + right) // 8

def n4_neighborhood_interpolation(image):
    height, width = image.shape
    interpolated_image = np.zeros_like(image, dtype=np.uint8)

    for x in range(1, height - 1):
        for y in range(1, width - 1):
            interpolated_value = n4_neighbourhood(image, x, y)
            interpolated_image[x, y] = np.clip(interpolated_value, 0, 255)

    return interpolated_image

def nd_neighborhood_interpolation(image):
    height, width = image.shape
    interpolated_image = np.zeros_like(image, dtype=np.uint8)

    for x in range(1, height - 1):
        for y in range(1, width - 1):
            interpolated_value = nd_neighbourhood(image, x, y)
            interpolated_image[x, y] = np.clip(interpolated_value, 0, 255)

    return interpolated_image

def n8_neighborhood_interpolation(image):
    height, width = image.shape
    interpolated_image = np.zeros_like(image, dtype=np.uint8)

    for x in range(1, height - 1):
        for y in range(1, width - 1):
            interpolated_value = n8_neighbourhood(image, x, y)
            interpolated_image[x, y] = np.clip(interpolated_value, 0, 255)

    return interpolated_image