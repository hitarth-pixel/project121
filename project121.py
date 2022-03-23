import numpy as np
import cv2
import time 

fcc=cv2.VideoWriter_fourcc(*'XVID')
o_file=cv2.VideoWriter('output_file.avi',fcc,20.0,(640,480))
cap=cv2.VideoCapture(0)

bg=0
time.sleep(2)

for i in range(60):
    ret,bg=cap.read()
bg=np.flip(bg,axis=1)

while(cap.isOpened()):
    ret,img=cap.read()
    if not ret : break
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    ub=np.array([104,153,70])
    lb=np.array([30,30,0])
    maskes=cv2.inRange(hsv,lb,ub)
    mask_1=cv2.morphologyEx(maskes,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask_2=cv2.morphologyEx(maskes,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mak=mask_1+mask_2
    res=cv2.bitwise_and(bg,bg,mask=mak)
    f=bg-res
    f=np.where(f==0,img,f)


cap.release()
cv2.destroyAllWindows()