from tkinter import *
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
global UpdateId
#Database
count=0
connection = psycopg2.connect(user = "postgres",
                                      password = "a",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "postgres")

cursor = connection.cursor()
def createdb ():
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS society(count int,name text,room text,address text,city text,state text,pcode text,hphone text,wphone text,email text,rd text,rm text,ry text,dd text,dm text,dy text,wing text);")
        connection.commit()
    except (Exception, psycopg2.Error) as error :
        print ("Error while creating to PostgreSQL", error)


def backi ():
    i.destroy()
    main()


#INFO DSIPLAY
def info():
    global i
    i = Tk()
    i.title('Society Member Information')
    #i.geometry("900x200")
    l35 = Label(i,text = "\tID\t").grid(row=2, column=0)
    l23 = Label(i,text = "\tName\t").grid(row=2, column=1)
    l24 = Label(i,text = "\tWing\t").grid(row=2, column=2)
    l25 = Label(i,text = "\tRoom No.     ").grid(row=2, column=3)
    l26 = Label(i,text = "\tAddress \t").grid(row=2, column=4)
    l27 = Label(i,text = "\tCity\t").grid(row=2, column=5)
    l28 = Label(i,text = "\tSate\t").grid(row=2, column=6)
    l29 = Label(i,text = "Postal Code\t").grid(row=2, column=7)
    l30 = Label(i,text = "Home Phone\t").grid(row=2, column=8)
    l31 = Label(i,text = "\tWork Phone\t").grid(row=2, column=9)
    l32 = Label(i,text = "Email ID\t").grid(row=2, column=10)
    l33 = Label(i,text = "Registraion Date\t").grid(row=2, column=11)
    l34 = Label(i,text = "Date Of Birth\t").grid(row=2, column=12)

    cursor.execute("SELECT * from society ;")
    records = cursor.fetchall()
    x=0
    for y in records:
        x=x+1
        l35 = Label(i,text = y[0]).grid(row=3+x, column=0)
        l23 = Label(i,text = y[1]).grid(row=3+x, column=1)
        l24 = Label(i,text = y[16]).grid(row=3+x, column=2)
        l25 = Label(i,text = y[2]).grid(row=3+x, column=3)
        l26 = Label(i,text = y[3]).grid(row=3+x, column=4)
        l27 = Label(i,text = y[4]).grid(row=3+x, column=5)
        l28 = Label(i,text = y[5]).grid(row=3+x, column=6)
        l29 = Label(i,text = y[6]).grid(row=3+x, column=7)
        l30 = Label(i,text = y[7]).grid(row=3+x, column=8)
        l31 = Label(i,text = y[8]).grid(row=3+x, column=9)
        l32 = Label(i,text = y[9]).grid(row=3+x, column=10)
        l33 = Label(i,text = (y[10]+"/"+y[11]+"/"+y[12])).grid(row=3+x, column=11)
        l34 = Label(i,text = (y[13]+"/"+y[14]+"/"+y[15])).grid(row=3+x, column=12) 

    back = Button(i, text='Back', width=15,pady =5,bg='Green',fg='white',command=backi).grid(row=4+x)
        
    
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
        createdb ()
        global count
        count = count+1
        name=e1.get()
        room=e2.get()
        address=e3.get()
        city=e4.get()
        state=e5.get()
        pcode=e7.get()
        hphone=e8.get()
        wphone=e9.get()
        email=e10.get()
        rd=s1.get()
        rm=s2.get()
        ry=s3.get()
        dd=s4.get()
        dm=s5.get()
        dy=s6.get()
        x=b1.curselection()
        if x[0]==0:
            wing=str("A")
        if x[0]==1:
            wing=str("B")
        if x[0]==2:
            wing=str("C")
        if x[0]==3:
            wing=str("D")
        cursor.execute("INSERT INTO society VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(count,name,room,address,city,state,pcode,hphone,wphone,email,rd,rm,ry,dd,dm,dy,wing))
        connection.commit();
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
    
def backd ():
    d.destroy()
    main()
    
def deleteMember ():
    deleteId=e11.get()
    cursor.execute("DELETE FROM society WHERE count = %s;",(deleteId,))
    cursor.executemany("UPDATE society SET count=count-1 where count > %s;",(deleteId,))
    connection.commit()
    messagebox.showinfo("Succesful", "DELETED MEMBER INFO")
    d.destroy()
    main()

def delete ():
    global d,e11,deleteId
    d = Tk()
    d.title('Remove Society Member')
    d.geometry("500x200")
    l36 = Label(d, text = "Enter ID Of Member:",font=("bold")).place(x=150,y=50)
    e11 = Entry(d)
    e11.place(x = 225, y = 100, height = 20, width = 50)
    deleteId=e11.get()
    delete = Button(d, text='Delete', width=25,pady = 10,bg='Red',fg='white',command=deleteMember).place(x=150,y=150)
    back = Button(d, text='Back', width=15,pady = 10,bg='Green',fg='white',command=backd).place(x=25,y=150)

def backu ():
    u.destroy()
    main()
    
def chk2 ():
    if(chk3.get()==False):
        chk3.set(True)
    else:
        chk3.set(False)
        
    if(chk4.get()==False):
        chk4.set(True)
    else:
        chk4.set(False)

    update = Button(m, text='Update', width=25,pady = 10,bg='Green',fg='white',command=upd).place(x=235,y=435)

def upd():  
    if (b2.curselection()==()) :
       #l20 = Label(t,text = "*FILL ALL FIELDS*",font=("bold",10),fg='red').place(x=265, y=480)
        messagebox.showinfo("Error", "FILL ALL FIELDS")
    else :
        createdb ()
        name=e13.get()
        room=e14.get()
        address=e15.get()
        city=e16.get()
        state=e17.get()
        pcode=e18.get()
        hphone=e19.get()
        wphone=e20.get()
        email=e21.get()
        rd=s7.get()
        rm=s8.get()
        ry=s9.get()
        dd=s10.get()
        dm=s11.get()
        dy=s12.get()
        x=b2.curselection()
        if x[0]==0:
            wing=str("A")
        if x[0]==1:
            wing=str("B")
        if x[0]==2:
            wing=str("C")
        if x[0]==3:
            wing=str("D")
        cursor.execute("UPDATE society SET name=%s,room=%s,address=%s,city=%s,state=%s,pcode=%s,hphone=%s,wphone=%s,email=%s,rd=%s,rm=%s,ry=%s,dd=%s,dm=%s,dy=%s,wing=%s WHERE count=%s;",(name,room,address,city,state,pcode,hphone,wphone,email,rd,rm,ry,dd,dm,dy,wing,UpdateId))
        connection.commit();
        messagebox.showinfo("Succesful", "UPDATED MEMBER INFO")
        m.destroy ()
        main ()

    
def updateMember ():
    global UpdateId
    UpdateId=e12.get()
    u.destroy()
    global m
    m = Tk()
    m.title('Update Member ')
    m.geometry("700x500")

    global e13,e14,e15,e16,e17,e18,e19,e20,e21,s7,s8,s9,s10,s11,s12,chk3,chk4,b2
    
    l38 = Label(m,text = "Full Name :",font=("bold")).place(x=50,y=20)
    e13 = Entry(m)
    e13.place(x=55,y=50,height = 20, width = 200)

    gender = IntVar()
    gender.set(0)
    
    l39 = Label(m, text = "Gender:",font=("bold")).place(x=50,y=75)
    male = Radiobutton(m, text="Male", variable=gender, value=1).place(x=55,y=100)
    female = Radiobutton(m, text="Female", variable=gender, value=2).place(x=120,y=100)
    
    
    l40 = Label(m, text = "Wing Name:",font=("bold")).place(x=350,y=20)
    b2 = Listbox(m,selectmode=SINGLE)
    b2.place(x = 355, y = 50, height = 70, width = 110)
    b2.insert(1,'A-Wing')
    b2.insert(2,'B-Wing')
    b2.insert(3,'C-Wing')
    b2.insert(4,'D-Wing')
    
    l41 = Label(m, text = "Room No. :",font=("bold")).place(x=500,y=20)
    e14 = Entry(m)
    e14.place(x=505,y=50,height = 20, width = 50)

    l42 = Label(m, text = "Registraion Date :",font=("bold")).place(x=400,y=130)
    s7 = Spinbox(m, from_= 1, to = 31)
    s7.place(x=405,y=160,height = 20,width=30)
    s8 = Spinbox(m, from_= 1, to = 12)
    s8.place(x=445,y=160,height = 20,width=30)
    s9 = Spinbox(m, from_= 2000, to = 2020)
    s9.place(x=485,y=160,height = 20,width=50)
    
    l43 = Label(m, text = "Date Of Birth :",font=("bold")).place(x=50,y=130)
    s10 = Spinbox(m, from_= 1, to = 31)
    s10.place(x=55,y=160,height = 20,width=30)
    s11 = Spinbox(m, from_= 1, to = 12)
    s11.place(x=95,y=160,height = 20,width=30)
    s12 = Spinbox(m, from_= 1960, to = 2010)
    s12.place(x=135,y=160,height = 20,width=50)

    chk3=BooleanVar()
    l44 = Label(m, text = "Room Rented :",font=("bold")).place(x=400,y=190)
    c1 = Checkbutton(m, text = "Yes",command=chk2)
    c1.place(x=550,y=195)

    l45 = Label(m, text = "Address :",font=("bold")).place(x=50,y=190)
    e15 = Entry(m)
    e15.place(x=55,y=220,height = 20, width = 250)

    l46 = Label(m, text = "City :",font=("bold")).place(x=50,y=250)
    e16 = Entry(m)
    e16.place(x = 55, y = 280, height = 20, width = 110)

    l47 = Label(m, text = "State :",font=("bold")).place(x=180,y=250)
    e17 = Entry(m)
    e17.place(x = 185, y = 280, height = 20, width = 110)

    l48 = Label(m, text = "Postal Code :",font=("bold")).place(x=310,y=250)
    e18 = Entry(m)
    e18.place(x = 315, y = 280, height = 20, width = 110)
    
    l49 = Label(m, text = "Home Phone :",font=("bold")).place(x=50,y=310)
    e19 = Entry(m)
    e19.place(x = 55, y = 340, height = 20, width = 110)

    l50 = Label(m, text = "Work Phone :",font=("bold")).place(x=200,y=310)
    e20 = Entry(m)
    e20.place(x = 205, y = 340, height = 20, width = 110)

    l51 = Label(m, text = "Email-ID :",font=("bold")).place(x=350,y=310)
    e21 = Entry(m)
    e21.place(x = 355, y = 340, height = 20, width = 200)

    chk4=BooleanVar()
    l52= Label(m, text = "I have read society rules and regulations.",font=(15)).place(x=150,y=400)
    c2 = Checkbutton(m, text = "",command=chk2)
    c2.place(x=545,y=405)

def update ():
    global u,e12
    u = Tk()
    u.title('Update Member Information')
    u.geometry("500x200")
    l37 = Label(u, text = "Enter ID Of Member:",font=("bold")).place(x=150,y=50)
    e12 = Entry(u)
    e12.place(x = 225, y = 100, height = 20, width = 50)
    updateId=e12.get()
    update = Button(u, text='Update', width=25,pady = 10,bg='Red',fg='white',command=updateMember).place(x=150,y=150)
    back = Button(u, text='Back', width=15,pady = 10,bg='Green',fg='white',command=backu).place(x=25,y=150)
    
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
    if radio.get()==3:
        r.destroy()
        delete()
    if radio.get()==4:
        r.destroy()
        update()

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
    op1 = Radiobutton(r, text="Society Member Info", variable=radio, value=1).place(x=240,y=160)

    op2 = Radiobutton(r, text="Register Member In Society", variable=radio, value=2).place(x=240,y=185)

    op3 = Radiobutton(r, text="Remove Member From Society", variable=radio, value=3).place(x=240,y=210)
    
    op4 = Radiobutton(r, text="Update Member Info In Society", variable=radio, value=4).place(x=240,y=235)

    submt = Button(r, text='Submit', width=25,pady = 10,command=submit,bg='green',fg='white').place(x=235,y=275)

    r.mainloop()
main()
