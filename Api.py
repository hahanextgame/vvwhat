# -*- coding: utf-8 -*-

# @Time :2019/5/28 15:26
# @File: Api.py
# @目的

from flask import Flask
from flask_cors import CORS

from fake.serivce import fakeData

app = Flask(__name__, static_folder='static')

CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    return 'Hello World!'


app.register_blueprint(fakeData, url_prefix='/rec')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
