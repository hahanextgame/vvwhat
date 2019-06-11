# -*- coding: utf-8 -*-

# @Time :2019/6/5 9:47
# @File: __init__.py.py
# @目的


from flask import Blueprint
from flask import Flask

from flask_caching import Cache
from config.dev import ConfRedis


# app = Flask("test")
app = Flask(__name__)

outformat = Blueprint('outformat', __name__)

cache = Cache(app, config=ConfRedis)



# app.register_blueprint(media, url_prefix='/media')