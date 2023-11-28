from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import csv
from time import strftime
from datetime import datetime


class Face_Recoginition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Face Recoginition", font=(
            "times new roman", 30, "bold"), bd=2, bg="#8379FA", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=55)

        # _______________First Image

        img1 = Image.open(r"./college_images/BestFacialRecognition.jpg")
        img1 = img1.resize((650, 730), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=0, y=55, width=650, height=730)

        # ==============2nd Image

        img2 = Image.open(r"./college_images/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img2 = img2.resize((950, 730), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb2 = Label(self.root, image=self.photoimg2)
        f_lb2.place(x=650, y=55, width=950, height=730)

        # -------------------Button
        b1_1 = Button(f_lb2, text="Face Recognition", width=7, command=self.face_recog, font=(
            "times new roman", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=375, y=645, width=200, height=40)

        b1_2 = Button(self.root, text="Main Menu", width=7, command=self.main_menu, font=(
            "times new roman", 15, "bold"), bg="red", fg="white")
        b1_2.place(x=1040, y=5, width=200, height=40)

    def main_menu(self):
        self.root.destroy()
        # import Main_GUI

        # --------------Attendance===============

    def mark_attendance(self, e, r, n, d):
        with open("Atten.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((e not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)) :
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{e},{r},{n},{d},{dtString},{d1},Present")

    # _________________________face Recognition

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="@Ashish12345", database="face_recognisation")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select email from student where student_id="+str(id))
                e = my_cursor.fetchone()
                e = "+".join(e)

                my_cursor.execute(
                    "select roll from student where student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute(
                    "select name from student where student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute(
                    "select dep from student where student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 77:
                    cv2.putText(
                        img, f"Email:{e}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                    cv2.putText(
                        img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                    cv2.putText(
                        img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                    self.mark_attendance(e, r, n, d)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1,10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recoginition ", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recoginition(root)
    root.mainloop()
