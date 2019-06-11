# -*- coding: utf-8 -*-

# @Time :2019/6/5 9:14
# @File: Api_Pro.py
# @目的


from flask_cors import CORS
from engine import app
from engine.service import predictor
CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    return 'Hello World!'

app.register_blueprint(predictor, url_prefix='/pro')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)