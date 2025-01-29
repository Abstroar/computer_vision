import numpy as np
import cv2

def otsu_threshold(image):
    # Step 1: Compute normalized histogram
    hist, _ = np.histogram(image.ravel(), bins=256, range=(0, 256), density=True)
    
    # Step 2: Compute cumulative sums
    P1 = np.cumsum(hist)
    
    # Step 3: Compute cumulative means
    m = np.cumsum(hist * np.arange(256))
    
    # Step 4: Compute global intensity mean
    mG = m[-1]
    
    # Step 5: Compute between-class variance
    sB2 = (mG * P1 - m) ** 2 / (P1 * (1 - P1) + 1e-6)  # Add small value to avoid division by zero
    
    # Step 6: Obtain Otsu threshold
    k_star = np.argmax(sB2)
    
    # Step 7: Compute separability measure
    h_star = sB2[k_star] / (np.var(image) + 1e-6)
    
    return k_star, h_star

# Example usage
image = cv2.imread("ti1.png", cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Compute Otsu's threshold
    k_star, h_star = otsu_threshold(image)
    print(f"Otsu's threshold: {k_star}")
    print(f"Separability measure: {h_star}")

    # Apply the threshold to the image
    _, binary_image = cv2.threshold(image, k_star, 255, cv2.THRESH_BINARY)

    # Display the original and thresholded images
    cv2.imshow("Original Image", image)
    cv2.imshow("Binary Image (Otsu)", binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()