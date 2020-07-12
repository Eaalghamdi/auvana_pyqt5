# the idea is to use face cascade from openCV to find and draw countors
#  and count them. https://www.youtube.com/watch?v=-ZrDjwXZGxI

import cv2
import numpy as np 


def findFaces(img, show):
    show == False
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    img = cv2.imread(img)
    # convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor =1.05,minNeighbors=5)

    for x,y, w,h in faces:
        img= cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    resised = cv2.resize(img, (int(img.shape[1]), (int(img.shape[0]))))
    numberFaces =len(faces)
    if show == True:
        cv2.imshow("test", resised)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
   
    return numberFaces

g= findFaces("faces.jpeg", False)
print(g)



