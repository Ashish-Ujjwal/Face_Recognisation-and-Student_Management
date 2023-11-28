from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation System")

        ################### variable ################
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_phone = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()


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

        # Title ------->
        title_lbl = Label(BG_img, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roman", 30, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=-10, y=-2, width=1540, height=55)

        main_frame = Frame(BG_img, bd=2)
        main_frame.place(x=-10, y=53, width=1540, height=610)

        # left label_frame --->
        Left_Frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_Frame.place(x=20, y=10, width=730, height=580)

        img_left = Image.open("./college_images/facialrecognition.png")
        img_left = img_left.resize((520, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_Frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=10, width=720, height=130)

        # current_course Information --->
        current_course_frame = LabelFrame(Left_Frame, bg="white", bd=2, relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=107)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=(
            "times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"] = (
            "Department", "Computer", "IT", "Mechanical", "Civil", "Diploma")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 13, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Course", "B-Tech", "BSC", "DIPLOMA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), width=17, state="readonly")
        year_combo["values"] = (
            "Year", "1st", "2nd", "3rd", "4th")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        semester_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=(
            "times new roman", 13, "bold"), width=17, state="readonly")
        semester_combo["values"] = ("Semester", "ODD", "EVEN")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Students Information --->
        class_student_frame = LabelFrame(Left_Frame, bg="white", bd=2, relief=RIDGE,
                                         text="Class Students Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=245, width=720, height=310)

        # StudentId
        studentId_label = Label(class_student_frame, text="Student ID:", font=(
            "times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_id, font=(
            "times new roman", 13, "bold"), width=17)
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        student_Name_label = Label(class_student_frame, text="Student Name:", font=(
            "times new roman", 13, "bold"), bg="white")
        student_Name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_Name_entry = ttk.Entry(class_student_frame, textvariable=self.var_name, font=(
            "times new roman", 13, "bold"), width=17)
        student_Name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class division
        class_div_label = Label(class_student_frame, text="Class Div:", font=(
            "times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        # class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, font=(
        #     "times new roman", 13, "bold"), width=17)
        # class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
            "times new roman", 13, "bold"), width=15)
        div_combo["values"] = ("Div", "A", "B", "C", "D", "E", "F")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll_No
        RollNo_label = Label(class_student_frame, text="Roll No:", font=(
            "times new roman", 13, "bold"), bg="white")
        RollNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        RollNo_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, font=(
            "times new roman", 13, "bold"), width=17)
        RollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        Gender_label = Label(class_student_frame, text="Gender:", font=(
            "times new roman", 13, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        # Gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender, font=(
        #     "times new roman", 13, "bold"), width=17)
        # Gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 13, "bold"), width=15, state="readonly")
        Gender_combo["values"] = ("Gender", "Male", "Female", "Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        DOB_label = Label(class_student_frame, text="DOB:", font=(
            "times new roman", 13, "bold"), bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        DOB_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, font=(
            "times new roman", 13, "bold"), width=17)
        DOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        Email_label = Label(class_student_frame, text="Email:", font=(
            "times new roman", 13, "bold"), bg="white")
        Email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, font=(
            "times new roman", 13, "bold"), width=17)
        Email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Address
        Address_label = Label(class_student_frame, text="Address:", font=(
            "times new roman", 13, "bold"), bg="white")
        Address_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        Address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, font=(
            "times new roman", 13, "bold"), width=17)
        Address_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Phone_No
        Phone_No_label = Label(class_student_frame, text="Phone No.:", font=(
            "times new roman", 13, "bold"), bg="white")
        Phone_No_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        Phone_No_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, font=(
            "times new roman", 13, "bold"), width=17)
        Phone_No_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Class Teacher Name
        Class_Teacher_label = Label(class_student_frame, text="Class Teacher:", font=(
            "times new roman", 13, "bold"), bg="white")
        Class_Teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        Class_Teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, font=(
            "times new roman", 13, "bold"), width=17)
        Class_Teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        # self.var_radio1 = StringVar()
        Radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Taken Photo Sample", value="Yes")
        Radiobtn1.grid(row=6, column=0, padx=10, pady=5)

        Radiobtn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        Radiobtn2.grid(row=6, column=1)

        # Buttons frame
        Btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        Btn_frame.place(x=0, y=210, width=715, height=35)

        Savebtn = Button(Btn_frame, text="Save", command=self.add_data, width=17, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        Savebtn.grid(row=0, column=0)

        Updatebtn = Button(Btn_frame, text="Update", width=17, command=self.update_data, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        Updatebtn.grid(row=0, column=1)

        Deletebtn = Button(Btn_frame, text="Delete", width=17, command=self.delete_data, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        Deletebtn.grid(row=0, column=2)

        Resetbtn = Button(Btn_frame, text="Reset", width=17, command=self.reset_data, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        Resetbtn.grid(row=0, column=3)
        ##########

        Btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        Btn_frame1.place(x=0, y=245, width=715, height=35)

        Take_Photo_btn = Button(Btn_frame1, text="Take Photo Sample",command=self.generate_dataset, width=35, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        Take_Photo_btn.grid(row=1, column=0)
        Upload_btn = Button(Btn_frame1, text="Upload A Sample", width=35, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        Upload_btn.grid(row=1, column=2)

        # Right label_frame --->
        Right_Frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        Right_Frame.place(x=760, y=10, width=760, height=580)

        img_Right = Image.open(
            "./college_images/Team-Management-Software-Development.jpg")
        img_Right = img_Right.resize((520, 130), Image.ANTIALIAS)
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)

        f_lbl = Label(Right_Frame, image=self.photoimg_Right)
        f_lbl.place(x=5, y=10, width=720, height=130)

        # Search System ------------->
        Search_frame = LabelFrame(Right_Frame, bg="white", bd=2, relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=720, height=70)

        Search_label = Label(Search_frame, text="Search By:", font=(
            "times new roman", 12, "bold"), bg="Red", fg="White")
        Search_label.grid(row=0, column=0, padx=10, sticky=W)

        Search_combo = ttk.Combobox(Search_frame, font=(
            "times new roman", 13, "bold"), width=17, state="readonly")
        Search_combo["values"] = (
            "Select", "id", "name")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_entry = ttk.Entry(Search_frame, font=(
            "times new roman", 13, "bold"), width=17)
        Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        Search_btn = Button(Search_frame, text="Search", width=11, height=1,command=self.search_data, font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        Search_btn.grid(row=0, column=3, padx=5)

        ShowAll_btn = Button(Search_frame, text="Show All", width=11, height=1, font=(
            "times new roman", 11, "bold"),command=self.fetch_data, bg="blue", fg="white")
        ShowAll_btn.grid(row=0, column=4, padx=5)

        # Table Frame ---->
        table_frame = LabelFrame(Right_Frame, bg="white", bd=2, relief=RIDGE)
        table_frame.place(x=5, y=210, width=720, height=340)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",
                                        "dob", "email", "address", "phone",  "Teacher", "PhotoSample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="RollNo")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("PhotoSample", text="PhotoSample")
        self.student_table["show"] = "headings"

        self.student_table.column("dep",anchor=N, width=100)
        self.student_table.column("course",anchor=N, width=100)
        self.student_table.column("year",anchor=N, width=100)
        self.student_table.column("sem",anchor=N, width=100)
        self.student_table.column("id",anchor=CENTER, width=100)
        self.student_table.column("name",anchor=N, width=100)
        self.student_table.column("div",anchor=N, width=100)
        self.student_table.column("roll",anchor=N, width=100)
        self.student_table.column("gender",anchor=N, width=100)
        self.student_table.column("dob",anchor=N, width=100)
        self.student_table.column("email",anchor=N, width=100)
        self.student_table.column("address",anchor=N, width=100)
        self.student_table.column("phone",anchor=N, width=100)
        self.student_table.column("Teacher",anchor=N, width=100)
        self.student_table.column("PhotoSample",anchor=N, width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


############### function declaration ####################

    # ================ Save Data ====================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="@Ashish12345", database="face_recognisation")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_phone.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),

                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details has been added Successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to :{str(es)}", parent=self.root)

    # ======================= Fetch Data ============================#

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="@Ashish12345", database="face_recognisation")

        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ========================== Get Cursor ============================

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_address.set(data[11]),
        self.var_phone.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # Update Function --------------------->

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)

        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Do You Want to Update this student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="@Ashish12345", database="face_recognisation")
                    my_cursor = conn.cursor()
                    
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,roll=%s,gender=%s,dob=%s,email=%s,address=%s,phone=%s,Teacher=%s,PhotoSample=%s where student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        # self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_phone.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))


                    # ================Another Method ==================#
                    # query=("update student set dep =%s, course= %s, year=%s, sem=%s, student_id=%s,name=%s,roll=%s,gender=%s,dob=%s,address=%s,phone=%s,Teacher=%s,PhotoSample=%s where email=%s")
                    # value=(self.var_dep.get(),
                    #         self.var_course.get(),
                    #         self.var_year.get(),
                    #         self.var_sem.get(),
                    #         self.var_id.get(),
                    #         self.var_name.get(),
                    #         # self.var_div.get(),
                    #         self.var_roll.get(),
                    #         self.var_gender.get(),
                    #         self.var_dob.get(),
                    #         self.var_address.get(),
                    #         self.var_phone.get(),
                    #         self.var_teacher.get(),
                    #         self.var_radio1.get(),
                    #         self.var_email.get())
                    # my_cursor.execute(query,value)


                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "Success", "Student details successfully updated.", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                # print (row)

            except Exception as es:
                # pass
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    # delete fun ---->
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page ", "Do You want to Delete this Stdent details", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="@Ashish12345", database="face_recognisation")
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Deleted", "Successfully deleted Student Details ", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to : {str(es)}", parent=self.root)

    # reset fun ---->

    def reset_data(self):
        self.var_dep.set(""),
        self.var_course.set(""),
        self.var_year.set(""),
        self.var_sem.set(""),
        self.var_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_phone.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set(""),
        self.var_id.set("")

    # ====================Generate Data Set for PHOTO sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="@Ashish12345", database="face_recognisation")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,roll=%s,gender=%s,dob=%s,email=%s,address=%s,phone=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    # self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_phone.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # =====Load Predefined data on Face Frontals from    openCV
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # Minimum Meighbour = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        file_name_path = "data/user." + str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crooped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo(
                    "Result ", "Generating Data Sets Completed !!!")

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to :{str(es)}", parent=self.root)



    def search_data(self):
        pass
        conn = mysql.connector.connect(
                    host="localhost", username="root", password="@Ashish12345", database="face_recognisation")
        my_cursor=conn.cursor()
          
        my_cursor.execute("select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                my_cursor.commit()
        my_cursor.close()




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()


