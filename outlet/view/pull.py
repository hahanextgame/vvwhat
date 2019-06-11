# -*- coding: utf-8 -*-

# @Time :2019/6/5 9:47
# @File: pull.py
# @目的

import json
import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from config.dev import ConfMySQL
from config.dev import ConfPred

from outlet.model import VideoInfo
from outlet.view.utils import re_hist_es, query_not_dup

from ..import cache

engine = create_engine(ConfMySQL.URLS)
DBSession = sessionmaker(bind=engine)
session = scoped_session(DBSession)




def list_items(info_video, res_data):
    '''
    将查询到的进行转化输出
    :param info_video:
    :return:
    '''
    list_items = []
    for i in range(len(info_video)):

        temp_mid = info_video[i].mid

        if info_video[i].content == None:
            content_temp = {}
        else:
            content_temp = json.loads(info_video[i].content)

        if info_video[i].imgs == None:
            temp_imgs = []
        else:
            temp_imgs = eval(info_video[i].imgs)


        if info_video[i].topic == None:
            temp_topic = []
        else:
            temp_topic = eval(info_video[i].topic)

        try:
            if info_video[i].topic_info == None:
                temp_topic_info = []
            else:
                temp_topic_info = eval(info_video[i].topic_info)
                temp_topic_info = [json.loads(i) for i in temp_topic_info]
        except Exception as e:
            print(i, "topic_info ->>>", info_video[i].topic_info)
            print("----------->>>", i)
            temp_topic_info = []

        try:
            if info_video[i].channel_id == None:
                temp_channel_id = []
            else:
                temp_channel_id = eval(info_video[i].channel_id)
        except Exception as e:
            print(i, "item_id ->>>", info_video[i].channel_id)
            print("----------->>>", i)
            temp_channel_id = []

        try:
            if info_video[i].item_info == None:
                temp_item_info = []
            else:
                temp_item_info = eval(info_video[i].item_info)
                temp_item_info = [json.loads(i) for i in temp_item_info]
        except Exception as e:
            print(i, "item_info ->>>", info_video[i].item_info)
            print("----------->>>", i)
            temp_item_info = []

        res = {"id": info_video[i].iid,
               "mid": info_video[i].mid,
               "iid": info_video[i].iid,
               "insert_time": info_video[i].insert_time,
               "source_id": "",
               "source_url": "",
               "pub_time": info_video[i].publish_time,
               "creator": info_video[i].creator,

               "title": info_video[i].title,
               "summary": info_video[i].summary,
               "cover": info_video[i].cover,
               "imgs": temp_imgs,

               "content": content_temp,
               "topic": temp_topic,
               "video_length": info_video[i].video_time,

               "status": "",
               "view_count": info_video[i].play_num,
               "comment_count": info_video[i].comments_num,
               "up_count": info_video[i].praise_num,
               "down_count": "",
               "favor_count": "",
               "share_count": info_video[i].share_count,
               "source_view_count": "",
               "source_comment_count": "",
               "source_up_count": "",
               "source_count_lastdate": "",
               "last_update": info_video[i].update_time,
               "source_type": "",
               "os_key": "",
               "has_img": "",
               "content_type": info_video[i].type,
               "item": temp_channel_id,
               "ext": {},
               "user_id": "",

               "view_img_type": "",
               "review_user_id": "",
               "unq_id": info_video[i].unq_id,
               "media_id": info_video[i].media_id,
               "show_count": info_video[i].play_num,
               "country": info_video[i].country,
               "country_code": info_video[i].country_code,
               "province": info_video[i].province,
               "province_code": info_video[i].province_code,
               "city": info_video[i].city,
               "city_code": info_video[i].city_code,
               "district": info_video[i].district,
               "district_code": info_video[i].district_code,
               "address": info_video[i].address,
               "latitude": info_video[i].latitude,
               "longitude": info_video[i].longitude,
               "mediaInfo": {"media_id": info_video[i].media_id,
                             "os_key": "",
                             "name": info_video[i].media_name,
                             "source_type": info_video[i].media_type,
                             "icon": info_video[i].media_icon,
                             "cover": info_video[i].cover,
                             "describe": info_video[i].media_desc,
                             "longitude": info_video[i].longitude,
                             "latitude": info_video[i].latitude,
                             "district": info_video[i].district,
                             "country_code": info_video[i].country_code,
                             "province_code": info_video[i].province_code,
                             "city_code": info_video[i].city_code,
                             "district_code": info_video[i].district_code,
                             "address": info_video[i].address,

                             "country": info_video[i].country,
                             "province": info_video[i].province,
                             "city": info_video[i].city},
               "itemInfo": temp_item_info,
               "topicInfo": temp_topic_info,

               "inBlacklist": res_data[temp_mid].get('inBlacklist'),
               "collect_type":res_data[temp_mid].get('collect_type'),
               "attention_type": res_data[temp_mid].get('attention_type'),
               "has_up": res_data[temp_mid].get('has_up')}

        for i in res.keys():
            try:
                if res[i] == None:
                    res[i] = ""
                if i == "mediaInfo":
                    for j in res[i].keys():
                        if res[i][j] == None:
                            res[i][j] = ""
            except Exception as e:
                print(e)
                pass

        list_items.append(res)

    return list_items


@cache.memoize(timeout=60)
def outs_form(media_id="127053", nums=10):
    '''
        :param nums: 这里默认了前10个
        :return:
    '''
    top10 = query_not_dup(media_id, nums)
    print(top10)
    re_hist_es(media_id, top10)
    try:
        post_data = {i: "" for i in top10}
        reurl = ConfPred.inblack_query + str(media_id)
        black_info = requests.post(reurl, json=post_data)

        print('bbbb')
        black_info = black_info.json()
        res_data = black_info['data']
        print("-----")
    except Exception as e:
        print('error in reurl', e)
        ones = {
            "code": 404,
            "msg": "error in query black list" + str(e)
        }
        return ones


    try:
        info_video = session.query(VideoInfo).filter(VideoInfo.video_id.in_(top10)).all()
        items = list_items(info_video, res_data)
        session.commit()
        ones = {"code": 0,
                "msg": "success",
                "data": {"req_id": "",
                         "alg_group": "test",
                         "items": items,
                         "scene": "up_feed"},
                "cost": 10}
        return ones

    except Exception as e:
        session.rollback()
        ones = {
            "code": 404,
            "msg": "error in outs_form" + str(e)
        }
        return ones
