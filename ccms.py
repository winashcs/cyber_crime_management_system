from tkinter import* # for creating graphic user interface
from tkinter import ttk  # (themed tk) we use ttk for modern widgets like buttons, labels, and other GUI elements
from PIL import Image,ImageTk # helps for image processing in gui

class CC: #i used CC here because CyberCrime will be a long keyword
    def __init__(self,root):
        self.root=root
        self.root.geometry('1300x700+0+0')
        self.root.title('CYBER CRIME MANAGEMENT SYSTEM') 
        self.root.iconbitmap('icon.ico')








if __name__=="__main__":
    root=Tk()
    obj=CC(root)
    root.mainloop()    