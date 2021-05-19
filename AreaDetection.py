import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",131,255,empty)
cv2.createTrackbar("Threshold2","Parameters",73,255,empty)
def stackImages(scale,imgArray):

    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

#def getContours(img,imgContour):
   
   # contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
   # cv2.drawContours(imgContour, contours, -1, (255, 0, 255), 7)

while True:
    success, img = cap.read()
    imgContour = img.copy()
    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
  #  imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  #  imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
    
    threshold1=cv2.getTrackbarPos("Threshold1","Parameters")
    threshold2=cv2.getTrackbarPos("Threshold2","Parameters")
    
    
    imgCanny = cv2.Canny(imgGray,threshold1,threshold2)
   
 
    imgBlank = np.zeros_like(img)
    kernel = np.ones((5,5))
    imgDil=cv2.dilate(imgCanny, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(imgGray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContour, contours, -1, (255, 0, 255), 7)


    #getContours(imgDil,imgContour)
    imgStack = stackImages(0.8,([img,imgGray,imgBlur],
                            [imgCanny,imgDil,imgDil]))

    cv2.imshow("Result", imgStack)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break