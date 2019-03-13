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

from sendValue import * 

# def callRest():
#     headers={'Content-Type': 'application/json'}
#     url = 'http://10.255.30.239:5000/select/report'
#     response = requests.get(url,headers=headers)
#     result = json.dumps(response.json(), indent=2, ensure_ascii=False)
#     value = json.loads(result)

#     if result != None:
#         print (result)
# callRest()
global cap
global name
global lastname
global address
global filename

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

hc = cv2.CascadeClassifier("C:\\Python\\opencv\\build\\etc\\haarcascades\\plate1.xml")
path = "C:\\Users\\Nattawadee\\Desktop\\web_security\\image"

def show_vid():  # creating a function
    if not cap.isOpened():  # checks for the opening of camera
        print("cant open the camera")
    flag, frame = cap.read()
    frame = cv2.resize(frame, (500, 400))
            # we can change the display color of the frame gray,black&white here
    pic1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = hc.detectMultiScale(pic1, 1.3, 2)

    filename = ""
    for (x, y, w, h) in cars:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        save = frame[y:y+h, x:x+w]
        filename = 'img'+str(x)+'.jpg'
        cv2.imwrite(os.path.join(path, filename), save)
        if(filename == 'img'+str(x)+'.jpg' ) :
            break
    if(filename != ''):
        print(filename)
    else :
        print("End")

    pic = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img1 = Image.fromarray(pic)
    imgtk = ImageTk.PhotoImage(image=img1)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_vid)

def switchoff():
    time.sleep(2)
switchoff()   

# def sendImage(image):
#     i = 0
#     v = '0'
#     c = 'th'
#     sk = "sk_9d34b992ad93485f2b2c8e0b"

#     # image = request.json['files']
#     # imgdata = base64.b64decode(image)
#     # localtime = time.asctime(time.localtime(time.time()))

#     # filename = 'C:\\Users\\Nattawadee\\Desktop\\Image_recognition\\image\\plate.jpeg'
#     path = 'C:\\Users\\Nattawadee\\Desktop\\web_security\\image\\'
#     images = path + image    
#     filename = images
#     print(filename)

#     url = 'https://api.openalpr.com/v2/recognize?recognize_vehicle=%s&country=%s&secret_key=%s' % (v, c, sk)
#     r = requests.post(url, files={'image': open(filename, 'rb')})
#     result = json.dumps(r.json(), indent=2, ensure_ascii=False)
#     value = json.loads(result)
# #     print(value)
#     i += 1
#     if result != None:
#         # print(result)
#         return jsonify(result=value)

#     # print(image)
#     # path = 'C:\\Users\\Nattawadee\\Desktop\\web_security\\image\\'
#     # files = {'files ': path + image}
#     # print(files)
#     # files = {'files': path}

#     # headers={'Content-Type': 'application/json'}
#     # url = 'http://192.168.1.40:5000/image/callapi'
#     # # url = 'http://10.255.44.63:5000/image/callapi'
#     # response = requests.post(url,json=files,headers=headers)
#     # # print (response)
#     # result = json.dumps(response.json(), indent=2, ensure_ascii=False)
#     # value = json.loads(result)
#     # data = value['result']
#     # datalist = data['results']

#     # for v_lists in datalist:
#     #     platename = v_lists['plate']
#     #     # print(v_lists['plate'])
#     # # return platename
        
#     # if result != None:
#     #     print ("result")

#     sendImage(image)


# def callRest():
    # platename = sendImage()
    # print("11111111: "+platename)
    # platename = platename
    # headers={'Content-Type': 'application/json'}
    # url = 'http://192.168.1.40:5000/check/license'
    # platename = {'platename':platename}
    # response = requests.post(url,json=platename ,headers=headers)
    # _result = json.dumps(response.json(), indent=2, ensure_ascii=False)
    # value = json.loads(_result)
    # print(value)
    # data = value['licenses']
    # # _list = data['results']
    # for dataValue in data:
    #     name = dataValue['username']
    #     lastname = dataValue['lastname']
    #     address = dataValue['address']
    #     if data != '' :
    #         print(name)
    #         print(lastname)
    #         print(address)
    #     else :
    #         print("Not found")
    # # return;
    # if _result != None:
    #     print ("result")
# callRest()

if __name__ == '__main__':
    root = tk.Tk()  # assigning root variable        for Tkinter as tk
    lmain = tk.Label(master=root)
    lmain.grid(row=0, column=1, columnspan=2, rowspan=4,
               padx=8, pady=15, sticky=E+W+S+N)

    root.title("License Plate")  # you can give any title
    root.geometry("900x500+100+10")  # size of window , x-axis, yaxis

    # plate = StringVar() 
    # plate.set(name)

    # lastname = StringVar() 
    # lastname.set(lastname)

    # address = StringVar() 
    # address.set(address)

    lfl = LabelFrame(root, text="Group", labelanchor="n", padx=5, pady=5)
    lfl.grid(row=0, column=3, sticky='E', padx=20, pady=50)

    # lbl = Label(lfl, text='license', font=5, fg="black").grid(row=1, column=3)
    # text = Entry(lfl, width=28, textvariable = plate ).grid(row=1, column=4, padx=5, pady=6)

    # lbl1 = Label(lfl, text='Name', font=5, fg="black").grid(row=2, column=3)
    # text1 = Entry(lfl, width=28, textvariable = name ).grid(row=2, column=4, padx=10, pady=10)

    # lbl1 = Label(lfl, text='Address', font=5, fg="black").grid(row=3, column=3)
    # text1 = Entry(lfl, width=28, textvariable = address ).grid(row=3, column=4, padx=10, pady=10)

    show_vid()
    # sendImage() 
    # callRest()
    root.mainloop()  # keeps the application in an infinite loop so it works continuosly
    cap.release()
    cv2.destroyWindow("Detect")
