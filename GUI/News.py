from tkinter import *
from tkinter import ttk
from GUI import Inbox, Sent, NewMail, EditInfo, Scroll
from SQL import Procedures as P


def myinbox():
    rootA.destroy()
    Inbox.callinboxfeed()


def mysent():
    rootA.destroy()
    Sent.callsentfeed()


def mymail():
    rootA.destroy()
    NewMail.callnewmail()


def myedit():
    rootA.destroy()
    EditInfo.calledit()


def newsfeed():
    global rootA
    global mainfeed
    labelfont = ('elephant italic', 70, 'bold')
    rootA = Tk()
    rootA.configure(bg='#D0CAEE')
    rootA.geometry("1000x1500")
    rootA.title('Foofle')
    titlelayout = Frame(rootA, width=500, height=170, bg='#D0CAEE')
    titlelayout.place(x=0, y=0)
    barlayout = Frame(rootA, width=200, height=1500, bg='#EECAE6')
    barlayout.place(x=0, y=170, width=200, height=1000)
    intruction = Label(rootA, text='foofle\n', bg='#D0CAEE')
    intruction.place(x=400, y=20)
    intruction.config(font=labelfont)

    mainfeed = Frame(rootA, width=1500, height=800, bg='#DBCEEC')
    mainfeed.place(x=200, y=170)

    scframe = Scroll.VerticalScrolledFrame(mainfeed)
    scframe.grid(row=1, column=0)

    font = ('times', 40, 'bold')
    pagetitle = Label(mainfeed, text="news", bg='#DBCEEC', anchor='nw')
    pagetitle.grid(row=0, column=0)
    pagetitle.config(font=font)
    newsB = Button(barlayout, text='news')
    newsB.place(x=20, y=30)
    newsB.config(width=15)
    inboxB = Button(barlayout, text='inbox', command=myinbox)
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
    name = P.getlastlogin()
    usern = Label(rootA, text=name, bg='#DBCEEC')
    usern.place(x=477, y=140)
    rootA.resizable(0, 1)
    for row in P.Fetchnews(name):
        add(row[0], row[1], scframe.interior)
    rootA.mainloop()


def callnews():
    newsfeed()


def add(title, body, canvas):
    newsPad = Canvas(canvas, bg="black", relief=FLAT)
    newsPad.pack(pady=15, side=TOP, fill="both")
    newsPad.config()
    newsTitle = ttk.Label(newsPad, text=title, background="#DBCEEC")
    newsTitle.pack(padx=10, pady=5, side=TOP, fill="x")
    newsContent = Text(newsPad, background="#DBCEEC")
    newsContent.pack(padx=10, pady=5, side=TOP, fill="x")
    newsContent.config(height=3, wrap='word')
    newsContent.insert('1.0', body)
    newsContent.config(state='disabled')
    if title == 'ask for permission':
        exp = Button(newsPad, text='add to exceptions', command=P.blockinfo(EditInfo.getinput, P.getlastlogin()))
