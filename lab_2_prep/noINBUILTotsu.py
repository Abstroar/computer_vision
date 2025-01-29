import numpy as np
import cv2

def compute_histogram(image):
    hist = np.zeros(256)
    for pixel in image.ravel():
        hist[pixel] += 1
    return hist / hist.sum()

def compute_cumulative_sums(hist):
    P1 = np.zeros(256)
    P1[0] = hist[0]
    for i in range(1, 256):
        P1[i] = P1[i - 1] + hist[i]
    return P1

def compute_cumulative_means(hist):
    m = np.zeros(256)
    m[0] = 0 * hist[0]
    for i in range(1, 256):
        m[i] = m[i - 1] + i * hist[i]
    return m

def otsu_threshold(image):
    hist = compute_histogram(image)
    P1 = compute_cumulative_sums(hist)
    m = compute_cumulative_means(hist)
    mG = m[-1]
    
    sB2 = np.zeros(256)
    for k in range(256):
        if P1[k] == 0 or P1[k] == 1:
            sB2[k] = 0
        else:
            sB2[k] = ((mG * P1[k] - m[k]) ** 2) / (P1[k] * (1 - P1[k]))
    
    k_star = np.argmax(sB2)
    h_star = sB2[k_star] / (np.var(image) + 1e-6)
    
    return k_star, h_star

# Example usage
image = cv2.imread("ti1.png", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Could not load image.")
else:
    k_star, h_star = otsu_threshold(image)
    print(f"Otsu's threshold: {k_star}")
    print(f"Separability measure: {h_star}")

    binary_image = np.where(image > k_star, 255, 0).astype(np.uint8)
    
    cv2.imshow("Original Image", image)
    cv2.imshow("Otsu Binary", binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
