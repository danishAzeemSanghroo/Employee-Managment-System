from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Employee:
    def __init__(self,root):
     self.root=root
     self.root.geometry("1530x790+0+0")
     self.root.title('Employee Managment System')




if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()