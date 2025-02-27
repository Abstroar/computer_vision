import cv2

# Load the image
image = cv2.imread("x1.jpg")

# Mouse click callback function
def select_pixel(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
        pixel_value = image[y, x]  # Get pixel value (BGR for color, grayscale otherwise)
        print(f"Selected Pixel: ({x}, {y}) - Value: {pixel_value}")

# Create a window and set mouse callback
cv2.imshow("Select a Seed Pixel", image)
cv2.setMouseCallback("Select a Seed Pixel", select_pixel)

cv2.waitKey(0)
cv2.destroyAllWindows()
