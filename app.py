# app.py
from flask import Flask
import mysql.connector
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.app['secret_key']
from controller.user.user import *
from controller.message.message import *

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9990)
