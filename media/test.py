# -*- coding: utf-8 -*-

# @Time :2019/6/6 9:58
# @File: test.py
# @目的

# sqlacodegen postgresql+psycopg2://postgres:postgres@192.168.11.156:5432/botbrain_haike --outfile  model.py

import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from media.model import FdContentMedia, FdContentBehaviorMediaHKBBTVSSK, FdUserLogin
from config.dev import ConfPostgre
import requests

from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(4)


engine = create_engine(ConfPostgre.URL, pool_size=10, pool_recycle=-1)
DBSession = sessionmaker(bind=engine)
session = scoped_session(DBSession)


def one_media(media_id):
    try:
        q_one = session.query(FdContentMedia).filter(FdContentMedia.media_id == media_id).first()
        q_login = session.query(FdUserLogin).filter(FdUserLogin.media_id == media_id).first()
        q_behavior = session.query(FdContentBehaviorMediaHKBBTVSSK).filter(
            FdContentBehaviorMediaHKBBTVSSK.followed_media_id == media_id).first()
        session.commit()
        res = {
            "media_id": q_one.media_id,
            "os_key": q_one.os_key,
            "name": q_one.name,
            "source_type": q_one.source_type,
            "ugc_type": None,
            "icon": q_one.icon,
            "cover": q_one.cover,
            "source_ids": q_one.source_ids,
            "third_id": q_one.third_id,
            "create_time": q_one.create_time,
            "status": q_one.status,
            "describe": q_one.describe,
            "ext": q_one.ext,
            "province": q_one.province,
            "city": q_one.city,
            "area": q_one.area,
            "sex": q_one.sex,
            "age": q_one.sex,
            "birth": q_one.birth,
            "email": q_one.email,
            "country": q_one.country,
            "address": q_one.address,
            "update_time": q_one.update_time,
            "sign_time": q_one.sign_time,
            "media_mark": q_one.media_mark,

            "able_status": q_login.status,  # log_in
            "mobile": q_login.mobile,  # log_in
            "country_code": "86",
            "user_status": q_one.status,
            "regist_type": 0,  # log_in
            "attention_type": q_behavior.type,  #############    fd_content_behavior_media_
            "attention_time": q_behavior.server_time,  #############    fd_content_behavior_media_
            "media_num": q_one.media_num,
            "ip": q_behavior.ip,  #############
            "position_lng": q_one.longitude,
            "position_lat": q_one.latitude
        }
        return res
    except Exception as e:
        print(e)
        session.rollback()
        res = {
            "error": e
        }
        return res




def query_all(medias:list):
    try:
        res = pool.map_async(one_media, medias)
        res.wait()
        if res.successful() == True:
            items = res.get()
            return items
    except Exception as e:
        print(e)
        return []



def pull_list():
    '''

    :return:
    '''
    a = time.time()
    medias = [112602, 112602, 112602]*10
    res = query_all(medias)

    b = time.time()
    cost = int(b - a)*10
    out = {
        "code": 0,
        "cost": cost,
        "msg": "success",
        "data": res
    }
    return out