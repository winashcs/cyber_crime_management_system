from tkinter import* # for creating graphic user interface
from tkinter import ttk  # (themed tk) we use ttk for modern widgets like buttons, labels, and other GUI elements
from PIL import Image,ImageTk # helps for image processing in gui
from tkcalendar import Calendar # for date

class CC: #i used CC here because CyberCrime will be a long keyword
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title('Cybersecurity Incident Management System') 
        self.root.iconbitmap('images/icon.ico')
        
        title=Label(self.root,text='Cybersecurity Incident Management System',font=('Brush Script MT',45,'bold'),bg='#006400',fg='#F5F5DC')
        title.place(x=0,y=0,width=1366,height=70)
        
        logo1_open=Image.open('images/logo.png')
        logo1_open=logo1_open.resize((100,65), Image.LANCZOS)
        self.image_logo1=ImageTk.PhotoImage(logo1_open)
        self.logo1=Label(self.root,image=self.image_logo1)
        self.logo1.place(x=123,y=3,width=100,height=65)
        
        logo2_open=Image.open('images/logo.png')
        logo2_open=logo2_open.resize((100,65), Image.LANCZOS)
        self.image_logo2=ImageTk.PhotoImage(logo2_open)
        self.logo2=Label(self.root,image=self.image_logo2)
        self.logo2.place(x=1143,y=3,width=100,height=65)
        
        frame1=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        frame1.place(x=0,y=70,width=1366,height=130)
        
        i1=Image.open('images/i1.jpg')
        i1=i1.resize((455,130), Image.LANCZOS)
        self.i11=ImageTk.PhotoImage(i1)
        self.i111=Label(frame1,image=self.i11)
        self.i111.place(x=0,y=0,width=455,height=130)
        
        i2=Image.open('images/i3.jpg')
        i2=i2.resize((455,130), Image.LANCZOS)
        self.i22=ImageTk.PhotoImage(i2)
        self.i222=Label(frame1,image=self.i22)
        self.i222.place(x=455,y=0,width=455,height=130)
        
        i3=Image.open('images/i1.jpg')
        i3=i3.resize((455,130), Image.LANCZOS)
        self.i33=ImageTk.PhotoImage(i3)
        self.i333=Label(frame1,image=self.i33)
        self.i333.place(x=910,y=0,width=455,height=130)
        
        frame2=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        frame2.place(x=10,y=200,width=1336,height=495)
        
        frame2_1=LabelFrame(frame2,bd=2,relief=RIDGE,text='Cybersecurity Alerts',font=("Garamond",15,'bold'),fg='dark green',bg='white')
        frame2_1.place(x=10,y=10,width=1316,height=238)
        
        b1=Label(frame2_1,text='Case ID :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b1.grid(row=0,column=0,padx=2,sticky=W,pady=2)
        b11=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b11.grid(row=0,column=1,padx=2,sticky=W,pady=2)
        
        b2=Label(frame2_1,text='Victim Name :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b2.grid(row=1,column=0,padx=2,sticky=W,pady=2)
        b22=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b22.grid(row=1,column=1,padx=2,sticky=W,pady=2)
        
        b3=Label(frame2_1,text='Victim Gender :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b3.grid(row=2,column=0,padx=2,sticky=W,pady=2)
        frame3_1=Frame(frame2_1,bd=1,relief=RIDGE,bg='white',highlightbackground="grey", highlightthickness=1)
        frame3_1.place(x=120,y=56,width=146,height=30)
        b33_male=Radiobutton(frame3_1, text='M',value='male',font=("Arial",10,'bold'),bg='white')
        b33_male.grid(row=0,column=0,pady=0,padx=10,sticky=W)
        b33_female=Radiobutton(frame3_1, text='F',value='female',font=("Arial",10,'bold'),bg='white')
        b33_female.grid(row=0,column=1,pady=0,padx=10,sticky=W)
        
        b4=Label(frame2_1,text='Victim Details :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b4.grid(row=3,column=0,padx=2,sticky=W,pady=10)
        b44=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b44.grid(row=3,column=1,padx=2,sticky=W,pady=3)
        
        b5=Label(frame2_1,text='Date of incident :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b5.grid(row=4,column=0,padx=2,sticky=W,pady=2)
        def show_calendar(event):
            top = Toplevel(root)
            top.iconbitmap('images/icon.ico')
            cal = Calendar(top, selectmode='day', year=2023, month=1, day=1)
            cal.pack(fill='both', expand=True)            
            def select_date():
                selected_date = cal.get_date()
                b55.delete(0, END)
                b55.insert(0, selected_date)
                top.destroy()            
            ok_button = ttk.Button(top, text="OK", command=select_date)
            ok_button.pack(pady=10)        
        b55 = ttk.Entry(frame2_1, width=20, font=("Times New Roman", 10, 'bold'))
        b55.grid(row=4, column=1, padx=2, sticky=W, pady=2)
        b55.bind('<Button-1>', show_calendar)
        
        b6=Label(frame2_1,text='Type of cybercrime :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b6.grid(row=0,column=2,padx=2,sticky=W,pady=2)
        b66=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b66.grid(row=0,column=3,padx=2,sticky=W,pady=2)
        
        b7=Label(frame2_1,text='Type of cyberattack :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b7.grid(row=1,column=2,padx=2,sticky=W,pady=2)
        b77=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b77.grid(row=1,column=3,padx=2,sticky=W,pady=2)
        
        b8=Label(frame2_1,text='Impact Assessment :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b8.grid(row=2,column=2,padx=2,sticky=W,pady=2)
        b88=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b88.grid(row=2,column=3,padx=2,sticky=W,pady=2)
        
        b9=Label(frame2_1,text='IP address :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b9.grid(row=3,column=2,padx=2,sticky=W,pady=2)
        b99=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b99.grid(row=3,column=3,padx=2,sticky=W,pady=2)
        
        b10=Label(frame2_1,text='Device Information :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b10.grid(row=4,column=2,padx=2,sticky=W,pady=2)
        b1010=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b1010.grid(row=4,column=3,padx=2,sticky=W,pady=2)
        
        b11=Label(frame2_1,text='Related Incident :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b11.grid(row=0,column=4,padx=2,sticky=W,pady=2)
        b1111=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b1111.grid(row=0,column=5,padx=2,sticky=W,pady=2)
        
        b12=Label(frame2_1,text='Suspect Name :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b12.grid(row=1,column=4,padx=2,sticky=W,pady=2)
        b1212=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b1212.grid(row=1,column=5,padx=2,sticky=W,pady=2)
        
        b13=Label(frame2_1,text='Suspect Gender :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b13.grid(row=2,column=4,padx=2,sticky=W,pady=2)
        frame3_2=Frame(frame2_1,bd=1,relief=RIDGE,bg='white',highlightbackground="grey", highlightthickness=1)
        frame3_2.place(x=677,y=56,width=146,height=30)
        b1313_male=Radiobutton(frame3_2, text='M',value='Male',font=("Arial",10,'bold'),bg='white')
        b1313_male.grid(row=0,column=0,pady=0,padx=10,sticky=W)
        b1313_female=Radiobutton(frame3_2, text='F',value='Female',font=("Arial",10,'bold'),bg='white')
        b1313_female.grid(row=0,column=1,pady=0,padx=10,sticky=W)
        
        
        b14=Label(frame2_1,text='Suspect Details :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b14.grid(row=3,column=4,padx=2,sticky=W,pady=2)
        b1414=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b1414.grid(row=3,column=5,padx=2,sticky=W,pady=2)
        
        b15=Label(frame2_1,text='Status :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b15.grid(row=4,column=4,padx=2,sticky=W,pady=2)
        selected = StringVar(frame2_1)
        selected.set("SELECT ▼")
        b1515 = OptionMenu(frame2_1, selected,"ONGOING", "CLOSED", "PENDING")
        b1515.configure(font=("Arial", 8,'bold'), bg='white',highlightthickness=1, highlightbackground='grey',activebackground='white',indicatoron=0)
        b1515['menu'].configure(font=("Times New Roman", 10, 'bold'), bg='white')
        b1515.grid(row=4, column=5, padx=2, pady=2, sticky=W)
        
        bf=Frame(frame2_1,bd=2,relief=RIDGE,bg='white')
        bf.place(x=3,y=160,width=613,height=45)
        
        bt1=Button(bf,text='SAVE',font=("Comic Sans MS", 10, 'bold'),bg='#fee01c',width=17,fg='black')
        bt1.grid(row=0,column=0,padx=3,pady=3)
        bt2=Button(bf,text='UPDATE',font=("Comic Sans MS", 10, 'bold'),bg='#fee01c',width=17,fg='black')
        bt2.grid(row=0,column=1,padx=3,pady=3)
        bt3=Button(bf,text='DELETE',font=("Comic Sans MS", 10, 'bold'),bg='#fee01c',width=17,fg='black')
        bt3.grid(row=0,column=2,padx=3,pady=3)
        bt4=Button(bf,text='CLEAR',font=("Comic Sans MS", 10, 'bold'),bg='#fee01c',width=17,fg='black')
        bt4.grid(row=0,column=3,padx=3,pady=3)
        
        i4=Image.open('images/i2.jpg')
        i4=i4.resize((472,222), Image.LANCZOS)
        self.i44=ImageTk.PhotoImage(i4)
        self.i444=Label(frame2_1,image=self.i44)
        self.i444.place(x=840,y=-10,width=472,height=222)
        
        frame2_2=LabelFrame(frame2,bd=2,relief=RIDGE,text='Cybersecurity Alert Dashboard',font=("Garamond",15,'bold'),fg='dark green',bg='white')
        frame2_2.place(x=10,y=248,width=1316,height=238)
        
        frame2_2_1=LabelFrame(frame2_2,bd=2,relief=RIDGE,text='Search Record',font=("Lucida Sans Unicode",11,'bold'),fg='black',bg='white')
        frame2_2_1.place(x=0,y=0,width=1306,height=50)
        sb=Label(frame2_2_1,text='Search By',font=("Georgia",10,'bold'),bg='yellow',fg='black')
        sb.grid(row=0,column=0,padx=4,sticky=W)
        
        design2=Image.open('images/design2.png')
        design2=design2.resize((200,35), Image.LANCZOS)
        self.design22=ImageTk.PhotoImage(design2)
        self.design222=Label(frame2_2_1,image=self.design22)
        self.design222.place(x=950,y=-8,width=200,height=35)
        
        design1=Image.open('images/design1.png')
        design1=design1.resize((40,29), Image.LANCZOS)
        self.design11=ImageTk.PhotoImage(design1)
        self.design111=Label(frame2_2_1,image=self.design11)
        self.design111.place(x=1047,y=-5,width=40,height=29)
        
        dd1=ttk.Combobox(frame2_2_1,font=("Georgia",9,'bold'),width=17,state='readonly')
        dd1['value']=('Select Option','Case ID','IP address','Status')
        dd1.current(0)
        dd1.grid(row=0,column=1,padx=4,sticky=W)
        
        searchtxt=ttk.Entry(frame2_2_1,width=17,font=("Georgia",9,'bold'))
        searchtxt.grid(row=0,column=2,padx=4,sticky=W)
        
        searchbn=Button(frame2_2_1,text='SEARCH',font=("Georgia",9,'bold'),bg='#fee01c',width=17,fg='black')
        searchbn.grid(row=0,column=3,padx=4,sticky=W)
        
        all1=Button(frame2_2_1,text='SHOW ALL',font=("Georgia",9,'bold'),bg='#fee01c',width=17,fg='black')
        all1.grid(row=0,column=4,padx=4,sticky=W)
        
        table_frame=Frame(frame2_2,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=50,width=1306,height=162)      
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.details_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Ebrima',10,'bold'))
        
        self.details_table.heading('1',text='Case ID')
        self.details_table.heading('2',text='Victim Name')
        self.details_table.heading('3',text='Victim Gender')
        self.details_table.heading('4',text='Victim Details')
        self.details_table.heading('5',text='Date of incident')
        self.details_table.heading('6',text='Type of cybercrime')
        self.details_table.heading('7',text='Type of cyberattack')
        self.details_table.heading('8',text='Impact Assessment')
        self.details_table.heading('9',text='IP address')
        self.details_table.heading('10',text='Device Information')
        self.details_table.heading('11',text='Related Incident')
        self.details_table.heading('12',text='Suspect Name')
        self.details_table.heading('13',text='Suspect Gender')
        self.details_table.heading('14',text='Suspect Details')
        self.details_table.heading('15',text='Status')
        
        self.details_table['show']='headings'
        
        self.details_table.column('1',width=75)
        self.details_table.column('2',width=150)
        self.details_table.column('3',width=110)
        self.details_table.column('4',width=220)
        self.details_table.column('5',width=135)
        self.details_table.column('6',width=160)
        self.details_table.column('7',width=150)
        self.details_table.column('8',width=150)
        self.details_table.column('9',width=130)
        self.details_table.column('10',width=160)
        self.details_table.column('11',width=135)
        self.details_table.column('12',width=150)
        self.details_table.column('13',width=130)
        self.details_table.column('14',width=220)
        self.details_table.column('15',width=75)
        
        self.details_table.pack(fill=BOTH,expand=1)        
        
if __name__=="__main__":
    root=Tk()
    obj=CC(root)
    root.mainloop()
