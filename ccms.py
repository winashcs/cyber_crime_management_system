from tkinter import* # for creating graphic user interface
from tkinter import ttk  # (themed tk) we use ttk for modern widgets like buttons, labels, and other GUI elements
from PIL import Image,ImageTk # helps for image processing in gui

class CC: #i used CC here because CyberCrime will be a long keyword
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title('CYBER CRIME MANAGEMENT SYSTEM') 
        self.root.iconbitmap('images/icon.ico')
        
        title=Label(self.root,text='CYBER CRIME MANAGEMENT SYSTEM',font=('Brush Script MT',30,'bold'),bg='black',fg='green')
        title.place(x=0,y=0,width=1366,height=70)
        
        logo1_open=Image.open('images/logo.png')
        logo1_open=logo1_open.resize((100,65), Image.Resampling.LANCZOS)
        self.image_logo1=ImageTk.PhotoImage(logo1_open)
        self.logo1=Label(self.root,image=self.image_logo1)
        self.logo1.place(x=203,y=3,width=100,height=65)
        logo2_open=Image.open('images/logo.png')
        logo2_open=logo2_open.resize((100,65), Image.Resampling.LANCZOS)
        self.image_logo2=ImageTk.PhotoImage(logo2_open)
        self.logo2=Label(self.root,image=self.image_logo2)
        self.logo2.place(x=1063,y=3,width=100,height=65)
        
        frame1=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        frame1.place(x=0,y=70,width=1366,height=130)
        
        i1=Image.open('images/i1.jpg')
        i1=i1.resize((455,130), Image.Resampling.LANCZOS)
        self.i11=ImageTk.PhotoImage(i1)
        self.i111=Label(frame1,image=self.i11)
        self.i111.place(x=0,y=0,width=455,height=130)
        
        i2=Image.open('images/i3.jpg')
        i2=i2.resize((455,130), Image.Resampling.LANCZOS)
        self.i22=ImageTk.PhotoImage(i2)
        self.i222=Label(frame1,image=self.i22)
        self.i222.place(x=455,y=0,width=455,height=130)
        
        i3=Image.open('images/i1.jpg')
        i3=i3.resize((455,130), Image.Resampling.LANCZOS)
        self.i33=ImageTk.PhotoImage(i3)
        self.i333=Label(frame1,image=self.i33)
        self.i333.place(x=910,y=0,width=455,height=130)
        
        frame2=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        frame2.place(x=10,y=200,width=1336,height=495)
        
        frame2_1=LabelFrame(frame2,bd=2,relief=RIDGE,text='Cybersecurity Alerts',font=("Garamond",15,'bold'),fg='dark green',bg='white')
        frame2_1.place(x=10,y=10,width=1316,height=238)
        
        frame2_2=LabelFrame(frame2,bd=2,relief=RIDGE,text='Cybersecurity Alert Dashboard',font=("Garamond",15,'bold'),fg='dark green',bg='white')
        frame2_2.place(x=10,y=248,width=1316,height=238)
        
        frame2_2_1=LabelFrame(frame2_2,bd=2,relief=RIDGE,text='Search Record',font=("Helvetica",10,'bold'),fg='black',bg='white')
        frame2_2_1.place(x=0,y=0,width=1306,height=50)
        
        



if __name__=="__main__":
    root=Tk()
    obj=CC(root)
    root.mainloop()    