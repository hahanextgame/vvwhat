# -*- coding: utf-8 -*-

# @Time :2019/6/5 9:52
# @File: service.py
# @目的


from flask import Blueprint, request, jsonify, make_response
from outlet.view.pull import outs_form
from outlet.view.pull_tag import query_tag

from .import outformat
#outformat = Blueprint('outformat', __name__, template_folder='templates')
from .import cache
import random


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



@outformat.route('/HKBBTVSSK/recommend', methods=['GET'])
def resys_out():
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
    media_id = request.args.get('media_id', '127053')
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
        res = outs_form(media_id, page_size)
        print(res)
        return jsonify(res)
    except Exception as e:
        res = {
            "status": 200,
            "error": "error in request" + str(e)
        }
        return jsonify(res)



@outformat.route('/HKBBTVSSK/recommend/share', methods=['GET'])
#@cache.memoize(timeout=60*5, unless=False, key_prefix='test')
@cache.cached(timeout=60*5, unless=False, key_prefix='test')
def q_tag():
    '''
        视频推荐-首页全屏/列表(新增)
        GET
        :return:
    '''
    print('---')
    video_tag = request.args.get('video_tag')
    video_tag = str(video_tag)

    try:
        res = query_tag(video_tag)
        return jsonify(res)
    except Exception as e:
        res = {
            "status": 200,
            "error": str(e)
        }
        return jsonify(res)



@outformat.route('/')
def tests():
    return 'hi!! this is outlet'