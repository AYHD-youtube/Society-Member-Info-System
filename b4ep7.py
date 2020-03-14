from tkinter import *
from tkinter import messagebox


#Database
count=1
name = ["Abhishek Yadav"]
room = ["304"]
address=["A-304 mayuresh residency bhandup west"]
city=["Mumbai"]
state=["Maharashtra"]
pcode=["400078"]
hphone=["25952466"]
wphone=["9702858226"]
email=["abhishek3yadav3@gmail.com"]
rd=["2"]
rm=["3"]
ry=["2013"]
dd=["26"]
dm=["5"]
dy=["2000"]
wing=["A"]


def backi ():
    i.destroy()
    main()


#INFO DSIPLAY
def info():
    global i
    i = Tk()
    i.title('Society Member Information')
    #i.geometry("900x500")      
    l23 = Label(i,text = "\tName\t").grid(row=2, column=0)
    l24 = Label(i,text = "\tWing\t").grid(row=2, column=1)
    l25 = Label(i,text = "\tRoom No.     ").grid(row=2, column=2)
    l26 = Label(i,text = "\tAddress \t").grid(row=2, column=3)
    l27 = Label(i,text = "\tCity\t").grid(row=2, column=4)
    l28 = Label(i,text = "\tSate\t").grid(row=2, column=5)
    l29 = Label(i,text = "Postal Code\t").grid(row=2, column=6)
    l30 = Label(i,text = "Home Phone\t").grid(row=2, column=7)
    l31 = Label(i,text = "\tWork Phone\t").grid(row=2, column=8)
    l32 = Label(i,text = "Email ID\t").grid(row=2, column=9)
    l33 = Label(i,text = "Registraion Date\t").grid(row=2, column=10)
    l34 = Label(i,text = "Date Of Birth\t").grid(row=2, column=11)
    
    for x in range(count):
        l23 = Label(i,text = name[x]).grid(row=3+x, column=0)
        l24 = Label(i,text = wing[x]).grid(row=3+x, column=1)
        l25 = Label(i,text = room[x]).grid(row=3+x, column=2)
        l26 = Label(i,text = address[x]).grid(row=3+x, column=3)
        l27 = Label(i,text = city[x]).grid(row=3+x, column=4)
        l28 = Label(i,text = state[x]).grid(row=3+x, column=5)
        l29 = Label(i,text = pcode[x]).grid(row=3+x, column=6)
        l30 = Label(i,text = hphone[x]).grid(row=3+x, column=7)
        l31 = Label(i,text = wphone[x]).grid(row=3+x, column=8)
        l32 = Label(i,text = email[x]).grid(row=3+x, column=9)
        l33 = Label(i,text = (rd[x]+"/"+rm[x]+"/"+ry[x])).grid(row=3+x, column=10)
        l34 = Label(i,text = (dd[x]+"/"+dm[x]+"/"+dy[x])).grid(row=3+x, column=11)

    back = Button(i, text='Back', width=15,pady =5,bg='Green',fg='white',command=backi).grid(row=4+count)
        
    
    i.mainloop()

def backt ():
    t.destroy()
    main()

def chk ():
    if(chk1.get()==False):
        chk1.set(True)
    else:
        chk1.set(False)
        
    if(chk2.get()==False):
        chk2.set(True)
    else:
        chk2.set(False)

    regist = Button(t, text='Register', width=25,pady = 10,bg='Red',fg='white',command=reg).place(x=235,y=435)

def reg():    
    if (b1.curselection()==()) :
       #l20 = Label(t,text = "*FILL ALL FIELDS*",font=("bold",10),fg='red').place(x=265, y=480)
        messagebox.showinfo("Error", "FILL ALL FIELDS")
    else :
        global count
        count = count+1
        name.append(e1.get())
        room.append(e2.get())
        address.append(e3.get())
        city.append(e4.get())
        state.append(e5.get())
        pcode.append(e7.get())
        hphone.append(e8.get())
        wphone.append(e9.get())
        email.append(e10.get())
        rd.append(s1.get())
        rm.append(s2.get())
        ry.append(s3.get())
        dd.append(s4.get())
        dm.append(s5.get())
        dy.append(s6.get())
        x=b1.curselection()
        if x[0]==0:
            wing.append(str("A"))
        if x[0]==1:
            wing.append(str("B"))
        if x[0]==2:
            wing.append(str("C"))
        if x[0]==3:
            wing.append(str("D"))
        print(wing)
        t.destroy ()
        main ()

    
