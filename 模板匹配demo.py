# -*- coding: cp936 -*-
import cv2.cv as cv

#load image
filename = "../Video/cat.jpg"
image = cv.LoadImage(filename)


#create one window
win_name = "test"
cv.NamedWindow(win_name)
win2_name = "test2"
cv.NamedWindow(win2_name)


#take off one template ����ģ��
rect = (170,80,50,50)           #ǰ��λΪ���Ͻ����꣬����λΪͼ���С
cv.SetImageROI(image, rect)     #���ڸ����ľ�������ͼ���ROI������Ȥ����
template = cv.CloneImage(image) #���¸���Ȥ������Ϊģ��
cv.ShowImage(win_name, template)#��ʾ���ģ��

cv.ResetImageROI(image)         #���ø���Ȥ����

#����ߴ�
W,H=cv.GetSize(image)
w,h=cv.GetSize(template)
width=W-w+1
height=H-h+1

#����result���󣬴洢ģ����Դͼ��ÿһ֡��ȽϺ������ֵ
#�˺���ԭ�ͣ�IplImage* cvCreateImage( CvSize size, int depth, int channels )
result=cv.CreateImage((width,height),32,1)
                                            
#����Ĳ������Ӿ������ҵ�����ֵ��С�ĵ㣬�Ӷ���λ��ģ��λ��
cv.MatchTemplate(image,template, result,cv.CV_TM_SQDIFF)

(min_x,max_y,minloc,maxloc)=cv.MinMaxLoc(result)
(x,y)=minloc
cv.Rectangle(image,(int(x),int(y)),(int(x)+w,int(y)+h),(255,255,255),1,0) #��image�ϵ��ӻ�����
cv.ShowImage(win2_name, image)

cv.WaitKey()
