from app import app
from flask import request, session
from database import findUser, createUser, userLogin, getUser

@app.route('/web/regist', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    result = findUser(username)
    if result:
        return {
            'errcode': 400,
            'errmsg': '该用户名已被注册'
        }, 400
    
    rowcount = createUser(username, password)
    if rowcount > 0:
        return {
            'errcode': 0,
            'errmsg': '注册成功'
        }, 200
    
    return {
        'errcode': 400,
        'errmsg': '请检查网络或其他设置'
    }, 400

@app.route('/web/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    result = userLogin(username, password)
    
    if result:
        session['user_id'] = result[0]
        uName=getUser(session['user_id'])
        return {
            'errcode': 0,
            'errmsg': '登陆成功',
            'temp':uName
        }, 200
    
    return {
        'errcode': 401,
        'errmsg': '用户不存在或密码错误'
    }, 401