#REGISTRATION
def register():
    global t
    t = Tk()
    t.title('Register Member ')
    t.geometry("700x500")

    global e1,e2,e3,e4,e5,e7,e8,e9,e10,s1,s2,s3,s4,s5,s6,chk1,chk2,b1,backt
    
    l1 = Label(t,text = "Full Name :",font=("bold")).place(x=50,y=20)
    e1 = Entry(t)
    e1.place(x=55,y=50,height = 20, width = 200)

    gender = IntVar()
    gender.set(0)
    
    l2 = Label(t, text = "Gender:",font=("bold")).place(x=50,y=75)
    male = Radiobutton(t, text="Male", variable=gender, value=1).place(x=55,y=100)
    female = Radiobutton(t, text="Female", variable=gender, value=2).place(x=120,y=100)
    
    
    l3 = Label(t, text = "Wing Name:",font=("bold")).place(x=350,y=20)
    b1 = Listbox(t,selectmode=SINGLE)
    b1.place(x = 355, y = 50, height = 70, width = 110)
    b1.insert(1,'A-Wing')
    b1.insert(2,'B-Wing')
    b1.insert(3,'C-Wing')
    b1.insert(4,'D-Wing')
    
    l4 = Label(t, text = "Room No. :",font=("bold")).place(x=500,y=20)
    e2 = Entry(t)
    e2.place(x=505,y=50,height = 20, width = 50)

    l5 = Label(t, text = "Registraion Date :",font=("bold")).place(x=400,y=130)
    s1 = Spinbox(t, from_= 1, to = 31)
    s1.place(x=405,y=160,height = 20,width=30)
    s2 = Spinbox(t, from_= 1, to = 12)
    s2.place(x=445,y=160,height = 20,width=30)
    s3 = Spinbox(t, from_= 2000, to = 2020)
    s3.place(x=485,y=160,height = 20,width=50)
    
    l6 = Label(t, text = "Date Of Birth :",font=("bold")).place(x=50,y=130)
    s4 = Spinbox(t, from_= 1, to = 31)
    s4.place(x=55,y=160,height = 20,width=30)
    s5 = Spinbox(t, from_= 1, to = 12)
    s5.place(x=95,y=160,height = 20,width=30)
    s6 = Spinbox(t, from_= 1960, to = 2010)
    s6.place(x=135,y=160,height = 20,width=50)

    chk1=BooleanVar()
    l7 = Label(t, text = "Room Rented :",font=("bold")).place(x=400,y=190)
    c1 = Checkbutton(t, text = "Yes",command=chk)
    c1.place(x=550,y=195)

    l8 = Label(t, text = "Address :",font=("bold")).place(x=50,y=190)
    e3 = Entry(t)
    e3.place(x=55,y=220,height = 20, width = 250)

    l9 = Label(t, text = "City :",font=("bold")).place(x=50,y=250)
    e4 = Entry(t)
    e4.place(x = 55, y = 280, height = 20, width = 110)

    l10 = Label(t, text = "State :",font=("bold")).place(x=180,y=250)
    e5 = Entry(t)
    e5.place(x = 185, y = 280, height = 20, width = 110)

    l12 = Label(t, text = "Postal Code :",font=("bold")).place(x=310,y=250)
    e7 = Entry(t)
    e7.place(x = 315, y = 280, height = 20, width = 110)
    
    l13 = Label(t, text = "Home Phone :",font=("bold")).place(x=50,y=310)
    e8 = Entry(t)
    e8.place(x = 55, y = 340, height = 20, width = 110)

    l14 = Label(t, text = "Work Phone :",font=("bold")).place(x=200,y=310)
    e9 = Entry(t)
    e9.place(x = 205, y = 340, height = 20, width = 110)

    l15 = Label(t, text = "Email-ID :",font=("bold")).place(x=350,y=310)
    e10 = Entry(t)
    e10.place(x = 355, y = 340, height = 20, width = 200)

    chk2=BooleanVar()
    l16= Label(t, text = "I have read society rules and regulations.",font=(15)).place(x=150,y=400)
    c2 = Checkbutton(t, text = "",command=chk)
    c2.place(x=545,y=405)

    back = Button(t, text='Back', width=25,pady = 10,bg='Green',fg='white',command=backt).place(x=25,y=435)

    t.mainloop()
    
def submit():
    if radio.get()==0:
        #l19 = Label(text = "SELECT AN OPTION BEFORE CLCIKING SUBMIT",font=("bold",15),fg='red').place(x=120, y=350)
        messagebox.showinfo("Error", "SELECT AN OPTION BEFORE CLCIKING SUBMIT")

    if radio.get()==1:
        r.destroy()
        info()
    if radio.get()==2:
        r.destroy()
        register()
    


#Front Page
def main ():
    global r
    r = Tk()

    r.title('Society Member System')
    r.geometry("700x400")

    l17 = Label(text = "Welcome To Mayuresh Residential Society",font=("bold", 20)).place(x=80, y=40)

    l18 = Label(text = "Select An Option :",font=("bold",15)).place(x=240, y=125)

    global radio
    radio = IntVar()
    radio.set(0)
    op1 = Radiobutton(r, text="Society Member Info", variable=radio, value=1).place(x=240,y=175)

    op2 = Radiobutton(r, text="Register Member In Society", variable=radio, value=2).place(x=240,y=200)


    submt = Button(r, text='Submit', width=25,pady = 10,command=submit,bg='green',fg='white').place(x=235,y=250)

    r.mainloop()
main()

