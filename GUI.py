# -*- coding: utf-8 -*-
"""
Created on Thu Mar 3 09:11:17 2023

@author: rosha
"""
from tkinter import *
from tkinter import messagebox
import cv2
global window
import pyttsx3
import time
import imutils
window=Tk()
window.title("Pedestrian and Vehicle detection")
window.geometry("2000x2000") 
window.configure(bg="blue")
def fun():
    pyttsx3.speak("Welcome to the pedestrian and vehicle detection!!")
    time.sleep(3)
    pyttsx3.speak("Please allow me to detect moving vehicles and pedestrians")
def fun1():
    #pedestiran detection
    #path of the video
    video="Pedestrians.mp4"
    #create open cv video and classifier model
    Ped_video=cv2.VideoCapture(video)
    print(Ped_video)
    #now loading HOG model from Opencv
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    #classifier_ped=cv2.CascadeClassifier("pedestrian.xml")
    #Now in order to read the frame one by one in video file we run a while loop
    pyttsx3.speak("Detecting pedestrian")
    while True:
        (read_succesful, frame)=Ped_video.read()
        if read_succesful:
            frame = imutils.resize(frame, width=min(800, frame.shape[1]))
            bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8),scale=1.03)
        else:
            break
        #ped_tracker=classifier_ped.detectMultiScale(gray)
        for (x,y,w,h) in bounding_box_cordinates:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.putText(frame,'person', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        #To display the image
        cv2.imshow("video",frame)
        #autocloses the image after every split mili-second just in one frame in order to avoid that we make use of waitKey, which waits for the key for few seconds and then close
        #press button x in keyboard to stop
        if cv2.waitKey(1) & 0xFF==ord('x'):
            cv2.destroyAllWindows()
            break
    Ped_video.release()
def fun2():
    #Vehicle detection
    #path of the video
    #video="Highway.mp4"
    video="Tesla FSD Autopilot Dashcam Compilation.mp4"
    #create open cv video and classifier model
    car_video=cv2.VideoCapture(video)
    print(car_video)
    #now loading cars.xml file
    car="car.xml"
    classifier_car=cv2.CascadeClassifier(car)
    #Now in order to read the frame one by one in video file we run a while loop
    pyttsx3.speak("Detecting Vehicles")
    while True:
        (read_succesful, frame)=car_video.read()
        if read_succesful:
            #Converting the color image into GRAYSCALE
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        else:
            break
        car_tracker=classifier_car.detectMultiScale(gray)
        
        for (x,y,w,h) in car_tracker:
            cv2.rectangle(frame,(x+1,y+2),(x+w,y+h),(255,0,0),2)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame,'Vehicle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)    
        #To display the image
        cv2.imshow("video",frame)
        #autocloses the image after every split mili-second just in one frame in order to avoid that we make use of waitKey, which waits for the key for few seconds and then close
        #press button x in keyboard to stop
        if cv2.waitKey(1) & 0xFF==ord('x'):
            cv2.destroyAllWindows()
            break

    car_video.release()
def fun3():
    #closing the window
    global window
    pyttsx3.speak("Thank you and Have a nice day")
    window.destroy()
    
alab1=Label(window,text="Welcome to the Pedestrian and Vehicle detection!!",font=("Relish Pro",50),bg="blue",fg="cyan")
alab1.pack()
alab2=Label(window,text="Be cautious of, ",font=("Relish Pro",40),bg="blue",fg="violet")
alab3=Label(window,text="When you cross your limits!! ",font=("Relish Pro",40),bg="blue",fg="violet")
alab4=Label(window,text="For there is no, Pedestrians",font=("Relish Pro",40),bg="blue",fg="violet")
alab2.place(x=200,y=300)
alab3.place(x=200,y=360)
alab4.place(x=200,y=420)
btn1=Button(window,text="Pedestrian detection",font=("Relish Pro",20),bg="white",fg="blue",width=25,command=fun1)
btn1.place(x=100,y=680)
btn2=Button(window,text="Vehicle detection",font=("Relish Pro",20),bg="white",fg="blue",width=25,command=fun2)
btn2.place(x=600,y=680)
btn3=Button(window,text="Exit",font=("Relish Pro",20),bg="Yellow",fg="Red",width=10,command=fun3)
btn3.place(x=1300,y=680)
fun()
window.mainloop()