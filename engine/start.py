# -*- coding: utf-8 -*-

# @Time :2019/6/5 8:55
# @File: start.py
# @目的

from engine.db import pull_mysql
from engine.pretreat import pred_prob
from .import cache


@cache.memoize(timeout=60)
def order_video(media_id):
    '''
    media_id = "111738"
    :param media_id:
    :return:
    '''
    media_id = str(media_id)
    try:
        get_data = pull_mysql(media_id)

        res = pred_prob(get_data)
        return res
    except Exception as e:
        return {
            "message": "error in order_video!!! " + e,
            "data" : get_data,
            "code": 404
        }


