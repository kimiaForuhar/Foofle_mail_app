from SQL import Connection as c


def deletemail(mail_id):
    c.cursor.callproc('deletemail', args=[mail_id, ])
    c.connection.commit()


def readmail(username, mail_id):
    c.cursor.callproc('readmail', args=(username, mail_id))
    c.connection.commit()


def checkcasecade(username):
    c.cursor.callproc('checkcasecade', args=[username, ])
    c.connection.commit()


def getsent(Username):
    global sent
    c.cursor.callproc('getsent', args=[Username, ])
    for result in c.cursor.stored_results():
        sent = result.fetchall()
    c.connection.commit()
    return sent


def getinbox(Username):
    global inbox
    c.cursor.callproc('getinbox', args=[Username, ])
    for result in c.cursor.stored_results():
        inbox = result.fetchall()
    c.connection.commit()
    return inbox


def addtorecivers(username):
    c.cursor.callproc('addtorecivers', args=[username, ])
    c.connection.commit()


def addnewmail(msubject, body, username):
    global newmail
    c.cursor.callproc('addnewmail', args=(msubject, body, username))
    c.connection.commit()


def addNewUser(username, passw, phone, fn, ln, nn, ntid, bd, ph2, addrs):
    c.cursor.callproc('addNewUser', args=(username, passw, phone, fn, ln, nn, ntid, bd, ph2, addrs))
    c.connection.commit()


def DeleteUser(username):
    c.cursor.callproc('DeleteUser', args=[username, ])
    c.connection.commit()


def deletemailforuser(username, mail_id):
    c.cursor.callproc('deletemailforuser', args=(username, mail_id))
    c.connection.commit()


def otherUsersInfo(username):
    c.cursor.callproc('otherUsersInfo', args=[username, ])
    c.connection.commit()


def getInfo(username):
    global info
    c.cursor.callproc('getInfo', args=[username, ])
    for result in c.cursor.stored_results():
        info = result.fetchall()
    c.connection.commit()
    return info


def addInfo(address, firstname, lastname, nickname, phone, nationalityID, birthdate, nid, accountphone, passw):
    c.cursor.callproc('addInfo',
                      args=(address, firstname, lastname, nickname, phone, nationalityID, birthdate, nid, accountphone,
                            passw))
    c.connection.commit()


def AddToLoginTable(username):
    c.cursor.callproc('AddToLoginTable', args=[username, ])
    c.connection.commit()


def Fetchnews(username):
    global news
    c.cursor.callproc('Fetchnews', args=[username, ])
    for result in c.cursor.stored_results():
        news = result.fetchall()
    c.connection.commit()
    return news


def getlastlogin():
    global un
    c.cursor.callproc('getlastlogin')
    for result in c.cursor.stored_results():
        un = result.fetchone()
    c.connection.commit()
    return un[0]


def userscheckpass(Username, passw):
    global password
    c.cursor.callproc('userscheckpass', args=(Username, passw))
    for result in c.cursor.stored_results():
        password = result.fetchone()
    c.connection.commit()
    return password[0]


def deleteNews(id):
    c.cursor.callproc('deleteNews', args=[id, ])
    c.connection.commit()


def permission(username, checkuser):
    global infos
    c.cursor.callproc('permission', args=(username, checkuser))
    for result in c.cursor.stored_results():
        infos = result.fetchone()
    c.connection.commit()
    return infos


def blockinfo(username, blockuser):
    c.cursor.callproc('blockinfo', args=(username, blockuser))
    c.connection.commit()


def permissionnews(username, checkuser):
    c.cursor.callproc('permissionnews', args=(username, checkuser))
    c.connection.commit()


def changepermissionstate(username):
    c.cursor.callproc('changepermissionstate', args=[username, ])
    c.connection.commit()

def getpermitstatus(Username,outp):
    c.cursor.callproc('getpermitstatus', args=(Username,outp ))
    c.connection.commit()
    return outp