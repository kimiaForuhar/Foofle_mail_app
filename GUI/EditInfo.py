from tkinter import *
from tkinter import ttk
from GUI import Inbox, Sent, NewMail, News,OthersInfo
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


def mynews():
    rootA.destroy()
    News.callnews()


def editfeed():
    global rootA, firste, lastnamee, nick, n_ide, passe, birthdatee, phonee, cphonee, addresse, search
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
    first_name = Label(mainfeed, text="first name:", bg='#DBCEEC')
    first_name.place(x=20, y=20)
    first_name.config(font=myfont)
    firste = Entry(mainfeed, width=50)
    firste.place(x=180, y=20)
    lastname = Label(mainfeed, text="last name:", bg='#DBCEEC')
    lastname.place(x=20, y=60)
    lastname.config(font=myfont)
    lastnamee = Entry(mainfeed, width=50)
    lastnamee.place(x=180, y=60)
    nickname = Label(mainfeed, text="nick name:", bg='#DBCEEC')
    nickname.place(x=20, y=100)
    nickname.config(font=myfont)
    nick = Entry(mainfeed, width=50)
    nick.place(x=180, y=100)
    n_id = Label(mainfeed, text="nationality id:", bg='#DBCEEC')
    n_id.place(x=20, y=140)
    n_id.config(font=myfont)
    n_ide = Entry(mainfeed, width=50)
    n_ide.place(x=180, y=140)
    passw = Label(mainfeed, text="password:", bg='#DBCEEC')
    passw.place(x=20, y=200)
    passw.config(font=myfont)
    passe = Entry(mainfeed, width=50)
    passe.place(x=180, y=200)
    birthdate = Label(mainfeed, text="birth date:", bg='#DBCEEC')
    birthdate.place(x=20, y=240)
    birthdate.config(font=myfont)
    birthdatee = Entry(mainfeed, width=50)
    birthdatee.place(x=180, y=240)
    phone = Label(mainfeed, text="phone:", bg='#DBCEEC')
    phone.place(x=20, y=320)
    phone.config(font=myfont)
    phonee = Entry(mainfeed, width=50)
    phonee.place(x=180, y=320)
    cphone = Label(mainfeed, text="connected phone:", bg='#DBCEEC')
    cphone.place(x=20, y=280)
    cphonee = Entry(mainfeed, width=50)
    cphonee.place(x=180, y=280)
    cphone.config(font=myfont)
    address = Label(mainfeed, text="address:", bg='#DBCEEC')
    address.place(x=20, y=360)
    address.config(font=myfont)
    addresse = Text(mainfeed, width=58, height=5)
    addresse.place(x=20, y=390)
    save = Button(mainfeed, text='save', width=10, command=getinput)
    save.place(x=300, y=500)
    deletB = Button(mainfeed, text='delete account', width=10, command=deleteuder)
    deletB.place(x=200, y=500)
    newsB = Button(barlayout, text='news', command=mynews)
    newsB.place(x=20, y=30)
    newsB.config(width=15)
    inboxB = Button(barlayout, text='inbox', command=myinbox)
    inboxB.place(x=20, y=70)
    inboxB.config(width=15)
    sentB = Button(barlayout, text='sent', command=mysent)
    sentB.place(x=20, y=110)
    sentB.config(width=15)
    editB = Button(barlayout, text='edit info')
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
    searchl = Label(titlelayout, text='search here', bg='#D0CAEE')
    searchl.place(x=20, y=140)
    searchl.config(font=myfont)
    search = ttk.Entry(titlelayout, width=30)
    search.place(x=150, y=140)
    search.bind("<Return>",(lambda event: searchCommadn(search.get())))

    infos = P.getInfo(P.getlastlogin())
    print(infos)

    if infos[0][5] != None:
        firste.insert(0, infos[0][5])
    if infos[0][6] != None:
        lastnamee.insert(0, infos[0][6])
    if infos[0][7] != None:
        nick.insert(0, infos[0][7])
    if infos[0][8] != None:
        phonee.insert(0, infos[0][8])
    if infos[0][3] != None:
        cphonee.insert(0, infos[0][3])
    if infos[0][4] != None:
        addresse.insert("1.0", infos[0][4])
    if infos[0][2] != None:
        birthdatee.insert(0,infos[0][2])

    rootA.mainloop()

def searchCommadn(username):
    #inja proco farakhoni kon va maghadire morede niazo bede be tabe
    OthersInfo.editfeed(username, "kim", "foroh", "kimy", "002", "2000-0-9", "0922", "0921", "tehran")



def calledit():
    editfeed()
    # in kar dare


def getinput():
    fnaem = firste.get()
    lname = lastnamee.get()
    nname = nick.get()
    id = P.getlastlogin()
    # id="msaeed"
    # passw = passe.get()
    passw = '123456'
    bd = birthdatee.get()
    phone = phonee.get()
    cphone = cphonee.get()
    address = addresse.get("1.0", END)
    # searchothers = search.get()
    P.addInfo(address, fnaem, lname, nname, phone, bd, id, cphone, passw)


def deleteuder():
    P.DeleteUser(P.getlastlogin())
