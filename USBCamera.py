
import cv2
import numpy as np




cap=cv2.VideoCapture(0)  # 30 sec to open camera
while True:
    ret, frame = cap.read() # if feed exist capture it else return false
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()