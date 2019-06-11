# -*- coding: utf-8 -*-

# @Time :2019/6/4 15:21
# @File: test.py
# @目的

import pandas as pd
import jieba
import re

import datetime
from gensim.models import KeyedVectors
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib

wordvec_model = KeyedVectors.load_word2vec_format('cn.cbow.bin', binary=True, unicode_errors='ignore')

gbm = joblib.load('predictor/gbm.pkl')


channelid_trans = joblib.load('predictor/trans_channelid.pkl')
wifi_trans = joblib.load('predictor/trans_$wifi.pkl')
os_trans = joblib.load('predictor/trans_$os.pkl')
network_type_trans = joblib.load('predictor/trans_$network_type.pkl')
model_trans = joblib.load('predictor/trans_$model.pkl')
manufacturer_trans = joblib.load('predictor/trans_$manufacturer.pkl')


feature_col = ['publishtime', '$model', '$country_x', '$screen_height',
               'videotitle', 'channelid', '$network_type', '$province_x', 'videotime',
               '$city_x', '$screen_width', 'videotag', '$is_first_day', '$manufacturer',
               'playtimes', '$os', '$wifi', 'medianame']





# feature_col = ['publishtime', '$model', '$country_x', '$screen_height',
#                'videotitle', 'channelid', '$network_type', '$province_x', 'videotime',
#                '$city_x', '$screen_width', 'videotag', '$carrier', '$is_first_day', '$manufacturer',
#                'registertime', 'year', 'playtimes', '$os', '$wifi', 'medianame']


class_label_name = ['$model', 'channelid', '$network_type', '$manufacturer', '$os', '$wifi']

class_label_name =['model', 'channel_id', 'network_type', 'manufacturer', 'os', 'wifi']



def converter_first_day(inputs):
    if inputs == 'false':
        res = 0
    else:
        res = 1

    return res

def converter_video_time(inputs):
    try:
        if inputs == '':
            res = 60
        else:
            res = float(inputs)
    except Exception as e:
        res = 90

    return res

['model', 'channel_id', 'network_type', 'manufacturer', 'os']



def converter_model(inputs):
    try:
        res = model_trans.transform(inputs)
        return res
    except Exception as e:
        res = 345
        return res

def converter_channel_id(inputs):
    try:
        res = channelid_trans.transform(inputs)
        return res
    except Exception as e:
        res = 74
        return res


def converter_network_type(inputs):
    try:
        res = network_type_trans.transform(inputs)
        return res
    except Exception as e:
        res = 3
        return res

def converter_manufacturer(inputs):
    try:
        res = manufacturer_trans.transform(inputs)
        return res
    except Exception as e:
        res = 1
        return res

def converter_os(inputs):
    try:
        res = os_trans.transform(inputs)
        return res
    except Exception as e:
        res = 0
        return res


def converter_wifi(inputs):
    try:
        res = wifi_trans.transform(inputs)
        return res
    except Exception as e:
        res = 0
        return res



def time_what(inputs):
    try:
        if pd.isna(inputs) == True: return 3
        inputs = int(inputs/1000)
        dateArray = datetime.datetime.utcfromtimestamp(inputs)
        if dateArray.hour > 12:
            return 2
        else:
            return 1
    except Exception as e:
        return 3

    #otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")

times = ['publishtime']




words = ['$country_x', '$province_x', '$city_x']

def word_vec_sum(inputs):
    '''

    :param inputs:  country, province， 'city_x'
    :return:
    '''
    try:
        res = wordvec_model[inputs].tolist()
        res = sum(res)
        return res
    except Exception as e:
        print(e)
        res = 66
        return res




cut_word_vec = [ 'videotitle', 'videotag', 'medianame']


def cut_sens(word: str):
    '''
    :param word: ’你最近还好吗?'
    :return: ['你','最近','还','好吗']
    '''
    test = re.sub('[a-zA-Z0-9’·!"•#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！，；◆～（：）。/.[\\]^_`{|}~\s]+', "", word)
    sentence = " ".join(jieba.cut(test)).replace('的', '').replace('月', '').replace('日', '').replace('天', '')
    words = sentence.split(' ')
    words = [i for i in words if i != '']
    return words


def cut_vec(word):
    try:
        words = cut_sens(word)[:5]
        res = [word_vec_sum(i) for i in words]
        res = sum(res)
        return res
    except Exception as e:
        res = 555
        return 555




data_pre = pd.DataFrame()

feature_col = ['model', 'country', 'publish_time', 'screen_height',
       'title', 'channel_id', 'network_type', 'province', 'video_time', 'city',
       'screen_width', 'video_tag', 'is_first_day', 'manufacturer', 'wifi',
       'media_name', 'os']

data_pre['video_time'] = data_pre['video_time'].map(converter_video_time)
data_pre['screen_height'] = data_pre['screen_height'].map(float)
data_pre['screen_width'] = data_pre['screen_width'].map(float)

data_pre['is_first_day'] = data_pre['is_first_day'].map(converter_first_day)
data_pre['model'] = data_pre['model'].map(converter_model)
data_pre['channel_id'] = data_pre['channel_id'].map(converter_channel_id)
data_pre['network_type'] = data_pre['network_type'].map(converter_network_type)
data_pre['manufacturer'] = data_pre['manufacturer'].map(converter_manufacturer)
data_pre['os'] = data_pre['model'].map(converter_os)
data_pre['wifi'] = data_pre['model'].map(converter_wifi)

data_pre['publish_time'] = data_pre['publish_time'].map(time_what)

data_pre['country'] = data_pre['country'].map(word_vec_sum)
data_pre['province'] = data_pre['province'].map(word_vec_sum)
data_pre['city'] = data_pre['city'].map(word_vec_sum)


data_pre['title'] = data_pre['title'].map(cut_vec)
data_pre['video_tag'] = data_pre['video_tag'].map(cut_vec)
data_pre['media_name'] = data_pre['media_name'].map(cut_vec)


data_pres = data_pre[feature_col]

pred_data = data_pres.to_numpy()

gbm.predict(pred_data)

