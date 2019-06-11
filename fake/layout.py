# -*- coding: utf-8 -*-

# @Time :2019/5/28 15:22
# @File: layout.py
# @目的: 存放假的数据相关的格式

'''
    主要是输出的相关格式
'''

from fake.house import fake_all
import random
from fake.db import query_one

def get_only_one():
    try:
        q_one = query_one()

        res = {
            "algs": random.choices(fake_all.get('strings'))[0],
            "imgs": random.choices(fake_all.get('imgs'))[0],
            "cover": random.choices(fake_all.get('cover'))[0],
            "title": q_one.get("video_title"),  # video_title
            "iid": random.choices(fake_all.get('iid'))[0],
            "unq_id": random.choices(fake_all.get('iid'))[0],

            "mid": q_one.get("video_id"),  # video_id
            "insert_time": random.choices(fake_all.get('insert_time'))[0],
            "type": random.choices(fake_all.get('type'))[0],

            "up_count": q_one.get('praise_num'),
            "cc_count": random.choices(fake_all.get('big_int_random'))[0],
            "shareCount": random.choices(fake_all.get('small_int_random'))[0],

            "media_desc": random.choices(fake_all.get('media_desc'))[0],
            "media_type": int(q_one.get('media_type')),
            "media_icon": random.choices(fake_all.get('cover'))[0],
            "media_id": q_one.get('media_id'),
            "media_name": q_one.get('media_name'),  # media_name

            "content": random.choices(fake_all.get('content'))[0],
            "summary": random.choices(fake_all.get('summary'))[0],
            "creator": random.choices(fake_all.get('creator'))[0],
            "attention_type": random.choices(fake_all.get('type'))[0],

            "topic": random.choices(fake_all.get('topic'))[0],
            "topType": random.choices(fake_all.get('type'))[0],

            "inBlacklist": random.choices(fake_all.get('twotype'))[0],
            "has_up": random.choices(fake_all.get('bol'))[0],

            "pub_time": q_one.get('publish_time'),
            "view_count": q_one.get('play_num'),
            "longitude": random.choices(fake_all.get('small_float'))[0],
            "latitude": random.choices(fake_all.get('small_float'))[0],
            "distance": random.choices(fake_all.get('big_float'))[0],

            "city": q_one.get('city'),
            "country": q_one.get('country'),
            "province": q_one.get('province'),
            "district": random.choices(fake_all.get('district'))[0],

            "district_code": random.choices(fake_all.get('city_code'))[0],
            "province_code": random.choices(fake_all.get('city_code'))[0],
            "city_code": random.choices(fake_all.get('city_code'))[0],
            "country_code": random.choices(fake_all.get('city_code'))[0],
            "address": random.choices(fake_all.get('address'))[0],
            "ifBlacklist": random.choices(fake_all.get('bol'))[0]
        }
        return res

    except Exception as e:

        res = {
            "algs": random.choices(fake_all.get('strings'))[0],
            "imgs": random.choices(fake_all.get('imgs'))[0],
            "cover": random.choices(fake_all.get('cover'))[0],
            "title": random.choices(fake_all.get('title'))[0],                # video_title
            "iid": random.choices(fake_all.get('iid'))[0],
            "unq_id": random.choices(fake_all.get('iid'))[0],

            "mid": random.choices(fake_all.get('mid'))[0],                     # video_id
            "insert_time": random.choices(fake_all.get('insert_time'))[0],
            "type": random.choices(fake_all.get('type'))[0],

            "up_count": random.choices(fake_all.get('small_int_random'))[0],
            "cc_count": random.choices(fake_all.get('big_int_random'))[0],
            "shareCount": random.choices(fake_all.get('small_int_random'))[0],

            "media_desc": random.choices(fake_all.get('media_desc'))[0],
            "media_type": random.choices(fake_all.get('type'))[0],
            "media_icon": random.choices(fake_all.get('cover'))[0],
            "media_id": random.choices(fake_all.get('media_id'))[0],
            "media_name": random.choices(fake_all.get('media_name'))[0],     # media_name

            "content": random.choices(fake_all.get('content'))[0],
            "summary": random.choices(fake_all.get('summary'))[0],
            "creator": random.choices(fake_all.get('creator'))[0],
            "attention_type": random.choices(fake_all.get('type'))[0],

            "topic": random.choices(fake_all.get('topic'))[0],
            "topType": random.choices(fake_all.get('type'))[0],

            "inBlacklist": random.choices(fake_all.get('twotype'))[0],
            "has_up": random.choices(fake_all.get('bol'))[0],

            "pub_time": random.choices(fake_all.get('insert_time'))[0],
            "view_count": random.choices(fake_all.get('big_int_random'))[0],
            "longitude": random.choices(fake_all.get('small_float'))[0],
            "latitude": random.choices(fake_all.get('small_float'))[0],
            "distance": random.choices(fake_all.get('big_float'))[0],

            "city": random.choices(fake_all.get('city'))[0],
            "country": random.choices(fake_all.get('country'))[0],
            "province": random.choices(fake_all.get('province'))[0],
            "district": random.choices(fake_all.get('district'))[0],

            "district_code": random.choices(fake_all.get('city_code'))[0],
            "province_code": random.choices(fake_all.get('city_code'))[0],
            "city_code": random.choices(fake_all.get('city_code'))[0],
            "country_code": random.choices(fake_all.get('city_code'))[0],
            "address": random.choices(fake_all.get('address'))[0],
            "ifBlacklist": random.choices(fake_all.get('bol'))[0]
            }
        return res




