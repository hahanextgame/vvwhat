# -*- coding: utf-8 -*-

# @Time :2019/6/5 10:51
# @File: Api_outlet.py
# @目的

# from flask import Flask
# from flask_cors import CORS

from outlet.service import outformat
from outlet import app


@app.route('/')
# @cache.cached()
def hello_world():
    return 'Hello World!'


app.register_blueprint(outformat, url_prefix='/rec')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=False)