from tkinter import*
from PIL import Image, ImageTk, ImageDraw
from tkinter import ttk
from datetime import*
import time
from math import*
import mysql.connector
from tkinter import messagebox
from Student import Student
from train import train
from face_recog import Face_Recoginition
from Attendence import attendance
import os
import tkinter
from time import strftime
from datetime import datetime

from main import Attendence_System
from Register import Register_GUI


def main():
    win=Tk()
    app = Login_GUI(win)
    win.mainloop()





class Login_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")
        self.root.config(bg="#021e2f")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\ashis\Desktop\Ashish\Atten\AttendenceSystem\college_images\hackers2.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)        

        title1 = Label(self.root, text="LOGIN FACE RECOGINITION SOFTWARE", font=(
            "times new roman", 50, "bold"), bg="#04444a", fg="white").pack(fill=X)

        # ------Frame------
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=400, y=200, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=(
            "times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250, y=50)
        email = Label(login_frame, text="EMAIL ADDRESS", font=(
            "times new roman", 20, "bold"), bg="white", fg="gray").place(x=250, y=150)
        self.txt_email = Entry(login_frame, font=(
            "times new roman", 20), bg="lightgray")
        self.txt_email.place(x=255, y=182, width=350, height=35)

        pass_ = Label(login_frame, text="PASSWORD", font=(
            "times new roman", 20, "bold"), bg="white", fg="gray").place(x=250, y=220)
        self.txt_pass_ = Entry(login_frame, font=(
            "times new roman", 20), bg="lightgray", show="*")
        self.txt_pass_.place(x=255, y=250, width=350, height=35)

        btn_reg = Button(login_frame, text="Register New Account ?", command=self.RegisterPage, font=(
            "times new roman", 12, "bold"), fg="red", bg="lightgray").place(x=420, y=360, width=180, height=40)

        btn_login = Button(login_frame, text="Login", command=self.login, font=(
            "times new roman", 20, "bold"), fg="white", bg="#B00857").place(x=250, y=360, width=150, height=40)

        btn_Pass_reset = Button(login_frame, text="Forgot Password", command=self.forgot_password_window, font=(
            "times new roman", 20, "bold"), fg="white", bg="black").place(x=320, y=420, width=215, height=40)
        
        self.lbl = Label(self.root, bg="white", bd=20, relief=RAISED)
        self.lbl.place(x=200, y=150, height=400, width=400)

        # self.clock_image()
        # self.working()

    def RegisterPage(self):
        # pass
        self.new_window=Toplevel(self.root)
        self.app=Register_GUI(self.new_window)
        # self.root.destroy()
        

    def login(self):
        if self.txt_email.get() == ""or self.txt_pass_.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="@Ashish12345", database="face_recognisation")
                cur = conn.cursor()
                cur.execute("select * from register where email=%s and password=%s",(
                    self.txt_email.get(), 
                    self.txt_pass_.get()
                ))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Username & Password", parent=self.root)
                else:
                    open_main = messagebox.askokcancel("YesNo","Only Access To Admin")
                    if open_main>0:
                        messagebox.showinfo(
                            "Success", "Welcome , Face Recognition Attendance System", parent=self.root)
                        # self.root.destroy()
                        self.new_window=Toplevel(self.root)
                        self.app=Attendence_System(self.new_window)
                        
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self.root)

    # ================================= Reset Password ======================
    def reset_pass(self):
        if self.combo_security_q.get() == "Select":
            messagebox.showerror("Error","Select Security Question", parent=self.root2)
        elif self.Security_a_entry.get()=="":
            messagebox.showerror("Error","Please Enter the Security Answer", parent=self.root2)
        elif self.New_pass_entry.get()=="":
            messagebox.showerror("Error","Please Enter New Password", parent=self.root2)

        else:
            conn = mysql.connector.connect(
                    host="localhost", user="root", password="@Ashish12345", database="face_recognisation")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ = %s and securityA = %s")
            value=(self.txt_email.get(),self.combo_security_q.get(),self.Security_a_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please enter correct Answer", parent=self.root2)
            else:
                query=("update register set password =%s where email=%s")
                value=(self.New_pass_entry.get(),self.txt_email.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset, Please Login With New Password !", parent=self.root2)
                self.root2.destroy()
        





    # ============================ Forgot Password Windows ======================
    def forgot_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please Enter Email id to reset password")
        
        else:
            conn = mysql.connector.connect(
                    host="localhost", user="root", password="@Ashish12345", database="face_recognisation")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value=(self.txt_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                self.root2.config(bg="white")

                l=Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"),fg="black",bg="orange")
                l.place(x=0,y=10,relwidth=1)

                Security_q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
                Security_q.place(x=0, y=80,relwidth=1)

                self.combo_security_q = ttk.Combobox(self.root2, font=("times new roman", 15,"bold"),state="readonly")
                self.combo_security_q["value"] = ("Select","Your birth Place","Your GirlFriend Name","Your Pet Name")
                self.combo_security_q.place(x=50,y=110,width=250)
                self.combo_security_q.current(0)

                
                Security_a = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
                Security_a.place(x=0, y=150,relwidth=1)

                self.Security_a_entry = ttk.Entry(self.root2, font=("times new roman", 15,"bold"))
                self.Security_a_entry.place(x=50, y=180, width=250)

                New_pass = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                New_pass.place(x=0, y=220,relwidth=1)

                self.New_pass_entry = ttk.Entry(self.root2, font=("times new roman", 15,"bold"))
                self.New_pass_entry.place(x=50, y=250, width=250)
                
                btn_Pass_reset = Button(self.root2, text="Reset Password", command=self.reset_pass, font=(
                    "times new roman", 20, "bold"), fg="white", bg="green").place(x=50, y=330, width=250, height=40)








class Register_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")
        self.root.config(bg="#021e2f")


        # ==================== Variables =========================
        self.var_fname = StringVar()
        self.var_l_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_q = StringVar()
        self.var_security_a = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()






        self.bg = ImageTk.PhotoImage(file=r"C:\Users\ashis\Desktop\Ashish\Atten\AttendenceSystem\college_images\hackers2.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        title = Label(self.root, text="REGISTER FACE RECOGINITION SOFTWARE", font=(
            "times new roman", 50, "bold"), bg="#04444a", fg="white").pack(fill=X)
        
        # --------Left Image --------------------
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\ashis\Desktop\Ashish\Atten\AttendenceSystem\college_images\facialrecognition (1).png")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=100,y=150, width=470, height=550)






        # ------Right_Frame------------#
        Register_frame = Frame(self.root, bg="white")
        Register_frame.place(x=570, y=150, width=800, height=550)

        reg = Label(Register_frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), bg="white", fg="#08A3D2").place(x=20, y=20)
        


        # ----------------------lable and entry -------------------->
        
        fname = Label(Register_frame, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(Register_frame,textvariable=self.var_fname, font=("times new roman", 15,"bold"))
        self.fname_entry.place(x=52, y=130, width=250)

        l_name = Label(Register_frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.l_name_entry = ttk.Entry(Register_frame,textvariable=self.var_l_name, font=("times new roman", 15,"bold"))
        self.l_name_entry.place(x=370, y=130, width=250)

        contact = Label(Register_frame, text="Contact", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.contact_entry = ttk.Entry(Register_frame,textvariable=self.var_contact, font=("times new roman", 15,"bold"))
        self.contact_entry.place(x=52, y=200, width=250)


        email = Label(Register_frame, text="Email Id", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.email_entry = ttk.Entry(Register_frame,textvariable=self.var_email, font=("times new roman", 15,"bold"))
        self.email_entry.place(x=370, y=200, width=250)

        Security_q = Label(Register_frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        Security_q.place(x=50, y=235)

        self.combo_security_q = ttk.Combobox(Register_frame,textvariable=self.var_security_q, font=("times new roman", 15,"bold"),state="readonly")
        self.combo_security_q["value"] = ("Select","Your birth Place","Your GirlFriend Name","Your Pet Name")
        self.combo_security_q.place(x=50,y=265,width=250)
        self.combo_security_q.current(0)

        # self.Security_q_entry = ttk.Entry(Register_frame, font=("times new roman", 15,"bold"))
        # self.Security_q_entry.place(x=52, y=260, width=250)

        Security_a = Label(Register_frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        Security_a.place(x=370, y=235)

        self.Security_a_entry = ttk.Entry(Register_frame,textvariable=self.var_security_a, font=("times new roman", 15,"bold"))
        self.Security_a_entry.place(x=370, y=265, width=250)

        pswd = Label(Register_frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=300)

        self.pswd_entry = ttk.Entry(Register_frame,textvariable=self.var_pass, font=("times new roman", 15,"bold"))
        self.pswd_entry.place(x=50, y=330, width=250)
        
        Conf_Pass = Label(Register_frame, text="Confirm Pass", font=("times new roman", 15, "bold"), bg="white", fg="black")
        Conf_Pass.place(x=370, y=300)

        self.Conf_Pass_entry = ttk.Entry(Register_frame,textvariable=self.var_confpass, font=("times new roman", 15,"bold"))
        self.Conf_Pass_entry.place(x=370, y=330, width=250)

        # ================ Check Button ====================== #
        self.var_check = IntVar()
        checkbtn = Checkbutton(Register_frame,variable=self.var_check, text="I Agree The Terms And Condition",font=("times new roman",15,"bold"),onvalue=1, offvalue=0)
        checkbtn.place(x=50, y =370)


        # ================ Button ====================== #

        img = Image.open(r"C:\Users\ashis\Desktop\Ashish\Atten\AttendenceSystem\college_images\register-now-button1.jpg")
        img = img.resize((200,55),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(Register_frame,image=self.photoimage,command=self.register_data ,borderwidth=0, cursor="hand2",font=("times new roman",15, "bold"))
        b1.place(x= 50,y = 420,width =172)

        # img1 = Image.open(r"C:\Users\ashis\Desktop\Ashish\copy\AttendenceSystem1\college_images\login.png")
        # img1 = img1.resize((200,55),Image.ANTIALIAS)
        # self.photoimage1 = ImageTk.PhotoImage(img1)
        # b2 = Button(Register_frame,image=self.photoimage1,borderwidth=0,command=self.login, cursor="hand2",font=("times new roman",15, "bold"))
        # b2.place(x= 410,y = 420,width =200)


        btn_Log = Button(Register_frame, text="Already A User ! Login ?", command=self.login, font=(
            "times new roman", 12, "bold"), fg="red", bg="lightgray").place(x=300, y=430, width=180, height=40)









    def login(self):
        # pass
        self.new_window=Toplevel(self.root)
        self.app=Login_GUI(self.new_window)
        self.root.destroy()

    def register_data(self):
        if self.var_fname.get() == ""or self.var_email.get() == "" or self.var_security_q.get() == "Select":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
            
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password & ConfirmPassword must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please agree our terms and condition")


        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="@Ashish12345", database="face_recognisation")
                my_cursor = conn.cursor()
                query = ("select * from register where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist, please try another email")
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_fname.get(),
                        self.var_l_name.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_security_q.get(),
                        self.var_security_a.get(),
                        self.var_pass.get()
                    ))
                    messagebox.showinfo("Success","Register Successfully")
                
                conn.commit()
                conn.close()
                
            
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self.root)


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

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition ","Are you sure want to exit this Project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


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
    

    def Login_Clock1(self):
        self.root.destroy()
        import Login_GUI
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=help1(self.new_window)

    # def clock_image(self, hr, min_, sec_):
    #     clock = Image.new("RGB", (400, 400), (255, 255, 255))
    #     draw = ImageDraw.Draw(clock)
    #     # =======For Clock Images======
    #     bg = Image.open("./college_images/clock.jpg")
    #     bg = bg.resize((300, 300), Image.ANTIALIAS)
    #     clock.paste(bg, (50, 50))

    #     # ======hour Line Images=====
    #     origin = 200, 200
    #     draw.line((origin, 200+50*sin(radians(hr)), 200-50 *
    #               cos(radians(hr))), fill="black", width=4)
    #     # ======min Line Images=====
    #     draw.line((origin, 200+80*sin(radians(min_)), 200 -
    #               80*cos(radians(min_))), fill="blue", width=3)

    #     # ======sec Line Images=====
    #     draw.line((origin, 200+100*sin(radians(sec_)), 200 -
    #               100*cos(radians(sec_))), fill="green", width=4)
    #     draw.ellipse((195, 195, 210, 210), fill="black")

    #     clock.save("clock_new.png")

    # def working(self):
    #     h = datetime.now().time().hour
    #     m = datetime.now().time().minute
    #     s = datetime.now().time().second
    #     print(h,m,s)

    #     hr = (h/12)*360
    #     min_ = (m/60)*360
    #     sec_ = (s/10)*360

    #     self.clock_image(hr, min_, sec_)
    #     self.img = ImageTk.PhotoImage(file="clock_new.png")
    #     self.lbl.config(image=self.img)
    #     self.lbl.after(200, self.working)


if __name__ == "__main__":
    main()
