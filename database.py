from config import db
import mysql.connector
from utils import encrypt, checkPwd

conn = mysql.connector.connect(host=db['host'], user=db['user'], passwd=db['passwd'], 
                                database=db['database'], charset='utf8mb4')
db = conn.cursor()

def findUser(username):
    db.execute('select * from users where `username`=%s', (username,))
    result = db.fetchall()
    return result

def userLogin(username, password):
    db.execute('select * from users where `username`=%s', (username, ))
    result = db.fetchone()
    if result:
        if checkPwd(password, result[2]):
            return result
    return None

def createUser(username, password):
    password = encrypt(password)
    db.execute('insert into users (`username`, `password`) values (%s, %s)', (username, password))
    conn.commit()
    return db.rowcount

def addmessage(topic,comment,user,time):
    db.execute('insert into message (`topic`, `comment`,`user`,`time`) values (%s, %s, %s,%s)', (topic,comment,user,time))
    conn.commit()
    return db.rowcount

def getUser(anId):
    db.execute('select * from users where `id`= %s',(anId,))
    finalGot=db.fetchone()
    return finalGot[1]
def getmessage():
    db.execute('select * from message order by `id` desc ')
    n1=db.fetchall()
    n2=['topic','comment','time']
    data1={}
    for row in n1:
        data1[row[0]]=dict(zip(n2,row[1:]))
    return data1
def deletemessage(anid):
    db.execute('delete from message where `id`=%s',(anid,))
    conn.commit()
    return db.rowcount
def revisemessage(comment,idget):
    db.execute('update message set `comment`=%s where (`id` = %s)',(comment,idget))
    conn.commit()
    return db.rowcount

