from tkinter import* # for creating graphic user interface
from tkinter import ttk  # (themed tk) we use ttk for modern widgets like buttons, labels, and other GUI elements
from PIL import Image,ImageTk # helps for image processing in gui

class CC: #i used CC here because CyberCrime will be a long keyword
    def __init__(self,root):
        self.root=root
        self.root.geometry('1300x700+0+0')
        self.root.title('CYBER CRIME MANAGEMENT SYSTEM') 
        self.root.iconbitmap('images/icon.ico')
        title=Label(self.root,text='CYBER CRIME MANAGEMENT SYSTEM',font=('Helvetica',30,'bold'),bg='black',fg='green')
        title.place(x=0,y=0,width=1300,height=70)
        logo1_open=Image.open('images/logo.png')
        logo1_open=logo1_open.resize((100,65), Image.Resampling.LANCZOS)
        self.image_logo1=ImageTk.PhotoImage(logo1_open)
        self.logo1=Label(self.root,image=self.image_logo1)
        self.logo1.place(x=150,y=3,width=100,height=65)
        logo2_open=Image.open('images/logo.png')
        logo2_open=logo2_open.resize((100,65), Image.Resampling.LANCZOS)
        self.image_logo2=ImageTk.PhotoImage(logo2_open)
        self.logo2=Label(self.root,image=self.image_logo2)
        self.logo2.place(x=1050,y=3,width=100,height=65)
        
        
        





if __name__=="__main__":
    root=Tk()
    obj=CC(root)
    root.mainloop()    