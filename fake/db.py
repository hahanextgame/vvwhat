# -*- coding: utf-8 -*-

# @Time :2019/6/3 18:16
# @File: db.py
# @目的

import pymysql

def sql_query(sql):
    # 10.0.15.6'
    conn = pymysql.connect(host='192.168.11.104', port=3306, user='root',
                           password='123456', database='video_test', charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res



def query_one():
    query = 'select video_id, publish_time, play_num, comments_num, media_id, title, media_name, city, province, country, media_type, praise_num from video_info Order By rand() Limit 1'

    one = sql_query(query)
    data_ones = one[0]

    video_id = data_ones[0]
    publish_time = data_ones[1]
    play_num = data_ones[2]
    if play_num == None: play_num = 0
    comments_num = data_ones[3]
    if comments_num == None: comments_num = 0
    media_id = data_ones[4]
    video_title = data_ones[5]
    media_name = data_ones[6]
    city = data_ones[7]
    province = data_ones[8]
    country = data_ones[9]
    media_type = data_ones[10]
    praise_num = data_ones[11]
    if praise_num == None: praise_num = 0

    temp = {"video_id": video_id,
            "publish_time": publish_time,
            "play_num": play_num,
            "comments_num": comments_num,
            "media_id": media_id,
            "media_name": media_name,
            "media_type": media_type,
            "video_title": video_title,
            "city": city,
            "province": province,
            "country": country,
            "praise_num": praise_num}

    return temp
