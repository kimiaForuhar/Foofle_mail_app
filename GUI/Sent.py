from tkinter import *
from tkinter import ttk
from GUI import Inbox, News, NewMail, EditInfo, Scroll
from SQL import Procedures as P


def mynews():
    rootA.destroy()
    News.callnews()


def myinbox():
    rootA.destroy()
    Inbox.callinboxfeed()


def mymail():
    rootA.destroy()
    NewMail.callnewmail()


def myedit():
    rootA.destroy()
    EditInfo.calledit()


def sentfeed():
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
    mainfeed = Frame(rootA, bg='#DBCEEC')
    mainfeed.place(x=200, y=170)
    mainfeed.config(width=200, height=200)
    font = ('times', 40, 'bold')

    scframe = Scroll.VerticalScrolledFrame(mainfeed)
    scframe.grid(row=1, column=0)

    pagetitle = Label(mainfeed, text="Sent mails", bg='#DBCEEC', anchor='nw')
    pagetitle.grid(row=0, column=0)
    # pagetitle.place(x=20, y=0)
    pagetitle.config(font=font)
    # title = Label(mainfeed, text="mailsubject", bg='#DBCEEC', anchor='nw')
    # title.place(x=20, y=80)
    # titlefont = ('times', 15, 'bold')
    # title.config(width=62, height=1, font=titlefont)
    # news = Label(mainfeed, text='this is a mail from me :)', width=90, height=10, anchor='nw')
    # news.place(x=20, y=110)
    newsB = Button(barlayout, text='news', command=mynews)
    newsB.place(x=20, y=30)
    newsB.config(width=15)
    inboxB = Button(barlayout, text='inbox', command=myinbox)
    inboxB.place(x=20, y=70)
    inboxB.config(width=15)
    sentB = Button(barlayout, text='sent')
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
    # add("tmcfkwo cvfwa vopw vopw 1", "n1", scframe.interior)
    # add("t2ufcbwienfinweoin", "n2", scframe.interior)
    # add("t3", "n3", scframe.interior)
    rootA.resizable(0, 1)
    for row in P.getsent(P.getlastlogin()):
        add(row[0],row[1],scframe.interior,row[0])
    rootA.mainloop()


def callsentfeed():
    sentfeed()
    P.getsent(P.getlastlogin())


def add(title, body, canvas,id):
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
    deleteB = Button(emailTitle, text='delete', bg='#DBCEEC',compound=TOP, command=deletemail(id))
    deleteB.place(x=722, y=0)


def deletemail(id):
    P.deletemail(id,P.getlastlogin())
    rootA.update()