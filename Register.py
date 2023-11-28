from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from datetime import*
import time
from math import*
import mysql.connector
from tkinter import messagebox

# from login import Login_GUI

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






        self.bg = ImageTk.PhotoImage(file=r"C:\Users\ashis\Desktop\Ashish\copy\AttendenceSystem1\college_images\hackers2.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        title = Label(self.root, text="REGISTER FACE RECOGINITION SOFTWARE", font=(
            "times new roman", 50, "bold"), bg="#04444a", fg="white").pack(fill=X)
        
        # --------Left Image --------------------
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\ashis\Desktop\Ashish\copy\AttendenceSystem1\college_images\facialrecognition (1).png")
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
        
        Conf_Pass = Label(Register_frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        Conf_Pass.place(x=370, y=300)

        self.Conf_Pass_entry = ttk.Entry(Register_frame,textvariable=self.var_confpass, font=("times new roman", 15,"bold"))
        self.Conf_Pass_entry.place(x=370, y=330, width=250)

        # ================ Check Button ====================== #
        self.var_check = IntVar()
        checkbtn = Checkbutton(Register_frame,variable=self.var_check, text="I Agree The Terms And Condition",font=("times new roman",15,"bold"),onvalue=1, offvalue=0)
        checkbtn.place(x=50, y =370)


        # ================ Button ====================== #

        img = Image.open(r"C:\Users\ashis\Desktop\Ashish\copy\AttendenceSystem1\college_images\register-now-button1.jpg")
        img = img.resize((200,55),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(Register_frame,image=self.photoimage,command=self.register_data ,borderwidth=0, cursor="hand2",font=("times new roman",15, "bold"))
        b1.place(x= 50,y = 420,width =172)

        img1 = Image.open(r"C:\Users\ashis\Desktop\Ashish\copy\AttendenceSystem1\college_images\login.png")
        img1 = img1.resize((200,55),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(Register_frame,image=self.photoimage1,borderwidth=0,command=self.login, cursor="hand2",font=("times new roman",15, "bold"))
        b2.place(x= 410,y = 420,width =200)









    def login(self):
        # pass
        # self.root.destroy()
        self.new_window=Toplevel(self.root)
        self.app=Login_GUI(self.new_window)
        # import login

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
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")
                
            
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due to : {str(es)}", parent=self.root)
                

if __name__ == "__main__":
    root = Tk()
    obj = Register_GUI(root)
    root.mainloop()