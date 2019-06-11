# -*- coding: utf-8 -*-

# @Time :2019/6/5 9:09
# @File: service.py
# @目的

from engine.start import order_video
import json
from flask import Blueprint, request, jsonify, make_response

# predictor = Blueprint('predictor', __name__, template_folder='templates')
# cache = Cache.init_app(predictor, ConfRedis)
from .import predictor
from .import cache


@predictor.route('/orderVideo', methods=['GET'])
def orderVideo():
    '''
        视频推荐-首页全屏/列表(新增)
        GET
        :return:
    '''

    media_id = request.args.get('media_id', "111738")
    media_id = str(media_id)

    try:
        res = order_video(media_id)
        out_form = dict(res)
        print(out_form)
        return json.dumps(out_form)
    except Exception as e:
        res = {
            "status": 404,
            "error": "error in orderVideo" + str(e)
        }
        return jsonify(res)


@predictor.route('/')
def tests():
    return 'hi! this is predictor'

