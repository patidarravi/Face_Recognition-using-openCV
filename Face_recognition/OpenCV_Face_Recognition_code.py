"""
Created on sunday December 23 15:32:22 2018
@author: Ravi
Project on Face Recognition :Recognition the faces in the image
"""


import cv2                                                    #importing the package cv2


img=cv2.imread("F:\OpenCV\image\\group.jpg",1)                             #reading the image from directory and 1 is for colorfull image and 0 is grayscale image or black and white image

print(img.shape)                                                           #display the shape of image

resize_img =cv2.resize(img,(int(img.shape[0]/6),int(img.shape[1]/3)))         #resize the shape of image
#cv2.imshow("ravi",resize)                                                # its for diaplay the image
gray_img=cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY)                          #reading the image as gray scale image

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")              #create a cascadeClassifier object and "haarcascade_frontalface_default.xml" is a
                                                                                      # classifier which is used to delete the image from source

faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)          # it is used here to reduce the size of image
print(type(faces))                                      #display the type faces
for x,y,w,h in faces:                                                                  #loop for excuting the x,y,w,h co-ordinate in faces nparray
    cv2.rectangle(resize_img,(x,y),(x+w,y+h),(0,255,0),3)            #it drawn the rectangular box of green color on face of image here (x,y) are starting co-orinate and (x+w,y+h) are ending.

cv2.imshow("ravi",resize_img)                                      #used to display the image
cv2.waitKey(0)                                                #press any key to end
cv2.destroyAllWindows()                                      #it closes all windows