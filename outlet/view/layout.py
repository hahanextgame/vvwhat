# -*- coding: utf-8 -*-

# @Time :2019/6/5 9:51
# @File: layout.py
# @目的


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
