# -*- coding: utf-8 -*-

# @Time :2019/6/5 10:01
# @File: test.py
# @目的

import requests
from config.dev import ConfPred

url = 'http://127.0.0.1:5001/pro/orderVideo?media_id=111738'
res_data = requests.get(ConfPred.URL)

top10 = res_data.json()
top10 = list(top10.keys())[:10]

a = ['BODgwMDA0MjE1MzYw', 'BODgwMDA0MTEwODI0', 'BODgwMDA0MjQ5NDQw', 'BODgwMDA0MDI5OTc2', 'BODgwMDA0MTg1NjY0',
     'BODgwMDA0MjU4OTA0', 'BODgwMDAzOTg4MTky', 'BODgwMDA0MjI3ODg4', 'BODgwMDA0MjU1OTY4', 'BODgwMDA0MjQyNjY0']

'''
SELECT video_id, publish_time, play_num, praise_num, comments_num, address, city, city_code
content, country, country_code, cover, creator, district, district_code, iid, imgs, insert_time,
latitude, longitude, 

FROM video_info
WHERE video_id in()
'''

from outlet.model import VideoInfo
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from config.dev import ConfMySQL, ConfPred
import requests

engine = create_engine(ConfMySQL.URL)
DBSession = sessionmaker(bind=engine)
session = DBSession()

res_data = requests.get(ConfPred.URL)
top10 = res_data.json()
top10 = list(top10.keys())[:10]

info_video = session.query(VideoInfo).filter(VideoInfo.video_id.in_(top10)).all()


def list_items(info_video):
    list_items = []
    for i in len(info_video):
        res = {
            "algs": "test",
            "imgs": info_video[i].imgs,
            "cover": info_video[i].cover,
            "title": info_video[i].title,
            "iid": info_video[i].iid,
            "unq_id": info_video[i].unq_id,

            "mid": info_video[i].mid,
            "insert_time": info_video[i].insert_time,
            "type": info_video[i].type,

            "up_count": info_video[i].praise_num,
            "cc_count": info_video[i].comments_num,
            "shareCount": info_video[i].share_count,

            "media_desc": info_video[i].media_desc,
            "media_type": info_video[i].media_type,
            "media_icon": info_video[i].media_icon,
            "media_id": info_video[i].media_id,
            "media_name": info_video[i].media_name,

            "content": info_video[i].content,
            "summary": info_video[i].summary,
            "creator": info_video[i].creator,
            "attention_type": 1,  ########################

            "topic": info_video[i].topic,
            "topType": info_video[i].top_type,

            "inBlacklist": "false",  ########################
            "has_up": "true",  ########################

            "pub_time": info_video[i].publish_time,
            "view_count": info_video[i].play_num,
            "longitude": info_video[i].longitude,
            "latitude": info_video[i].latitude,
            "distance": 999999999999,  ###################

            "city": info_video[i].city,
            "country": info_video[i].country,
            "province": info_video[i].province,
            "district": info_video[i].district,

            "district_code": info_video[i].district_code,
            "province_code": info_video[i].province_code,
            "city_code": info_video[i].city_code,
            "country_code": info_video[i].country_code,
            "address": info_video[i].address,
            "ifBlacklist": "false"  #############################
        }

        for i in res.keys():
            if res[i] == None:
                res[i] = ""

        list_items.append(res)

    return list_items


