from tkinter import *
import mysql.connector
import datetime
win=Tk()
win.geometry('600x400')
win.title('Deposits')

con=mysql.connector.connect(host='localhost',database='accounts',user='root',password='Ajay@123',port=3306)
mycur=con.cursor()

def search():
    accnum=e1.get()
    sql='select * from newaccount where accnum='+accnum
    mycur.execute (sql)
    data=[]
    for i in mycur:
        for dt in i:
            data.append(dt)
    
    accnolbl.config(text=data[0])
    accnamelbl.config(text=data[1])
    addresslbl.config(text=data[3])
    
    #print(datetime.datetime.now())
    
def save():
    accnum=e1.get()
    deposit=e3.get()
    mycur.execute('insert into deposits(accnum,deposit)values(%s,%s)',
                  (accnum,deposit))
    mycur.execute('commit')
   
searchbtn=Button(win,text='SEARCH',command=search)
searchbtn.place(x=550,y=160)  

accnolbl=Label(win,font=('calibri',25))
accnolbl.place(x=750, y=160)
accnamelbl=Label(win,font=('calibri',25))
accnamelbl.place(x=750, y=200)
addresslbl=Label(win,font=('calibri',25))
addresslbl.place(x=750, y=240)

L1=Label(win,text='State Bank of India',bg='lightblue',
         fg='blue',font=('Elephant',30))
L1.place(x=250,y=20)
L2=Label(win,text='Account Deposits',fg='red',
         font=('Calibri',18))
L2.place(x=80,y=100)

search=Label(win,text='Enter Account Number',font=('Arial',16))
search.place(x=30,y=160)
e1=Entry(win,font=('TimesNewRoman',16))
e1.place(x=270,y=160)

deposit=Label(win,text='Deposit Amount',font=('Arial',16))
deposit.place(x=30,y=230)
e3=Entry(win,font=('TimesNewRoman',16))
e3.place(x=270,y=230)

savebtn=Button(win,text='Save',font=('calbri',20),bg='blue',command=save)
savebtn.place(x=150,y=350)



win.mainloop()
