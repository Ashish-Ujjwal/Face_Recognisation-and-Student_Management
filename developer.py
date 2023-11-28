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


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer Profile")





if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()