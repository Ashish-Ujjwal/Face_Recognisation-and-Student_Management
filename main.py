from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Student import Student
from train import train
from face_recog import Face_Recoginition
from Attendence import attendance
import os
import tkinter
from time import strftime
from datetime import datetime


class Attendence_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation System")

        img1 = Image.open("./college_images/unnamed.jpg")
        img1 = img1.resize((520, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=520, height=130)

        img2 = Image.open("./college_images/facialrecognition.png")
        img2 = img2.resize((520, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=520, y=0, width=520, height=130)

        img3 = Image.open("./college_images/School.jpg")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1040, y=0, width=500, height=130)

        # bg image --->
        img4 = Image.open("./college_images/AIMT1.png")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        BG_img = Label(self.root, image=self.photoimg4)
        BG_img.place(x=0, y=130, width=1530, height=710)

        # Title 1------->
        title_lbl = Label(BG_img, text="FACE RECOGNISATION ATTENDENCE SYSTEM SOFTWARE", font=(
            "times new roman", 30, "bold"), bg="black", fg="white")
        title_lbl.place(x=0,y=-2,width=1530,height=55)

        # Title 2------->
        title_lbl = Label(BG_img, text="Ambalika Institute OF Management And Technology", font=(
            "times new roman", 25, "bold"), bg="pink", fg="green")
        title_lbl.place(x=0,y=45,width=1530,height=45)

        ###########
        # Button Students---->
        img5 = Image.open("./college_images/56-565073_student-malefemale-student-portal-logo-png-transparent-png.png")
        img5 = img5.resize((180, 180), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(BG_img, cursor="hand2",command=self.student_details, image=self.photoimg5)
        b1.place(x=200, y=100, width=180, height=180)

        b1_1 = Button(BG_img, text="Student Details",command=self.student_details, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="black", fg="pink")
        b1_1.place(x=200, y=280, width=180, height=40)

        # Detect_face Button ------->
        img6 = Image.open("./college_images/face_detector1.jpg")
        img6 = img6.resize((180, 180), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(BG_img, cursor="hand2",command=self.face_data, image=self.photoimg6)
        b1.place(x=500, y=100, width=180, height=180)
        b1_1 = Button(BG_img, text="Face Detector",command=self.face_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="black", fg="pink")
        b1_1.place(x=500, y=280, width=180, height=40)

        # Attendence face System ------->
        img7 = Image.open("./college_images/smart-attendance.jpg")
        img7 = img7.resize((180, 180), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(BG_img,cursor="hand2",command=self.attendance_data, image=self.photoimg7)
        b1.place(x=800, y=100, width=180, height=180)
        b1_1 = Button(BG_img, text="Attendence",command=self.attendance_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="black", fg="pink")
        b1_1.place(x=800, y=280, width=180, height=40) 
        
        # Help Desk System ------->
        img8 = Image.open("./college_images/help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img8 = img8.resize((180, 180), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(BG_img,cursor="hand2", image=self.photoimg8)
        b1.place(x=1100, y=100, width=180, height=180)
        b1_1 = Button(BG_img, text="Help Desk", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="black", fg="pink")
        b1_1.place(x=1100, y=280, width=180, height=40) 

        # train face System ------->
        img9 = Image.open("./college_images/Train.jpg")
        img9 = img9.resize((180, 180), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(BG_img,cursor="hand2",command=self.train_data, image=self.photoimg9)
        b1.place(x=200, y=380, width=180, height=180)
        b1_1 = Button(BG_img, text="Train Data",command=self.train_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="black", fg="pink")
        b1_1.place(x=200, y=560, width=180, height=40) 

        # Photos ------->
        img11 = Image.open("./college_images/employee_img2.jpg")
        img11 = img11.resize((180, 180), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(BG_img,cursor="hand2", image=self.photoimg11, command=self.open_img)
        b1.place(x=500, y=380, width=180, height=180)
        b1_1 = Button(BG_img, text="Photos", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="black", fg="pink")
        b1_1.place(x=500, y=560, width=180, height=40) 

        # developer System ------->
        img10 = Image.open("./college_images/dev.jpg")
        img10 = img10.resize((180, 180), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(BG_img,cursor="hand2", image=self.photoimg10)
        b1.place(x=800, y=380, width=180, height=180)
        b1_1 = Button(BG_img, text="Developer", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="black", fg="pink")
        b1_1.place(x=800, y=560, width=180, height=40) 


        # Exit ------->
        img12 = Image.open("./college_images/exit.jpg")
        img12 = img12.resize((180, 180), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(BG_img,cursor="hand2", image=self.photoimg12, command=self.iExit)
        b1.place(x=1100, y=380, width=180, height=180)
        b1_1 = Button(BG_img, text="Exit", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="black", fg="pink")
        b1_1.place(x=1100, y=560, width=180, height=40) 



################# Functions Buttons #################

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recoginition(self.new_window)

    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)
    
    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition ","Are you sure want to exit this Project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    # def Login_Clock1(self):
    #     self.root.destroy()
    #     import Login_GUI
    
    # def help_data(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=help1(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Attendence_System(root)
    root.mainloop()
