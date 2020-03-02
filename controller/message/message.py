from app import app
from flask import request, session
from database import addmessage, getmessage, deletemessage, revisemessage
import datetime

@app.route('/web/send', methods=['POST'])
def sendmessage():
    data = request.get_json()
    topic = data['topic']
    comment = data['comment']
    user=data['user']
    time=datetime.datetime.now()
    rowcount=addmessage(topic,comment,user,time)
    if(rowcount>0):
        return {
            'errcode': 0,
            'errmsg': '留言成功'
        }
    return {
        'errcode':400,
        'errmsg':'留言失败，请检查网络或其他配置'
    }
@app.route('/web/get', methods=['POST'])
def getdata():
    data1=getmessage();
    return data1;
@app.route('/web/delete',methods=['POST'])
def delete():
    ID=request.get_json()
    anid=ID['id']
    rowcount=deletemessage(anid)
    if (rowcount>0):
        return{'errmsg':'删除成功'}
    return{'errmsg':'删除失败，请检查网络或其他配置'}
@app.route('/web/revise',methods=['POST'])
def revise():
    datasec=request.get_json()
    anidsec=datasec['id']
    comment=datasec['comment']
    rowcount=revisemessage(comment,anidsec)
    if (rowcount>0):
        return{'errmsg':'修改成功'}
    elif(rowcount==-1):
        return{'errmsg':'修改失败，该留言已被删除'}
    return{'errmsg':'修改失败，请检查网络或其他配置'}