a = {"code": 0,
     "msg": "success",
     "data": {"req_id": "",
              "alg_group": "",
              "items": [
                {"id": 110000527043,
                 "mid": "BODgwMDA0MjE2MzQ0",
                 "iid": 110000527043,
                 "insert_time": 1557889317124,
                 "source_id": null,
                 "source_url": "BODgwMDA0MjE2MzQ0",
                 "pub_time": 1557889050179,
                 "creator": "",
                 "topic1": null,
                 "topic2": null,
                 "topic3": null,
                 "category": null,
                 "title": "05151057",
                 "summary": "11",
                 "cover": "http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190515/155788931464033190.jpg",
                 "imgs": ["http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190515/155788931464033190.jpg",
                          "http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190515/155788934737283239.jpg"],
                 "content": "{\"url\": \"http://haiwaivideo.src.haiwainet.cn/video/HKBBTVSSK/20190515/155788933655830175.mp4\", \"video_name\": \"0515.mp4\", \"video_width\": 640, \"video_height\": 360, \"video_length\": 219}",
                 "tags": null,
                 "topic": [1000000],
                 "score": null,
                 "video_length": 219,
                 "length": null,
                 "status": null,
                 "copyrightlevel": null,
                 "view_count": 0,
                 "comment_count": 0,
                 "up_count": 0,
                 "down_count": null,
                 "favor_count": null,
                 "share_count": 0,
                 "source_view_count": null,
                 "source_comment_count": null,
                 "source_up_count": null,
                 "source_count_lastdate": null,
                 "last_update": null,
                 "source_type": null,
                 "os_key": null,
                 "has_img": null,
                 "content_type": 2,
                 "item": [100027],
                 "ext": null,
                 "thirdExt": null,
                 "user_id": null,
                 "img_list": null,
                 "view_img_type": null,
                 "review_user_id": null,
                 "unq_id": null,
                 "is_pay": null,
                 "price": null,
                 "sub_category": null,
                 "text_parse_model": null,
                 "show_model": null,
                 "list_model": null,
                 "media_id": 123579,
                 "show_count": null,
                 "beautify_multiple": null,
                 "comment_type": null,
                 "title_tsv": null,
                 "country": null,
                 "country_code": null,
                 "province": null,
                 "province_code": null,
                 "city": null,
                 "city_code": null,
                 "district": null,
                 "district_code": null,
                 "address": null,
                 "latitude": null,
                 "longitude": null,
                 "mediaInfo": {"media_id": 123579,
                               "os_key": null,
                               "name": "01070946",
                               "source_type": 3,
                               "icon": "http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190107/154682550866447903.JPG",
                               "cover": null,
                               "create_time": null,
                               "status": 1,
                               "describe": "1111",
                               "sex": null,
                               "area": null,
                               "birth": null,
                               "email": null,
                               "longitude": null,
                               "latitude": null,
                               "district": null,
                               "country_code": null,
                               "province_code": null,
                               "city_code": null,
                               "district_code": null,
                               "address": null,
                               "country": null,
                               "province": null,
                               "city": null,
                               "user_status": null,
                               "regist_type": null,
                               "attention_type": null,
                               "ext": null},
                 "itemInfo": [
                            {"id": 100027,
                             "os_key": null,
                             "item_name": "新时代",
                             "type": null,
                             "item_order": null,
                             "article_config": null,
                             "video_config": null,
                             "status": null,
                             "item_config": null,
                             "alg_config": null}],
                 "topicInfo": [
                            {"id": 1000000, "os_key": null,
                             "topic_name": null, "desc": null,
                             "icon": null, "create_time": null,
                             "status": null,
                             "ext": null,
                             "topic_category": null,
                             "uid": null,
                             "type": null}],
                 "inBlacklist": 0,
                         "attention_type": 1,
                 "has_up": false}],
              "scene": ""},
     "cost": 32}







tag1 = '新闻频道'
tag2 = '人文'
tag3 = '娱乐'


tag1 = "%" + tag1 + "%"
tag2 = "%" + tag2 + "%"


a = VideoInfo.video_tag.like(tag1)
b = VideoInfo.video_tag.like(tag2)

from sqlalchemy import and_
from sqlalchemy import or_

test = [a,b]

top10 = _generate_top(100)
session.query(VideoInfo).filter(VideoInfo.video_id.in_(top10)).filter(a)
b = session.query(VideoInfo).filter(or_(*test))




input_data ='新闻频道,人文,娱乐'

tag = input_data.split(',')

tag = ["%" + i + "%" for i in tag]

cond = [VideoInfo.video_tag.like(i) for i in tag]
query_like = session.query(VideoInfo).filter(or_(*cond))

if len(query_like) < 6:
    top10 = _generate_top(6)
    query_like = session.query(VideoInfo).filter(VideoInfo.video_id.in_(top10))


query_like = query_like.order_by(VideoInfo.update_time).limit(6)


