# -*- coding: utf-8 -*-

# @Time :2019/5/29 8:25
# @File: view_control.py
# @目的

from fake.layout import gen_one, get_only_one



def fake_ct(ct):
    '''
    分页数量
    :param ct: 分页参数，默认是5
    :return:
    '''
    fake_ct = []
    for i in range(ct):
        fake_one = get_only_one()
        fake_ct.append(fake_one)

    res = gen_one(fake_ct)
    out_data = {
        "code": 0,
        "cost": 1,
        "data": res
    }

    return out_data
