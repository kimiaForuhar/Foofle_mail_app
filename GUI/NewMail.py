from tkinter import *
from GUI import Inbox, Sent, News, EditInfo, Errors
from SQL import Procedures as P
import mysql.connector


def myinbox():
    rootA.destroy()
    Inbox.callinboxfeed()


def mysent():
    rootA.destroy()
    Sent.callsentfeed()


def mynews():
    rootA.destroy()
    News.callnews()


def myedit():
    rootA.destroy()
    EditInfo.calledit()


def newmailfeed():
    global rootA, tot, cct, subjectt, mailt
    labelfont = ('elephant italic', 70, 'bold')
    rootA = Tk()
    rootA.configure(bg='#D0CAEE')
    rootA.geometry("1000x1500")
    rootA.title('Foofle')
    titlelayout = Frame(rootA, width=500, height=170, bg='#D0CAEE')
    titlelayout.place(x=0, y=0)
    barlayout = Frame(rootA, width=200, height=1500, bg='#EECAE6')
    barlayout.grid(row=0, column=0, padx=0, pady=170)
    intruction = Label(rootA, text='foofle\n', bg='#D0CAEE')
    intruction.place(x=400, y=20)
    intruction.config(font=labelfont)
    mainfeed = Label(rootA, bg='#DBCEEC')
    mainfeed.place(x=200, y=170)
    mainfeed.config(width=200, height=200)
    myfont = ('times', 15, 'bold')
    froml = Label(mainfeed, text="from:\t    %s@foofle.com" % P.getlastlogin(), bg='#DBCEEC')
    froml.place(x=20, y=20)
    froml.config(font=myfont)
    tol = Label(mainfeed, text="to:", bg='#DBCEEC')
    tol.place(x=20, y=60)
    tol.config(font=myfont)
    cc = Label(mainfeed, text="cc:", bg='#DBCEEC')
    cc.place(x=20, y=100)
    cc.config(font=myfont)
    subject = Label(mainfeed, text="Subject:", bg='#DBCEEC')
    subject.place(x=20, y=140)
    subject.config(font=myfont)
    tot = Entry(mainfeed, width=100)
    tot.place(x=120, y=60)
    cct = Entry(mainfeed, width=100)
    cct.place(x=120, y=100)
    subjectt = Entry(mainfeed, width=100)
    subjectt.place(x=120, y=140)
    mailt = Text(mainfeed, width=88, height=15)
    mailt.place(x=20, y=170)
    save = Button(mainfeed, text='send', width=10, command=getinput)
    save.place(x=300, y=500)
    newsB = Button(barlayout, text='news', command=mynews)
    newsB.place(x=20, y=30)
    newsB.config(width=15)
    inboxB = Button(barlayout, text='inbox', command=myinbox)
    inboxB.place(x=20, y=70)
    inboxB.config(width=15)
    sentB = Button(barlayout, text='sent', command=mysent)
    sentB.place(x=20, y=110)
    sentB.config(width=15)
    editB = Button(barlayout, text='edit info', command=myedit)
    editB.place(x=20, y=480)
    editB.config(width=15)
    new_mailB = Button(barlayout, text='new mail')
    new_mailB.place(x=20, y=440)
    new_mailB.config(width=15)
    logoutB = Button(barlayout, text='log out', command=logout)
    logoutB.place(x=20, y=520)
    logoutB.config(width=15)
    user = Label(rootA, text="logged in as", bg='#DBCEEC')
    user.place(x=410, y=140)
    name = P.getlastlogin()
    usern = Label(rootA, text=name, bg='#DBCEEC')
    usern.place(x=477, y=140)
    rootA.resizable(0, 1)
    rootA.mainloop()


def callnewmail():
    newmailfeed()


def logout():
    rootA.destroy()


def getinput():
    to = str(tot.get())
    cc = cct.get()
    if cc != to:
        Errors.error('cc recivers list should be the same as recivers list')
    else:
        subj = subjectt.get()
        body = mailt.get("1.0", END)
        try:
            P.addnewmail(subj, body, P.getlastlogin())
            to = to.split(',')
            for i in range(len(to)):
                P.addtorecivers(to[i])
        except mysql.connector.Error as e:
            Errors.error(e)
            return None
        rootA.destroy()
        Sent.callsentfeed()
