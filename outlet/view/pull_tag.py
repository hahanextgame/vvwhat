# -*- coding: utf-8 -*-

# @Time :2019/6/10 9:48
# @File: pull_tag.py
# @目的

import json
import requests

from sqlalchemy import create_engine
from sqlalchemy import or_, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from config.dev import ConfMySQL
from config.dev import ConfPred
from outlet.model import VideoInfo

from outlet.view.utils import generate_top


engine = create_engine(ConfMySQL.URLS)
DBSession = sessionmaker(bind=engine)
session = scoped_session(DBSession)


def _generate_top(nums=10):
    res_data = requests.get(ConfPred.URL)
    top10 = res_data.json()
    top10 = list(top10.keys())[:nums]
    return top10



def list_items_share(info_video):
    '''
    将查询到的进行转化输出
    :param info_video:
    :return:
    '''
    list_items = []
    for i in range(len(info_video)):

        if info_video[i].content == None:
            content_temp = {}
        else:
            content_temp = eval(info_video[i].content)


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
        except Exception as e:
            print(i, " error！！ topic_info ->>>", info_video[i].topic_info)
            temp_topic_info = []

        try:
            if info_video[i].channel_id == None:
                temp_channel_id = []
            else:
                temp_channel_id = eval(info_video[i].channel_id)
        except Exception as e:
            print(i, " error！！ item_id ->>>", info_video[i].channel_id)
            temp_channel_id = []


        try:
            if info_video[i].video_tag == None:
                temp_video_tag = []
            else:
                temp_video_tag = eval(info_video[i].video_tag)
        except Exception as e:
            print(i, " error！！ video_tag ->>>", info_video[i].video_tag)
            temp_channel_id = []



        if info_video[i].item_info == None:
            temp_item_info = []
        else:
            temp_item_info = eval(info_video[i].item_info)


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
               "has_img": "",  #########################
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
               "video_tag": temp_video_tag
               }

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




def query_tag(input_data):
    '''

    :param input_data:
    :return:
    '''
    if isinstance(input_data, str) == False:
        return {
            "code": 404,
            "message": "please input the right format"
        }

    tag = input_data.split(',')
    tag = ["%" + i + "%" for i in tag]

    cond = [VideoInfo.channel_id.like(i) for i in tag]

    # 没有input_data的时候进行随机取数据
    try:
        query_like = session.query(VideoInfo).filter(or_(*cond))
        query_like = query_like.order_by(VideoInfo.play_num).limit(6).all()

        lens = len(query_like)
        if lens < 6:
            fill_loss = _generate_top(6 - lens)
            temp = session.query(VideoInfo).filter(VideoInfo.video_id.in_(fill_loss))
            query_like.extend(temp.all())

        items = list_items_share(query_like)
        session.commit()

        ones = {"code": 200,
                "msg": "success",
                "data": {"alg_group": "test",
                         "items": items,
                         "scene": "share"},
                "cost": 10}
        return ones

    except Exception as e:
        session.rollback()
        ones = {
            "code": 404,
            "msg": e
        }
        return ones