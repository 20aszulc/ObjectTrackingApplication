import cv2
import numpy as np
img1 = cv2.imread("./images/geisel.jpg") # Default condition or 1
print(img1.shape)  # (476, 640, 3)

img2 = cv2.imread("./images/geisel.jpg", 0) # Default condition
print(img2.shape)  # (476, 640)

cv2.imshow("GrayGeisel", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img3=cv2.imread("./images/geisel.jpg",1)
b, g, r = cv2.split(img3)
img4 = cv2.merge([r, g, b])
cv2.imshow("no 1 color", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()

img5 = img3.copy()
#no blue
img5[0, 0, :] = 0
img5[2, 2, :] = 0
cv2.imshow("no blue", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()

invert_blue = img3.copy()
invert_blue = cv2.bitwise_not(img3)
invert_blue[:, :, 0] = img3[:, :, 0]
cv2.imshow("invert blue", invert_blue)
cv2.waitKey(0)
cv2.destroyAllWindows()

total_invert = 255 - img3
cv2.imshow("no 1 color", total_invert)
cv2.waitKey(0)
cv2.destroyAllWindows()

sobelx = cv2.Sobel(src=img1, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge
cv2.imshow("soblex", sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()

edge_canny = cv2.Canny(img1, 100, 200) #
cv2.imshow("edge_canny", edge_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
