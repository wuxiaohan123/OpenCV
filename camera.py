# -*- coding: cp936 -*-
# environment:Python2.7 + OpenCV 2.4 + numpy 1.8
# platform:Windows 10 x64

import cv2.cv as cv

import time

if __name__ == '__main__':

    cv.NamedWindow("camera",1)
    capture = cv.CaptureFromCAM(0)  #这个方法要比cv2.videocapture更靠谱一点

    while True:
        img = cv.QueryFrame(capture)  #此函数返回的指针总是指向同一块内存（每次刷新），若处理图像则应复制一份出来
        cv.ShowImage("camera",img)
        
        if cv.WaitKey(10) == 27:
            break
        
    del(capture)
    cv.DestroyWindow("camera")