def gen_one(items):
    ones = {
        "req_id": random.choices(fake_all.get('req_id'))[0],
        "alg_group": random.choices(fake_all.get('strings'))[0],
        "scene": random.choices(fake_all.get('strings'))[0],
        "items": items
    }
    return ones



# {
#     "code": 0,
#     "cost": 1,
#     "data": {
#         "req_id": "41c1eb3cc8464b5db07e3fdbff3d9162",
#         "alg_group": "aaaaaaaaaaaaaaa",
#         "scene": "sssssssssssss",
#         "items": [
#             {
#                 "algs": "aaaaaaaa",
#                 "imgs": [
#                     "http://1257886685.vod2.myqcloud.com/af14f0b9vodhk1257886685/8098b6945285890789174182083/5285890789174182084.jpg",
#                     "http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190528/155898128035750222.jpg"
#                 ],
#                 "cover": "http://1257886685.vod2.myqcloud.com/af14f0b9vodhk1257886685/8098b6945285890789174182083/5285890789174182084.jpg",
#
#                 "title": "巴黎北郊华商批发地发生火灾！过火6000平方米烧毁4个仓库",
#                 "iid": "110000530853",
#                 "unq_id": "",
#                 "mid": "BODgwMDA0MjQ2ODI0",
#                 "insert_time": "",
#                 "type": 2,
#                 "up_count": 32,
#                 "cc_count": 1110,
#                 "shareCount": 1,
#                 "media_desc": "海外网法国融媒体中心",
#                 "media_type": 2,
#                 "media_icon": "http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190214/155011263385692905.jpg",
#                 "media_id": "111785",
#                 "media_name": "相对论",
#                 "content": "{\"url\": \"http://haiwaivideo.src.haiwainet.cn/video/HKBBTVSSK/20190528/155898127545810088.mp4\", \"desc\": \"5月26日19时许，巴黎北郊塞纳-圣但尼省华商批发集散地奥贝维利耶（ Aubervilliers）发生火灾，消防部门动员了约200名灭火人员和多台车辆、器械，大火于23点30分许被扑灭。火灾发生地点位于华商进出口批发区附近。据悉，大火首先从萨迪·卡诺路一座废弃仓库燃起，很快波及其它三座存放鞋类和纺织品的仓库，建筑过火面积达6000平方米，方圆数公里可见浓烟滚滚。\", \"video_name\": \"video_1558981221023.mp4\", \"video_width\": 640, \"video_height\": 422, \"video_length\": 59}",
#                 "summary": "5月26日19时许，巴黎北郊塞纳-圣但尼省华商批发集散地奥贝维利耶（ Aubervilliers）发生火灾，消防部门动员了约200名灭火人员和多台车辆、器械，大火于23点30分许被扑灭。火灾发生地点位于华商进出口批发区附近。据悉，大火首先从萨迪·卡诺路一座废弃仓库燃起，很快波及其它三座存放鞋类和纺织品的仓库，建筑过火面积达6000平方米，方圆数公里可见浓烟滚滚。",
#                 "creator": "鲁佳",
#                 "attention_type": 1,
#
#                 "topic": [
#                     {
#                         "id": 1000176,
#                         "name": "海外华人"
#                     }
#                 ],
#                 "topType": 0,
#
#                 "inBlacklist": 0,
#                 "has_up": False,
#                 "pub_time": 1558981253495,
#                 "view_count": 14,
#                 "longitude": -77.06247,
#                 "latitude": 38.91964,
#                 "distance": 693.37,
#                 "city": "",
#                 "country": "美国",
#                 "province": "",
#                 "district": "",
#                 "district_code": "",
#                 "province_code": "",
#                 "city_code": "",
#                 "country_code": "840",
#                 "address": "3100 Massachusetts Ave NW Washington, DC 20008 美国",
#                 "ifBlacklist": False
#
#             }
#         ]
#     }
# }