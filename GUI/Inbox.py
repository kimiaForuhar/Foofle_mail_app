from tkinter import *
from tkinter import ttk
from GUI import Sent, NewMail, EditInfo, Scroll, News
from SQL import Procedures as P


def mynews():
    rootA.destroy()
    News.callnews()


def mysent():
    rootA.destroy()
    Sent.callsentfeed()


def mymail():
    rootA.destroy()
    NewMail.callnewmail()


def myedit():
    rootA.destroy()
    EditInfo.calledit()


def inboxfeed():
    global rootA
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
    mainfeed = Frame(rootA, width=1500, height=800, bg='#DBCEEC')
    mainfeed.place(x=200, y=170)
    scframe = Scroll.VerticalScrolledFrame(mainfeed)
    scframe.grid(row=1, column=0)
    font = ('times', 40, 'bold')
    pagetitle = Label(mainfeed, text="inbox", bg='#DBCEEC', anchor='nw')
    pagetitle.grid(row=0, column=0)
    pagetitle.config(font=font)
    newsB = Button(barlayout, text='news', command=mynews)
    newsB.place(x=20, y=30)
    newsB.config(width=15)
    inboxB = Button(barlayout, text='inbox')
    inboxB.place(x=20, y=70)
    inboxB.config(width=15)
    sentB = Button(barlayout, text='sent', command=mysent)
    sentB.place(x=20, y=110)
    sentB.config(width=15)
    editB = Button(barlayout, text='edit info', command=myedit)
    editB.place(x=20, y=580)
    editB.config(width=15)
    new_mailB = Button(barlayout, text='new mail', command=mymail)
    new_mailB.place(x=20, y=540)
    new_mailB.config(width=15)
    user = Label(rootA, text="logged in as", bg='#DBCEEC')
    user.place(x=410, y=140)
    usern = Label(rootA, text=P.getlastlogin(), bg='#DBCEEC')
    usern.place(x=477, y=140)
    # add("tmcfkwo cvfwa vopw vopw 1", "n1", scframe.interior, 1)
    rootA.resizable(0, 1)
    for row in P.getinbox(P.getlastlogin()):
        add(row[1], row[2], scframe.interior, row[0])
    rootA.mainloop()


def callinboxfeed():
    inboxfeed()


def add(title, body, canvas, id):
    emailPad = Canvas(canvas, bg="black", relief=FLAT)
    emailPad.pack(pady=15, side=TOP, fill="both")
    emailPad.config()
    emailTitle = ttk.Label(emailPad, text=title, background="#DBCEEC")
    emailTitle.pack(padx=10, pady=5, side=TOP, fill="x")
    emailContent = Text(emailPad, background="#DBCEEC")
    emailContent.pack(padx=10, pady=5, side=TOP, fill="x")
    emailContent.config(height=3, wrap='word')
    emailContent.insert('1.0', body)
    emailContent.config(state='disabled')
    deleteB = Button(emailTitle, text='delete', bg='#DBCEEC', command=lambda: deletemail(id))
    deleteB.place(x=722, y=0)
    status = Label(emailTitle, text=P.getinbox(P.getlastlogin()))
    status.place(x=690)
    status.config(width=2)
    readB = Button(emailTitle, text='mark as read', bg='#DBCEEC', command=P.readmail(P.getlastlogin(), id))
    readB.place(x=600)
    emailTitle.update()


def deletemail(id):
    P.deletemail(id)
    rootA.after(10,inboxfeed)
