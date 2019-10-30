# Frontend

from tkinter import *
import tkinter.messagebox

# import Student's Database


class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        StdID = StringVar()  # Def 1
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        # -------------------------------Frames---------------------------------
        # MainFrame = Frame(self, root, bg="cadet blue")
        # MainFrame.grid()
        #
        # TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        # TitFrame.pack(side=TOP)
        #
        # self.iblTit = Label(TitFrame, font=('arial', 47, 'bold'),
        #                     text="Student Database Management Systems", bg="Ghost White")
        # self.iblTit.grid()


if __name__ == '__main__':
    root = tkinter.Tk()
    application = Student(root)
    root.mainloop()
