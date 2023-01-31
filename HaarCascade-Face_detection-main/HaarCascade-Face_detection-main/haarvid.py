import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#loading the visual data
vid=cv2.VideoCapture('testvid.MP4')


#Cascading frame by frame

while vid.isOpened():
    _,img=vid.read()
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grayimg,1.1,4)


    #Cascading with Rectangle
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,1000),3)


    #Display
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

vid.release()
    #Thankful for the knowledge
    #grateful for the knowledge