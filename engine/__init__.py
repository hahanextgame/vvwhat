# -*- coding: utf-8 -*-

# @Time :2019/6/4 15:21
# @File: __init__.py.py
# @目的
from flask import Flask
from flask import Blueprint

from flask_caching import Cache
from config.dev import ConfRedis


app = Flask(__name__)


predictor = Blueprint('predictor', __name__)
# cache = Cache.init_app(predictor, ConfRedis)

cache = Cache(app, config=ConfRedis)

