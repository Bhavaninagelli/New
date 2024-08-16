from tkinter import *
import mysql.connector
win=Tk()
win.title('Balance Enquiry')
win.geometry('1000x800')
con=mysql.connector.connect(host='localhost',database='accounts',user='root',password='Ajay@123',port=3306)
mycur=con.cursor()


def deposit():
    accnum=e1.get()
    sql="select sum(deposit) from deposits where accnum="+accnum
    mycur.execute(sql)
    totdep=0
    for i in mycur:
       totdep=i
    totdep=totdep[0]
    print(totdep)
  
    mysql="select sum(withdraw) from withdraw where accnum="+accnum
    mycur.execute(mysql)
    totwd=0
    for i in mycur:
        totwd=i
    totwd=totwd[0]
    print(totwd)


    bal=totdep-totwd
    print(bal)
     
   
    depositlbl.config(text=totdep)
    withdrawlbl.config(text=totwd)
    baleq.config(text=bal)

depositlbl=Label(win,font=('calibri',16))
depositlbl.place(x=200, y=300)
dep=Label(win,text='Deposit Amount :-',font=('calibri',14))
dep.place(x=30,y=300)

withdrawlbl=Label(win,font=('calibri',16))
withdrawlbl.place(x=200, y=350)
wthdr=Label(win,text='Withdraw Amount :-',font=('calibri',14))
wthdr.place(x=30,y=350)

baleq=Label(win,font=('calibri',16))
baleq.place(x=200,y=400)
bale=Label(win,text='Balance Amount :-',font=('calibri',14))
bale.place(x=30,y=400)

L1=Label(win,text='State Bank of India',bg='lightblue',
         fg='blue',font=('Elephant',30))
L1.place(x=250,y=20)
L2=Label(win,text='Balance Enquiry',fg='red',
         font=('Calibri',18))
L2.place(x=80,y=100)

search=Label(win,text='Enter Account Number',font=('Arial',16))
search.place(x=30,y=160)
e1=Entry(win,font=('TimesNewRoman',16))
e1.place(x=270,y=160)



btn=Button(win,text='Search',command=deposit)
btn.place(x=550,y=160)
