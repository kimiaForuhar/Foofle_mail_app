from tkinter import *
from tkinter import ttk
from GUI import Inbox, Sent, NewMail, News
from SQL import Procedures as P


def editfeed(username, firstName, lastName, nickName, national_id, birthday, phonePersonal, PhoneSystem, addressVorodi):

    global rootA, firste, lastnamee, nick, n_ide, nationalId, birthdatee, phonee, cphonee, addresse, search
    labelfont = ('elephant italic', 50, 'bold')

    rootA = Tk()
    rootA.configure(bg='#D0CAEE')
    rootA.geometry("660x600")
    rootA.title(username)

    titlelayout = Frame(rootA, width=500, height=100, bg='#D0CAEE')
    titlelayout.place(x=0, y=0)
    # barlayout = Frame(rootA, width=200, height=1500, bg='#EECAE6')
    # barlayout.grid(row=0, column=0, padx=0, pady=170)
    intruction = Label(rootA, text=username, bg='#D0CAEE')
    intruction.place(x=50, y=10)
    intruction.config(font=labelfont)

    mainfeed = Label(rootA, bg='#DBCEEC')
    mainfeed.place(x=50, y=120)
    mainfeed.config(width=80, height=30)
    myfont = ('times', 15, 'bold')

    first_name = Label(mainfeed, text="first name:", bg='#DBCEEC')
    first_name.place(x=20, y=20)
    first_name.config(font=myfont)

    firste = Entry(mainfeed, width=50)
    firste.place(x=180, y=20)
    firste.insert(0, firstName)

    lastname = Label(mainfeed, text="last name:", bg='#DBCEEC')
    lastname.place(x=20, y=60)
    lastname.config(font=myfont)

    lastnamee = Entry(mainfeed, width=50)
    lastnamee.place(x=180, y=60)
    lastnamee.insert(0, lastName)

    nickname = Label(mainfeed, text="nick name:", bg='#DBCEEC')
    nickname.place(x=20, y=100)
    nickname.config(font=myfont)

    nick = Entry(mainfeed, width=50)
    nick.place(x=180, y=100)
    nick.insert(0, nickName)

    n_id = Label(mainfeed, text="nationality id:", bg='#DBCEEC')
    n_id.place(x=20, y=140)
    n_id.config(font=myfont)

    n_ide = Entry(mainfeed, width=50)
    n_ide.place(x=180, y=140)
    n_ide.insert(0, national_id)

    birthdate = Label(mainfeed, text="birth date:", bg='#DBCEEC')
    birthdate.place(x=20, y=180)
    birthdate.config(font=myfont)

    birthdatee = Entry(mainfeed, width=50)
    birthdatee.place(x=180, y=180)
    birthdatee.insert(0, birthday)

    phone = Label(mainfeed, text="phone:", bg='#DBCEEC')
    phone.place(x=20, y=260)
    phone.config(font=myfont)

    phonee = Entry(mainfeed, width=50)
    phonee.place(x=180, y=260)
    phonee.insert(0, phonePersonal)

    cphone = Label(mainfeed, text="connected phone:", bg='#DBCEEC')
    cphone.place(x=20, y=220)
    cphone.config(font=myfont)

    cphonee = Entry(mainfeed, width=50)
    cphonee.place(x=180, y=220)
    cphonee.insert(0, PhoneSystem)

    address = Label(mainfeed, text="address:", bg='#DBCEEC')
    address.place(x=20, y=300)
    address.config(font=myfont)
    addresse = Text(mainfeed, width=58, height=5)
    addresse.place(x=20, y=330)
    addresse.insert("1.0", addressVorodi)

    firste["state"] = "disabled"
    lastnamee["state"] = "readonly"
    nick["state"] = "readonly"
    n_ide["state"] = "readonly"
    birthdatee["state"] = "readonly"
    phonee["state"] = "readonly"
    cphonee["state"] = "readonly"
    addresse["state"] = "disabled"
    addresse.config(bg="gray93")

    rootA.mainloop()



