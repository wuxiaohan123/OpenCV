# environment:Python2.7 + OpenCV 2.4 + numpy 1.8
# platform:Windows 10 x64

import cv2.cv as cv

if __name__ == '__main__':

    #load template
    left = 'D:\\left.jpg'
    right = 'D:\\right.jpg'
    template_L = cv.LoadImage(left)
    template_R = cv.LoadImage(right)

    #cv.ShowImage(filename, template)#显示这个模板

    #create window
    cv.NamedWindow("camera",1)

    capture = cv.CaptureFromCAM(0)  #这个方法要比cv2.videocapture更靠谱一点
    image = cv.QueryFrame(capture)
    
    #计算尺寸
    #W,H=cv.GetSize(image)
    W,H=640,480     #wxh的电脑摄像头

    w,h=cv.GetSize(template_L)
    width=W-w+1
    height=H-h+1

    while True:
        image = cv.QueryFrame(capture)  #此函数返回的指针总是指向同一块内存（每次刷新），若处理图像则应复制一份出来

        #创建result矩阵，存储模板与源图像每一帧相比较后的相似值
        #此函数原型：IplImage* cvCreateImage( CvSize size, int depth, int channels )
        result_L=cv.CreateImage((width,height),32,1)
        result_R=cv.CreateImage((width,height),32,1)                   

        #从矩阵中找到相似值最小的点，从而定位出模板位置
        cv.MatchTemplate(image,template_L, result_L,cv.CV_TM_SQDIFF)
        cv.MatchTemplate(image,template_R, result_R,cv.CV_TM_SQDIFF)

        (min_x,max_y,minloc_L,maxloc_L)=cv.MinMaxLoc(result_L)
        (min_x,max_y,minloc_R,maxloc_R)=cv.MinMaxLoc(result_R)
        (x_L,y_L)=minloc_L
        (x_R,y_R)=minloc_R

        cv.Rectangle(image,(int(x_L),int(y_L)),(int(x_L)+w,int(y_L)+h),(0,0,255),1,0) #向image上叠加画矩形
        cv.Rectangle(image,(int(x_R),int(y_R)),(int(x_R)+w,int(y_R)+h),(255,0,0),1,0) #向image上叠加画矩形
        
        cv.ShowImage('camera', image)

        cv.WaitKey(10)
        
    del(capture)
    cv.DestroyWindow("camera")

