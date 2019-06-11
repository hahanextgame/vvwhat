# -*- coding: utf-8 -*-

# @Time :2019/5/28 15:25
# @File: serivce.py
# @目的

import json
from flask import Blueprint, abort, request, jsonify, make_response
from fake.view_control import fake_ct


fakeData = Blueprint('fakeData', __name__, template_folder='templates')


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



@fakeData.route('/HKBBTVSSK/recommend', methods=['GET'])
def fake_some():
    '''
        视频推荐-首页全屏/列表(新增)
        GET
        :return:
    '''
    print('---')
    action = request.args.get('action', 1)
    display = request.args.get('display', 0)
    guid = request.args.get('action', '')
    uid = request.args.get('uid', '')
    media_id = request.args.get('media_id', '')
    plt = request.args.get('plt', 'android')
    widen = request.args.get('widen', 1)
    city = request.args.get('city', '')
    load_cursor = request.args.get('load_cursor', 1)
    longitude = request.args.get('longitude', 48)
    latitude = request.args.get('latitude', 33)
    page_size = request.args.get('page_size', 5)
    country = request.args.get('country', '中国')
    cb = request.args.get('cb', '')
    fmt = request.args.get('fmt', 1)
    refresh_cursor = request.args.get('refresh_cursor', '')
    column_id = request.args.get('column_id', 1)

    page_size = int(page_size)
    print('ct: ', page_size)
    try:
        res = fake_ct(page_size)
        return jsonify(res)
    except Exception as e:
        res = {
            "status": 200,
            "error": str(e)
        }
        return jsonify(res)


@fakeData.route('/')
def tests():
    return 'hi this is '