import os
import cv2
import numpy as np

def _colorMap_blur_JET_(image):
    # image = cv2.imread("figure/temp.jpg", cv2.IMREAD_GRAYSCALE)  # imput origin image data
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    zoomScale = 0.8
    # res_image = None
    res_image = cv2.resize(image, dsize=None, fx=zoomScale, fy=zoomScale, interpolation=cv2.INTER_LINEAR)  # resize image

    blur_image = cv2.GaussianBlur(res_image, (13, 13), cv2.BORDER_DEFAULT)  # blur image
    blur_image = cv2.resize(blur_image, dsize=(image.shape[::-1]))  # resize to origin image size

    hotmap = None
    hotmap = cv2.normalize(image, hotmap, 0, 255, cv2.NORM_MINMAX)
    hotmap = cv2.applyColorMap(hotmap, cv2.COLORMAP_JET)
    blur_hotmap = cv2.normalize(blur_image, hotmap, 0, 255, cv2.NORM_MINMAX)
    blur_hotmap = cv2.applyColorMap(blur_hotmap, cv2.COLORMAP_JET)

    merge_image = None
    merge_image = cv2.addWeighted(src1=hotmap, alpha=0.25, src2=blur_hotmap, beta=0.75, gamma=0.0,
                                  dst=merge_image)  # merge

    return blur_hotmap # 改成blur_hotmap不merge，merge_image

    # directory = r'D:\desk\HEATMAP\output'  # path to save
    # os.chdir(directory)
    # cv2.imwrite('merge_image.jpg', merge_image)

    # cv2.imshow("merge_image", merge_image)
    # cv2.waitKey(0)

def _makeVideo_():
    videoPath = "video/0524.avi"
    savePath = "output/0524.avi"
    cap = cv2.VideoCapture(videoPath)
    # cap.set(cv2.CAP_PROP_MODE, 2)
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'xvid') #mp4 = mp4v  avi = xvid
    videoWriter = cv2.VideoWriter(savePath, fourcc, fps, (int(w),int(h)))
    if cap.isOpened():
        while True:
            ret, frame = cap.read()
            if not ret:break
            frame_processed = _colorMap_blur_JET_(frame)
            videoWriter.write(frame_processed)
    else:
        print("Video failed to open.")
    videoWriter.release()


_makeVideo_()