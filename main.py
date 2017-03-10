# environment:Python2.7 + OpenCV 2.4 + numpy 1.8
# platform:Windows 10 x64

import cv2.cv as cv

if __name__ == '__main__':

    #load template
    filename = 'D:\\xunxian0.jpg'
    template = cv.LoadImage(filename)
    cv.ShowImage(filename, template)#显示这个模板

    #create window
    cv.NamedWindow(filename)
    cv.NamedWindow("camera",1)

    capture = cv.CaptureFromCAM(0)  #这个方法要比cv2.videocapture更靠谱一点
    image = cv.QueryFrame(capture)
    
    #计算尺寸
    #W,H=cv.GetSize(image)
    W,H=640,480     #wxh的电脑摄像头

    w,h=cv.GetSize(template)
    width=W-w+1
    height=H-h+1

    while True:
        image = cv.QueryFrame(capture)  #此函数返回的指针总是指向同一块内存（每次刷新），若处理图像则应复制一份出来

        #创建result矩阵，存储模板与源图像每一帧相比较后的相似值
        #此函数原型：IplImage* cvCreateImage( CvSize size, int depth, int channels )
        result=cv.CreateImage((width,height),32,1)
                                            
        #从矩阵中找到相似值最小的点，从而定位出模板位置
        cv.MatchTemplate(image,template, result,cv.CV_TM_SQDIFF)

        (min_x,max_y,minloc,maxloc)=cv.MinMaxLoc(result)
        (x,y)=minloc
        cv.Rectangle(image,(int(x),int(y)),(int(x)+w,int(y)+h),(0,0,255),1,0) #向image上叠加画矩形
        cv.ShowImage('camera', image)

        cv.WaitKey(50)
        
    del(capture)
    cv.DestroyWindow("camera")

