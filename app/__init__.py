from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_login import LoginManager
from flask_pagedown import PageDown
from flaskext.markdown import Markdown

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'index'
bootstrap = Bootstrap(app)
manager = Manager(app)
pagedown = PageDown(app)
md = Markdown(app)

from app import models, views, admin_views
from admin_views import admin
admin.init_app(app)
