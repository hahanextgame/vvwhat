# -*- coding: utf-8 -*-

# @Time :2019/6/5 8:34
# @File: pretreat.py
# @目的

# -*- coding: utf-8 -*-

# @Time :2019/6/4 15:21
# @File: test.py
# @目的


import jieba
import re
import datetime

import pandas as pd
from gensim.models import KeyedVectors
from sklearn.externals import joblib

wordvec_model = KeyedVectors.load_word2vec_format('cn.cbow.bin', binary=True, unicode_errors='ignore')


gbm = joblib.load('predictor/gbm.pkl')

channelid_trans = joblib.load('predictor/trans_channelid.pkl')
wifi_trans = joblib.load('predictor/trans_$wifi.pkl')
os_trans = joblib.load('predictor/trans_$os.pkl')
network_type_trans = joblib.load('predictor/trans_$network_type.pkl')
model_trans = joblib.load('predictor/trans_$model.pkl')
manufacturer_trans = joblib.load('predictor/trans_$manufacturer.pkl')



def converter_first_day(inputs):
    '''
    is_first_day
    :param inputs:
    :return:
    '''
    if inputs == 'false':
        res = 0
    else:
        res = 1

    return res

def converter_video_time(inputs):
    '''
    video_time
    :param inputs:
    :return:
    '''
    try:
        if inputs == '':
            res = 60
        else:
            res = float(inputs)
    except Exception as e:
        res = 90

    return res


def converter_model(inputs):
    '''
    model
    :param inputs:
    :return:
    '''
    try:
        res = model_trans.transform(inputs)
        return res
    except Exception as e:
        res = 345
        return res

def converter_channel_id(inputs):
    '''
    channel_id
    :param inputs:
    :return:
    '''
    try:
        res = channelid_trans.transform(inputs)
        return res
    except Exception as e:
        res = 74
        return res


def converter_network_type(inputs):
    '''
    network_type
    :param inputs:
    :return:
    '''
    try:
        res = network_type_trans.transform(inputs)
        return res
    except Exception as e:
        res = 3
        return res

def converter_manufacturer(inputs):
    '''
    manufacturer
    :param inputs:
    :return:
    '''
    try:
        res = manufacturer_trans.transform(inputs)
        return res
    except Exception as e:
        res = 1
        return res

def converter_os(inputs):
    '''
    os
    :param inputs:
    :return:
    '''
    try:
        res = os_trans.transform(inputs)
        return res
    except Exception as e:
        res = 0
        return res


def converter_wifi(inputs):
    '''
    wifo
    :param inputs:
    :return:
    '''
    try:
        res = wifi_trans.transform(inputs)
        return res
    except Exception as e:
        res = 0
        return res



def time_what(inputs):
    '''
    publish_time
    :param inputs:
    :return:
    '''
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





def word_vec_sum(inputs):
    '''
    country, province， 'city
    :param inputs:  '
    :return:
    '''
    try:
        res = wordvec_model[inputs].tolist()
        res = sum(res)
        return res
    except Exception as e:
        # print(e)
        res = 66
        return res




def _cut_sens(word: str):
    '''
    for cut_vec
    :param word: ’你最近还好吗?'
    :return: ['你','最近','还','好吗']
    '''
    test = re.sub('[a-zA-Z0-9’·!"•#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！，；◆～（：）。/.[\\]^_`{|}~\s]+', "", word)
    sentence = " ".join(jieba.cut(test)).replace('的', '').replace('月', '').replace('日', '').replace('天', '')
    words = sentence.split(' ')
    words = [i for i in words if i != '']
    return words


def cut_vec(word):
    '''
    title, video_tag, media_name
    :param word:
    :return:
    '''
    try:
        words = _cut_sens(word)[:5]
        res = [word_vec_sum(i) for i in words]
        res = sum(res)
        return res
    except Exception as e:
        res = 555
        return 555



def pred_prob(inputs_dataframe):

    data_pre = inputs_dataframe.copy()
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

    pred_data = data_pre[feature_col]
    pred_data = pred_data.to_numpy()

    pred_res = gbm.predict(pred_data)


    # 本来应该是mid的
    mid = data_pre['video_id']

    k = mid.to_list()
    w = pred_res.tolist()

    res = dict(zip(k, w))
    res = sorted(res.items(), key=lambda x: x[1], reverse=True)
    return res