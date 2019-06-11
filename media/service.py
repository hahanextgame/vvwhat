# -*- coding: utf-8 -*-

# @Time :2019/6/5 9:52
# @File: service.py
# @目的


import json
from flask import Blueprint, abort, request, jsonify, make_response

from media.pull import pull_list


media = Blueprint('media', __name__, template_folder='templates')


def cros(dicts):
    '''
    处理跨域请求
    :param dicts:
    :return:
    '''
    json_data = jsonify(dicts)
    res = make_response(json_data)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST,PUT,DELETE'
    res.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return res



@media.route('/HKBBTVSSK/media/recommend', methods=['GET'])
def fake_some():
    '''
        视频推荐-首页全屏/列表(新增)
        GET
        :return:
    '''
    print('---')

    page_size = request.args.get('page_size', 5)

    page_size = int(page_size)
    print('ct: ', page_size)
    try:
        res = pull_list()
        return jsonify(res)
    except Exception as e:
        res = {
            "status": 200,
            "error": str(e)
        }
        return jsonify(res)


@media.route('/')
def tests():
    return 'hi!! this is media'