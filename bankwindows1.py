from tkinter import *
import mysql.connector
win=Tk()
win.geometry('1000x800')
con=mysql.connector.connect(host='localhost',database='accounts',user='root',password='Ajay@123',port=3306)
mycur=con.cursor()

def getaccnum():
    mycur.execute('select last_insert_id() from newaccount')
    for i in mycur:
        accnum=i
    return accnum

def selection():
    accname=e1.get()
    uid=e2.get()
    address=e3.get()
    mobno=e4.get()
    dob=e5.get()
    fname=e6.get()
    mname=e7.get()
    
    mycur.execute('insert into newaccount(accname,uid,address,dob,mobno,fname,mname)values(%s,%s,%s,%s,%s,%s,%s)',
              (accname,uid,address,dob,mobno,fname,mname))
    mycur.execute('commit')
    newacc=getaccnum()    
    msg='Account Saved Successfully with Account Number',newacc

    res.config(text=msg)

    
L1=Label(win,text='State Bank of India',bg='lightblue',
         fg='blue',font=('Elephant',30))
L1.place(x=250,y=20)

L2=Label(win,text='Create New Account',fg='red',
         font=('Calibri',18))
L2.place(x=80,y=100)

L3=Label(win,text='Account Holder Name',font=('Arial',16))
L3.place(x=30,y=160)
e1=Entry(win,font=('TimesNewRoman',16))
e1.place(x=270,y=160)

L4=Label(win,text='Adhar Number',font=('Arial',16))
L4.place(x=30,y=200)
e2=Entry(win,font=('TimesNewRoman',16))
e2.place(x=270,y=200)

L5=Label(win,text='Address',font=('Arial',16))
L5.place(x=30,y=240)
e3=Entry(win,font=('TimesNewRoman',16))
e3.place(x=270,y=240)

L6=Label(win,text='Mobile Number',font=('Arial',16))
L6.place(x=30,y=280)
e4=Entry(win,font=('TimesNewRoman',16))
e4.place(x=270,y=280)

L=Label(win,text='(YYYYMMDD)',font=('Arial',10))
L.place(x=270,y=310)
L7=Label(win,text='Date of Birth',font=('Arial',16))
L7.place(x=30,y=340)
e5=Entry(win,font=('TimesNewRoman',16))
e5.place(x=270,y=340)

L8=Label(win,text='Father Name',font=('Arial',16))
L8.place(x=30,y=380)
e6=Entry(win,font=('TimesNewRoman',16))
e6.place(x=270,y=380)

L9=Label(win,text='Mother Name',font=('Arial',16))
L9.place(x=30,y=420)
e7=Entry(win,font=('TimesNewRoman',16))
e7.place(x=270,y=420)

res=Label(win,font=('Calibri',18),bg='yellow')
res.place(x=600,y=150)
btn=Button(win,text='Submit',bg='blue',fg='white',
           font=('Calibri',18),command=selection)
btn.place(x=290,y=500)

