# a basic version of face recognition using cv2

import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
frame=cv2.VideoCapture(0)

while True:
    _,img=frame.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img , (x,y) , (x+w , y+w),(255,255,0) , 2 )
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
frame.release()
cv2.destroyAllWindows()
