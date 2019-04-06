import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import numpy as np
import requests
import json
import base64
import time
from multiprocessing import Process, Queue
from send import * 
from tkinter import StringVar

global cap

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    
hc = cv2.CascadeClassifier("C:\\Python\\opencv\\build\\etc\\haarcascades\\plate1.xml")
path = "C:\\Users\\Nattawadee\\Desktop\\web_security\\image"
port = '192.168.1.40:5000'
# port = '10.255.3.20:5000'

def show_vid():  # creating a function
    if not cap.isOpened():  # checks for the opening of camera
        print("cant open the camera")
    flag, frame = cap.read()
    frame = cv2.resize(frame, (500, 400))
    pic1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = hc.detectMultiScale(pic1, 1.3, 2)

    images = []
    for i,(x, y, w, h) in enumerate(cars):
        images.append(cv2.rectangle(frame,(x, y), (x+w, y+h), (255, 0, 0), 2))

    for (x, y, w, h) in cars:
        save = frame[y:y+h, x:x+w]
        filename = 'img'+str(x)+'.jpg'
        cv2.imwrite(os.path.join(path, filename), save)
        sendImage(filename)
        break

    pic = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img1 = Image.fromarray(pic)
    imgtk = ImageTk.PhotoImage(image=img1)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_vid)  

def sendImage(images):
    a = 'C:\\Users\\Nattawadee\\Desktop\\web_security\\image\\'
    b = images
    filename = a + b
    
    api(filename)

def api(filename):
    v = '0'
    c = 'th'
    sk = "sk_9d34b992ad93485f2b2c8e0b"
    
    url = 'https://api.openalpr.com/v2/recognize?recognize_vehicle=%s&country=%s&secret_key=%s' % (v, c, sk)
    r = requests.post(url, files={'image': open(filename, 'rb')})
    result = json.dumps(r.json(), indent=2, ensure_ascii=False)
    value = json.loads(result)
#     data = value['result']
    datalist = value['results']
    # vdata = datalist['candidates']
    for v_lists in datalist:
        platename = v_lists['plate']
        print("11111111"+platename)
        if not platename :
            print("กรุณาสแกนใหม่") 
        else :
            callRest(platename)  
        break

def callRest(platename):

    headers={'Content-Type': 'application/json'}
    url = 'http://'+port+'/check/license'
    # url = 'http://10.255.23.144:5000/check/license'
    platename = { 'platename' : platename }
    response = requests.post(url,json=platename ,headers=headers)
    _result = json.dumps(response.json(), indent=2, ensure_ascii=False)
    value = json.loads(_result)
    print(value)
    data = value['licenses']
    print(data)
    # # _list = data['results']
    if not data:
        name = '-'
        lastname = '-'
        address = '-'
        amount = '-'
        plate = '-'
        passing = 'ไม่ผ่าน'
        receiver = '-'
        varliableData(name,address,amount,plate,passing,receiver)
    else: 
        for dataValue in data:
            name = dataValue['username']
            lastname = dataValue['lastname']
            address = dataValue['address']
            amount = dataValue['amount']
            plate = dataValue['platename']
            receiver = dataValue['receiver']
            # print("name :"+name)
            # print("lastname :"+lastname)
            # print("address :"+address)
            # print("postoffice :"+postoffice)
            # print("plate :"+plate)
            passing = 'ผ่าน'
            varliableData(name,address,amount,plate,passing,receiver)
            break

def varliableData(name,address,amount,plate,passing,receiver):

    name = name
    plate = plate
    address = address
    passing = passing
    amount = amount
    receiver = receiver
    # return name,plate,address,passing,postoffice
    r_name = StringVar() 
    r_name.set(name)

    r_plate = StringVar() 
    r_plate.set(plate)

    r_address = StringVar() 
    r_address.set(address)

    r_passing = StringVar()
    r_passing.set(passing)

    r_amount = StringVar()
    r_amount.set(amount)

    r_receiver = StringVar()
    r_receiver.set(receiver)

    lbl = Label( root,text='license', font=5, fg="black").grid(row=0, column=3, padx=30)
    text = Entry( root, width=28 ,textvariable = r_name ).grid(row=0, column=4, padx=5, pady=6)

    
    lbl1 = Label(root, text='Name', font=5, fg="black").grid(row=1, column=3)
    text1 = Entry(root, width=28 ,textvariable = r_plate  ).grid(row=1, column=4, padx=10, pady=10)


    lbl1 = Label(root, text='Address', font=5, fg="black").grid(row=2, column=3)
    text2 = Entry(root, width=28 ,textvariable = r_address ).grid(row=2, column=4, padx=10, pady=10)
     
    lbl2 = Label(root,font=50 ,textvariable = r_passing ,fg="red").grid(row=3, column=4)

    lbl3 = Label(root,font=50 ,text="พัสดุ" ,fg="red").grid(row=4, column=3 , padx=30)
    lbl4 = Label(root,font=50 ,textvariable = r_amount ,fg="red").grid(row=4, column=4)
    lbl5 = Label(root,font=50 ,text="ชิ้น" ,fg="red").grid(row=4, column=5)
    lbl6 = Label(root,font=50 ,text="ผู้รับ" ,fg="red").grid(row=5, column=3)
    lbl7 = Label(root,font=50 ,textvariable = r_receiver ,fg="red").grid(row=5, column=4)
    Update(plate,name)

def Update(plate,name):
    headers={'Content-Type': 'application/json'}
    url = 'http://'+port+'/update/name'
    # url = 'http://10.255.23.144:5000/check/license'
    platename = { 'platename' : plate, 
                  'receiver' : name }
    response = requests.post(url,json=platename, headers=headers)
    _result = json.dumps(response.json(), indent=2, ensure_ascii=False)
    value = json.loads(_result)
    print(value)

    # text.config(state = "readonly")
    # text1.config(state = "readonly")
    # text2.config(state = "readonly")

if __name__ == '__main__':
    print ('queue initialized...')

    root = tk.Tk()

    lmain = tk.Label(master=root)
    lmain.grid(row=0, column=1, columnspan=2, rowspan=4,padx=13, pady=20, sticky=E+W+S+N)

    root.title("License Plate")  # you can give any title
    root.geometry("1000x500+200+100")  # size of window , x-axis, yaxis


    show_vid()
    root.mainloop()  # keeps the application in an infinite loop so it works continuosly
    cap.release()
    cv2.destroyWindow("Detect")
