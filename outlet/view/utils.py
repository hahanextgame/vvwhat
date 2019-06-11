# -*- coding: utf-8 -*-

# @Time :2019/6/11 8:48
# @File: utils.py
# @目的
import datetime
import json
import requests
import random


from elasticsearch import Elasticsearch
from itertools import chain

from config.dev import ConfEs
from config.dev import ConfPred


def generate_top(media_id, nums=10):
    '''
        查询推荐的10个
    :param nums:
    :return:
    '''
    try:
        data = {
            "media_id": media_id
        }
        res_data = requests.get(ConfPred.URL, params=data)
        top10 = res_data.json()
        top10 = list(top10.keys())[:nums]
        return top10
    except Exception as e:
        print("error in generate_top", e)
        return []




def re_hist_es(media_id, top_num, es_index='video_re_hist',
               es_type='htmlbean', scene="up_feed"):
    '''
        推荐结果存入数据
    :param media_id: media_id = "123134"
    :param top10: top_num = []
    :param es_index:
    :param es_type:
    :param scene:
    :return:
    '''
    es = Elasticsearch(ConfEs.IP, port=ConfEs.PORT)
    now = datetime.datetime.now()
    now = str(now)[:19]
    now_time = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    ids = str(media_id) + "_" + str(now_time)
    media_id = str(media_id)

    es_body = {
        "media_id": media_id,
        "createTime": now,
        "mid": top_num,
        "scene": scene
    }
    try:
        es.index(index=es_index, doc_type=es_type, id=ids, body=json.dumps(es_body))
    except Exception as e:
        print('error in re_hist_es!!', e)
        pass


def query_hist_es(media_id, size=50, es_index='video_re_hist'):
    '''
        取出最新的50个推荐历史
    :param media_id:
    :param size:
    :param es_index:
    :return:
    '''
    es = Elasticsearch(ConfEs.IP, port=ConfEs.PORT)

    q = {
        "query": {
            "bool": {"must": [
                {"term": {
                    "media_id": {
                        "value": str(media_id)
                    }
                }}
            ]}
        }
        , "size": size
        , "sort": [
            {
                "createTime.keyword": {
                    "order": "desc"
                }
            }
        ]
    }

    try:
        res = es.search(index=es_index, body=json.dumps(q))
        data_source = res['hits']['hits']

        mid = [i['_source']['mid'] for i in data_source]

        mid = list(chain.from_iterable(mid))
        return mid

    except Exception as e:
        print('error in query_hist_es', e)
        return []





def query_not_dup(media_id, nums):
    '''
    media_id = 123134
    :param media_id:
    :return:
    '''
    print('media_id', media_id)
    top_nums = generate_top(media_id, nums=1000)

    hist_nums = query_hist_es(media_id)

    print('top_nums ->>>', top_nums)
    print('hist_nums ->>>>', hist_nums)

    not_dup = [i for i in top_nums if i not in hist_nums]
    print('not_dup ->>>>', not_dup)
    if not_dup == [] or 'error' in hist_nums:
        not_dup = random.sample(top_nums, nums)

    out_nums = not_dup[:nums]

    return out_nums