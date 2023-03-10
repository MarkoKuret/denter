#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from tempfile import mkdtemp
from flask_login import LoginManager
#import locale
#from flask_mail import Mail


# konfiguracije aplikacije
app = Flask(__name__)
app.config["SECRET_KEY"] = "EsX5Cls1GiistLq6"
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] =  'sqlite:///denter.db'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'prijava'
login_manager.login_message_category = 'lose'

app.app_context().push()

# konfiguracija sessiona
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#app.config["SESSION_FILE_DIR"] = mkdtemp()
#Session(app)

#lokalizacija (za datume na hr)
#locale.setlocale(locale.LC_ALL, "hr_HR.UTF-8")


#konfiguracija email servera
"""
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'dirmreza@gmail.com'
app.config['MAIL_PASSWORD'] = 'supertajna'
mail = Mail(app)
"""

#import svih ruta (i funkcija)
from denter import rute