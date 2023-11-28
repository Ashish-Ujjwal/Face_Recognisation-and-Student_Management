# from _typeshed import WriteableBuffer
from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import csv
from time import strftime, time
from datetime import datetime
import os
import csv


from tkinter import filedialog

mydata = []
class attendance:
    def __init__(self, root):

        self.root = root
        self.root.geometry("1530x790+0+0")

        # ============Variable
        self.var_email = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

        # -----first Image

        img1 = Image.open(r"./college_images/bg.jpg")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=0, y=0, width=770, height=200)

        # 2nd Image

        img2 = Image.open(r"./college_images/dev.jpg")
        img2 = img2.resize((800, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb2 = Label(self.root, image=self.photoimg2)
        f_lb2.place(x=770, y=0, width=800, height=200)

        # ----------------BACKGROUND IMAGES............

        img4 = Image.open(
            r"./college_images/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img4 = img4.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1530, height=710)

        string = strftime(
            "%H:%M:%S %p                                             Attendance Management System")

        title_bgl = Label(bg_img, anchor="center", text=string, font=(
            "ds-digital", 30, "bold"), bd=2, bg="black", fg="cyan")
        title_bgl.place(x=0, y=-3, width=1530, height=50)
        title_bgl.after(1000, time)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=0, y=50, width=1530, height=600)

        # ------------Left Label Frame

        Left_frame = LabelFrame(main_frame, bd=4, bg="white", relief=RIDGE,
                                text="Teacher Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=20, y=5, width=730, height=500)

        img_left = Image.open(
            r"./college_images/bg1.jpg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        bg_img_left = Label(Left_frame, image=self.photoimg_left)
        bg_img_left.place(x=5, y=0, width=700, height=80)

        class_student_frame = LabelFrame(
            Left_frame, bd=2, bg="white", relief=RIDGE, font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=80, width=700, height=385)

        img10 = Image.open(r"./college_images/university.jpg")
        img10 = img10.resize((160, 140), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        bg_img10 = Label(self.root, image=self.photoimg10)
        bg_img10.place(x=480, y=470, width=170, height=155)

        # -----------MainMenu Button

        # ---------Student Email
        studentEmail_label = Label(class_student_frame, text="Email :", font=(
            "times new roman", 12, "bold"), bg="white")
        studentEmail_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentEmail_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_email, font=(
            "times new roman", 12, "bold"))
        studentEmail_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # ---------Roll No
        studentRoll_label = Label(class_student_frame, text="Roll No.:", font=(
            "times new roman", 12, "bold"), bg="white")
        studentRoll_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentRoll_entry = ttk.Entry(
            class_student_frame, width=20, textvariable=self.var_roll, font=("times new roman", 12, "bold"))
        studentRoll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # ---------Name
        studentName_label = Label(class_student_frame, text="Student Name :", font=(
            "times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_name, font=(
            "times new roman", 12, "bold"))
        studentName_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # ---------Department
        studentName_label = Label(class_student_frame, text="Department :", font=(
            "times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_frame, width=20, textvariable=self.var_dep, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # ---------Time
        studentId_label = Label(class_student_frame, text="Time :", font=(
            "times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_time, font=(
            "times new roman", 12, "bold"))
        studentId_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # ---------Date
        studentName_label = Label(class_student_frame, text="Date :", font=(
            "times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_frame, width=20, textvariable=self.var_date, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # -----------Attendance Status
        attendance_label = Label(class_student_frame, text="Attendance :", font=(
            "times new roman", 12, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        attendance_combo = ttk.Combobox(class_student_frame, font=(
            "times new roman", 12, "bold"), state="readonly", width=18, textvariable=self.var_attendance)
        attendance_combo["values"] = ("Status", "Present", "Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # ---------Profile Picture
        studentName_label = Label(class_student_frame, text="Profile Picture :", font=(
            "times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=5, column=0, padx=5, pady=5, sticky=W)

        ########### clock##############

        # -----------Buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=2, y=300, width=650, height=50)

        import_btn = Button(btn_frame, text="IMPORT CSV", width=13, command=self.importCsv, font=(
            "times new roman", 13, "bold"), bg="#8379FA", fg="black")
        import_btn.grid(row=0, column=0, padx=10, pady=5)

        export_btn = Button(btn_frame, text="EXPORT CSV", width=13, command=self.exportcsv, font=(
            "times new roman", 13, "bold"), bg="#8379FA", fg="black")
        export_btn.grid(row=0, column=1, padx=10)

        update_btn = Button(btn_frame, text="UPDATE", width=13, font=(
            "times new roman", 13, "bold"), bg="#8379FA", fg="black")
        update_btn.grid(row=0, column=2, padx=10)

        reset_btn = Button(btn_frame, text="RESET", width=13, command=self.reset_data, font=(
            "times new roman", 13, "bold"), bg="#8379FA", fg="black")
        reset_btn.grid(row=0, column=3, padx=10)

        # ------------RIGHT Label Frame

        Right_frame = LabelFrame(main_frame, bd=4, bg="white", relief=RIDGE,
                                 text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=760, y=5, width=730, height=500)

        # -------------------Scroll Bar Table

        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=0,  width=700, height=470)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(table_frame, columns=(
            "email", "roll", "name", "dep", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("roll", text="Roll")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("dep", text="Department")
        self.Student_table.heading("time", text="Time")
        self.Student_table.heading("date", text="Date")
        self.Student_table.heading("attendance", text="Attendance")

        self.Student_table['show'] = 'headings'

        self.Student_table.column("email", width=100)
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("dep", width=100)
        self.Student_table.column("time", width=100)
        self.Student_table.column("date", width=100)
        self.Student_table.column("attendance", width=100)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease>", self.get_cursor)
        # self.fetch_data()

    # --------------Fetch Data

    def fetchData(self, rows):
        self.Student_table.delete(*self.Student_table.get_children())
        for i in rows:
            self.Student_table.insert("", END, values=i)

    # -------------------IMPORT
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("ALl File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

    # -------------Export CSV
    def exportcsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data", "No Data Found to Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File", "*.csv"), ("ALl File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Export ", "Your Data Exported "+os.path.basename(fln)+" Successfully")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Error due to : {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.Student_table.focus()
        content = self.Student_table.item(cursor_row)
        rows = content['values']
        self.var_email.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])

        # ====================Profile Frame
        img5 = Image.open("data/user."+str(self.var_email.get()) +
                          "."+str(self.var_email.get())+".jpg")
        file_name_path="data/user."+str(1)+"."+str(1)+".jpg"
        img5 = img5.resize((160, 150), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        bg_img5 = Label(self.root, image=self.photoimg5)
        bg_img5.place(x=465, y=470, width=170, height=155)

    def reset_data(self):
        self.var_email.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")

        img10 = Image.open(r"FACEIMAGES\cc2.png")
        img10 = img10.resize((160, 140), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        bg_img10 = Label(self.root, image=self.photoimg10)
        bg_img10.place(x=465, y=470, width=170, height=155)

        img5=Image.open("data/user."+str(self.var_email.get())+"."+str(self.var_email.get())+".jpg")


if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()
