import os
import cv2

image = cv2.imread("figure/2-1.jpg",cv2.IMREAD_GRAYSCALE) # imput origin image data

zoomScale = 0.8
res_image = None
res_image = cv2.resize(image, dsize=None, fx=zoomScale, fy=zoomScale, interpolation=cv2.INTER_LINEAR) # resize image

blur_image = cv2.GaussianBlur(res_image,(13,13),cv2.BORDER_DEFAULT) # blur image
blur_image = cv2.resize(blur_image, dsize=(image.shape)) # resize to origin image size

hotmap = None
hotmap = cv2.normalize(image, hotmap, 0, 255, cv2.NORM_MINMAX)
hotmap = cv2.applyColorMap(hotmap, cv2.COLORMAP_JET)
blur_hotmap = cv2.normalize(blur_image, hotmap, 0, 255, cv2.NORM_MINMAX)
blur_hotmap = cv2.applyColorMap(blur_hotmap, cv2.COLORMAP_JET)

merge_image = None
merge_image = cv2.addWeighted(src1 = hotmap, alpha = 0.25, src2 = blur_hotmap, beta = 0.75, gamma = 0.0, dst = merge_image) # merge
cv2.imshow("merge_image", merge_image)

directory = r'D:/desk/HeatMap/output' # path to save
os.chdir(directory)
cv2.imwrite('merge_image.jpg', merge_image)

cv2.waitKey(0)