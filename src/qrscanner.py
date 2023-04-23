import qrcode
import cv2

import webbrowser

import glob
import pandas as pd


class Scanner:

    def Creat_qr_code(self, info_dic):
        myqr = qrcode.make(info_dic)
        myqr.save("myqr.png")
        return myqr

    def read_qr_code(self):
        global cap, a
        cap = cv2.VideoCapture(0)
        detect = cv2.QRCodeDetector()
        while True:
            _, img = cap.read()
            data, one, _ = detect.detectAndDecode(img)
            if data:
                a = data
                self.track_students()
                break

            cv2.imshow('qr code app', img)
            if cv2.waitKey(1) == ord('q'):
                break

        return a

    def mark_presence(self):
        y = Scanner()
        y.read_qr_code()

        if cap.isOpened():
            print("hello world")



    def track_students(self):

        num_students_entered = 0
        num_students_entered += 1


x = Scanner()
x.read_qr_code()
x.mark_presence()



