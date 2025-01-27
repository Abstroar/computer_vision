import cv2
import numpy as np

image = cv2.imread("proxy-image.jpeg", cv2.IMREAD_GRAYSCALE)

size_x,size_y = image.shape

segmented_img = np.zeros((size_x, size_y), dtype=np.uint8)

# def inital_t(img):
#
#     size_x, size_y = img.shape
#     size = size_x*size_y
#     total = 0
#
#     for i in range(size_x):
#         for j in range(size_y):
#             total += img[i][j]
#     return int(total/size)



# initial_T = inital_t(image)
# print("ini",initial_T)
initial_T = 240
delta_T = 1
new_T = initial_T
iteration = 0
while True:
    G1 = []
    G2 = []

    for i in range(size_x):
        for j in range(size_y):

            if image[i][j] > new_T:
                segmented_img[i][j] = 255
                G1.append(image[i][j])
            else:
                segmented_img[i][j] = 0
                G2.append(image[i][j])

    m1 = np.mean(G1)
    m2 = np.mean(G2)

    print("avg_intensity_G1:", m1)
    print("avg_intensity_G2", m2)

    new_T = (m1 + m2) / 2
    print("new threshold value: ", new_T)
    iteration += 1
    if abs(new_T - initial_T) == 0:
        break
    initial_T = new_T

print("final threshold value", new_T , "number of interation", iteration)
cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented_img)
cv2.waitKey(0)
cv2.destroyAllWindows()