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


#take off one template 抠下模板
rect = (170,80,50,50)           #前两位为左上角坐标，后两位为图像大小
cv.SetImageROI(image, rect)     #基于给定的矩形设置图像的ROI（感兴趣区域）
template = cv.CloneImage(image) #裁下感兴趣区域作为模板
cv.ShowImage(win_name, template)#显示这个模板

cv.ResetImageROI(image)         #重置感兴趣区域

#计算尺寸
W,H=cv.GetSize(image)
w,h=cv.GetSize(template)
width=W-w+1
height=H-h+1

#创建result矩阵，存储模板与源图像每一帧相比较后的相似值
#此函数原型：IplImage* cvCreateImage( CvSize size, int depth, int channels )
result=cv.CreateImage((width,height),32,1)
                                            
#下面的操作将从矩阵中找到相似值最小的点，从而定位出模板位置
cv.MatchTemplate(image,template, result,cv.CV_TM_SQDIFF)

(min_x,max_y,minloc,maxloc)=cv.MinMaxLoc(result)
(x,y)=minloc
cv.Rectangle(image,(int(x),int(y)),(int(x)+w,int(y)+h),(255,255,255),1,0) #向image上叠加画矩形
cv.ShowImage(win2_name, image)

cv.WaitKey()
