from tkinter import *
from tkinter import scrolledtext, messagebox
import sqlite3
 
window = Tk()

window.geometry('1050x550')
window.title("Goo")
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
re_var = StringVar()

menu = Menu(window)
window.config(menu=menu)


def ex():
    exit()


subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit", command=ex)

def seh():

    c=0
    i=0
    gm=var7.get()
    if(gm == ''):
        messagebox.showerror("Error","Enter Gmail id" )
    else:
        con = sqlite3.connect('Form.db')
        with con:
            cursor = con.cursor()
            cursor.execute('SELECT Gmail FROM Detalis')
            rows = cursor.fetchall()
            for i in range(0,len(rows)):
                if (gm in rows[i][0]):
                    c = 1
                    break
            if (c == 1):
                cursor.execute("SELECT * FROM Detalis WHERE Gmail=:gm", {"gm": gm})
                rows1 = cursor.fetchone()
                s11.configure(text=rows1[0], fg="Red")
                s22.configure(text=rows1[1], fg="Red")
                s33.configure(text=rows1[2], fg="Red")
                s44.configure(text=rows1[3], fg="Red")
                s55.configure(text=rows1[4], fg="Red")
                s66.configure(text=rows1[5], fg="Red")
                s77.configure(text=rows1[6], fg="Red")

            else:
                messagebox.showerror("Error", "No Details")
                c = 0

    return 0


def about():
    messagebox.showinfo("Welcome to My Tool", "I AM GUNA")

def all_d():
    con = sqlite3.connect('Form.db')
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Detalis")
        rows = cursor.fetchall()
        sho=Tk()
        sho.title("All Details")
        sho.geometry("1100x500")
        d1=Label(sho, text="All Details", font=("Courier New", 16, 'bold'), fg="Red")
        d1.place(x=500,y=50)
        d2 = Label(sho, text="Name", font=("Courier New", 16, 'bold'))
        d2.place(x=75, y=100)
        d3 = Label(sho, text="Gmail", font=("Courier New", 16, 'bold'))
        d3.place(x=250, y=100)
        d4 = Label(sho, text="Age", font=("Courier New", 16, 'bold'))
        d4.place(x=430, y=100)
        d5 = Label(sho, text="DOB", font=("Courier New", 16, 'bold'))
        d5.place(x=550, y=100)
        d6 = Label(sho, text="Country", font=("Courier New", 16, 'bold'))
        d6.place(x=650, y=100)
        d7 = Label(sho, text="Gender", font=("Courier New", 16, 'bold'))
        d7.place(x=790, y=100)
        d8 = Label(sho, text="Number", font=("Courier New", 16, 'bold'))
        d8.place(x=910, y=100)
        i=0
        x1=70
        y1=150
        x2=190
        x3=432
        x4=540
        x5=665
        x6=790
        x7=910
        for i in range(0,len(rows)):
            p1=Label(sho,text=rows[i][0],font=("Courier New", 12, 'bold'))
            p1.place(x=x1,y=y1)
            p2=Label(sho,text=rows[i][1],font=("Courier New", 12, 'bold'))
            p2.place(x=x2,y=y1)
            p3=Label(sho,text=rows[i][6],font=("Courier New", 12, 'bold'))
            p3.place(x=x3,y=y1)
            p4=Label(sho,text=rows[i][2],font=("Courier New", 12, 'bold'))
            p4.place(x=x4,y=y1)
            p4=Label(sho,text=rows[i][3],font=("Courier New", 12, 'bold'))
            p4.place(x=x5,y=y1)
            p4=Label(sho,text=rows[i][4],font=("Courier New", 12, 'bold'))
            p4.place(x=x6,y=y1)
            p4=Label(sho,text=rows[i][5],font=("Courier New", 12, 'bold'))
            p4.place(x=x7,y=y1)
            y1 = y1 + 30

def Database():
    fname=var1.get()
    lname=var2.get()
    dob=var3.get()
    coy=var4.get()
    gend=re_var.get()
    pass1=var5.get()
    pass2=var6.get()
    if(fname=='' or lname=='' or  dob=='' or coy=="Select Couuntry" or gend=='' or pass1=='' or pass2==''):
        messagebox.showerror("Error","You must fill in all of the fields." )
    else:
        c=i=0
        con=sqlite3.connect('Form.db')
        with con:
            cursor=con.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Detalis (Name TEXT,Gmail TEXT,DOB TEXT,Country TEXT,Gender TEXT,Phone_Number TEXT,Age TEXT)')
            cursor.execute('SELECT Gmail FROM Detalis')
            rows = cursor.fetchall()
            for i in range(len(rows)):
                if(lname in rows[i][0]):
                    c=1
                    break
            if(c!=1):
                cursor.execute('INSERT INTO Detalis(Name,Gmail,DOB,Country,Gender,Phone_Number,Age) VALUES(?,?,?,?,?,?,?)',(fname, lname, dob, coy, gend, pass1,pass2))
                con.commit()
                messagebox.showinfo("Goo","Data Updated Successfully")
                c=0
            else:
                messagebox.showerror("Error", "Gmail id already exists")


