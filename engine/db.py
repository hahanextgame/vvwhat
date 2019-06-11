# -*- coding: utf-8 -*-

# @Time :2019/6/4 15:30
# @File: db.py
# @目的

import pandas as pd
from sqlalchemy import create_engine
from config.dev import ConfMySQL

engine = create_engine(ConfMySQL.URL)


def _get_info(limits = 100):
    query_video = '''
        SELECT video_id, mid, model, country, publish_time, screen_height, title, channel_id,
        network_type, province, video_time, city, screen_width, video_tag, is_first_day, manufacturer,
        wifi, media_name
        FROM video_info WHERE content != "" and video_status != "2" ORDER BY publish_time desc LIMIT {}
    
    '''.format(100)
    video_info = pd.read_sql(query_video, engine)
    return video_info



def _get_user(media_id):
    '''
    '''
    query_user = '''
            SELECT media_id,
                    screen_height,
                    screen_width,
                    is_first_day,
                    manufacturer,
                    wifi,
                    network_type,
                    os
            from video_user WHERE media_id = '{}'
            '''.format(media_id)
    video_user = pd.read_sql_query(query_user, engine)
    return video_user




def _broad_data(video_info, video_user):
    data_pre = video_info.copy()
    data_pre['media_id'] = video_user.media_id.head(1).item()
    data_pre['screen_height'] = video_user.screen_height.head(1).item()
    data_pre['screen_width'] = video_user.screen_width.head(1).item()
    data_pre['is_first_day'] = video_user.is_first_day.head(1).item()
    data_pre['manufacturer'] = video_user.manufacturer.head(1).item()
    data_pre['wifi'] = video_user.wifi.head(1).item()
    data_pre['network_type'] = video_user.network_type.head(1).item()
    data_pre['os'] = video_user.os.head(1).item()
    return data_pre



def pull_mysql(media_id):
    '''
    media_id = "111738"
    :param media_id:
    :return:
    '''
    video_info = _get_info()
    video_user = _get_user(media_id)
    if len(video_user) == 0:
        return {
            "message": "please input the right media_id",
            'code': 404
        }
    data_pre = _broad_data(video_info, video_user)
    return data_pre
