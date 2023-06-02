import os
import cv2

image = cv2.imread("figure/1.jpg",cv2.IMREAD_GRAYSCALE) # imput origin image data

res_image = None
res_image = cv2.resize(image, dsize=None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR) # resize image

blur_image = cv2.GaussianBlur(res_image, (13, 13), cv2.BORDER_DEFAULT)  # blur image
blur_image = cv2.resize(blur_image, dsize=(image.shape[::-1]))  # resize to origin image size

hotmap = None
hotmap = cv2.normalize(blur_image, hotmap, 0, 255, cv2.NORM_MINMAX)
hotmap = cv2.applyColorMap(hotmap, cv2.COLORMAP_JET)
cv2.imshow("hotmap", hotmap)

directory = r'H:/lhl/HeatMap/output' # path to save
os.chdir(directory)
cv2.imwrite('1.jpg', hotmap)

cv2.waitKey(0)