subm2 = Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label="About", command=about)

icon = PhotoImage(file="E:\icons8-ginger-man-in-violet-shirt-100.png")
l2 = Label(window, image=icon)
l2.place(x=160,y=10)
l1 = Label(window, text="Registration Form", font=("Courier New", 16, 'bold'), fg="Red")
l1.place(x=118,y=110)

l3 = Label(window, text="Name", font=("Courier New", 16, 'bold'))
l3.place(x=40, y=150)

e1 = Entry(window, textvar=var1, bg="#dddbdb")
e1.place(x=270, y=153)

l4 = Label(window, text="Gmail ID", font=("Courier New", 16, 'bold'))
l4.place(x=40, y=190)

e2 = Entry(window, textvar=var2, bg="#dddbdb")
e2.place(x=270, y=193)

l5 = Label(window, text="DOB", font=("Courier New", 16, 'bold'))
l5.place(x=40, y=230)

e3 = Entry(window, textvar=var3, bg="#dddbdb")
e3.place(x=270, y=233)

l5 = Label(window, text="Country", font=("Courier New", 16, 'bold'))
l5.place(x=40, y=270)

l = ["Armenia", "Australia", "India", "Japan"]
drp = OptionMenu(window, var4, *l)
var4.set("Select Couuntry")
drp.config(width=14, height=1)
drp.place(x=269, y=273)

l6 = Label(window, text="Gender", font=("Courier New", 16, 'bold'))
l6.place(x=40, y=315)
ra1 = Radiobutton(window, text="Male", value="Male", variable=re_var)
ra2 = Radiobutton(window, text="Female", value="Female", variable=re_var)
re_var.set(False)
ra1.place(x=270, y=315)
ra2.place(x=340, y=315)

l5 = Label(window, text="Phone Number", font=("Courier New", 16, 'bold'))
l5.place(x=40, y=360)

e3 = Entry(window, textvar=var5, bg="#dddbdb")
e3.place(x=270, y=360)

l6 = Label(window, text="Age", font=("Courier New", 16, 'bold'))
l6.place(x=40, y=400)

e4 = Entry(window, textvar=var6, bg="#dddbdb")
e4.place(x=270, y=405)

l7 = Label(window, text="Gmail ID", font=("Courier New", 16, 'bold'))
l7.place(x=525, y=100)

s0 = Entry(window, textvar=var7, bg="#dddbdb")
s0.config(width=28)
s0.place(x=700, y=105)



bt = Button(window, text="Update", font=("Arial", 10), bg="#7970F8", fg="#FFFFFF", command=Database)
bt.config(width=44, height=1)
bt.place(x=40, y=450)
window.bind("<Return>",Database)

bt = Button(window, text="Search", font=("Arial", 10), bg="#7970F8", fg="#FFFFFF",command=seh)
bt.config(width=18, height=1)
bt.place(x=525, y=450)
window.bind("<Return>",seh)

bt2 = Button(window, text="All Details", font=("Arial", 10), bg="#7970F8", fg="#FFFFFF",command=all_d)
bt2.config(width=18, height=1)
bt2.place(x=700, y=450)
window.bind("<Return>",all_d)



#######################################################################################################

s1 = Label(window, text="Name", font=("Courier New", 16, 'bold'))
s1.place(x=525, y=150)

s11 = Label(window, font=("Courier New", 16, 'bold'))
s11.place(x=750, y=150)

s2 = Label(window, text="Gmail ID", font=("Courier New", 16, 'bold'))
s2.place(x=525, y=190)

s22 = Label(window, font=("Courier New", 16, 'bold'))
s22.place(x=750, y=190)

s3 = Label(window, text="DOB", font=("Courier New", 16, 'bold'))
s3.place(x=525, y=230)

s33 = Label(window, font=("Courier New", 16, 'bold'))
s33.place(x=750, y=230)

s4 = Label(window, text="Country", font=("Courier New", 16, 'bold'))
s4.place(x=525, y=270)

s44 = Label(window, font=("Courier New", 16, 'bold'))
s44.place(x=750, y=270)

s5 = Label(window, text="Gender", font=("Courier New", 16, 'bold'))
s5.place(x=525, y=315)

s55 = Label(window, font=("Courier New", 16, 'bold'))
s55.place(x=750, y=315)

s6 = Label(window, text="Phone Number", font=("Courier New", 16, 'bold'))
s6.place(x=525, y=360)

s66 = Label(window, font=("Courier New", 16, 'bold'))
s66.place(x=750, y=360)

s7 = Label(window, text="Age", font=("Courier New", 16, 'bold'))
s7.place(x=525, y=400)

s77 = Label(window, font=("Courier New", 16, 'bold'))
s77.place(x=750, y=400)

window.mainloop()
