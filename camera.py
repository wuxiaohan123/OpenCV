# -*- coding: cp936 -*-
# environment:Python2.7 + OpenCV 2.4 + numpy 1.8
# platform:Windows 10 x64

import cv2.cv as cv

import time

if __name__ == '__main__':

    cv.NamedWindow("camera",1)
    capture = cv.CaptureFromCAM(0)  #�������Ҫ��cv2.videocapture������һ��

    while True:
        img = cv.QueryFrame(capture)  #�˺������ص�ָ������ָ��ͬһ���ڴ棨ÿ��ˢ�£���������ͼ����Ӧ����һ�ݳ���
        cv.ShowImage("camera",img)
        
        if cv.WaitKey(10) == 27:
            break
        
    del(capture)
    cv.DestroyWindow("camera")
