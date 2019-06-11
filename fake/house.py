# -*- coding: utf-8 -*-

# @Time :2019/5/28 16:19
# @File: house.py
# @目的
import random

fake_all = {
    "bol": [True, False],
    'small_int_random': [30 + random.randint(1, 10),
                         40 + random.randint(20, 40),
                         10 + random.randint(2, 10),
                         15 + random.randint(1, 20),
                         10 + random.randint(0, 10)],

    "big_int_random": [80 + random.randint(1, 10),
                       100 + random.randint(20, 40),
                       1000 + random.randint(2, 10),
                       500 + random.randint(1, 20),
                       300 + random.randint(0, 10)],

    'title': ['学猫叫', '讲真的', '远走高飞', '你的前男友', '沙漠骆驼', '欧巴我不傻',
              '往后余生', '可不可以', '去年夏天', '等一分钟', '广东爱情故事', '带你去旅行',
              '苦行僧', '一生所爱', 'C哩C哩'],

    'small_float': [random.random() * 100, random.random() * 80 - 50],
    'big_float': [random.random() * 1000, random.random() * 2000 - 231,
                  random.random() * 300 + 1000],

    'content': [{'url': 'http://haiwaivideo.src.haiwainet.cn/video/HKBBTVSSK/20190520/155831312613297194.mp4',
                 'desc': '测试', 'video_name': 'video_1558313091927.mp4', 'video_width': 640, 'video_height': 360,
                 'video_length': 233},
                {'url': 'http://haiwaivideo.src.haiwainet.cn/video/HKBBTVSSK/20190527/155891942681429050.mp4',
                 'video_name': '梅姨辞职声明完整版：对继任者寄予厚望_World湃_澎湃新闻-The Paper.mp4', 'video_width': 640,
                 'video_height': 360, 'video_length': 405},
                {'url': 'http://haiwaivideo.src.haiwainet.cn/video/HKBBTVSSK/20190527/155891339297478477.mp4',
                 'desc': '老哥稳', 'video_name': 'video_1558913372169.mp4', 'video_width': 362, 'video_height': 640,
                 'video_length': 9},
                {'url': 'http://haiwaivideo.src.haiwainet.cn/video/HKBBTVSSK/20190526/155884331644158524.mp4',
                 'desc': '打卡Gordon Ramsay家的汉堡店 实话是很失望 不怎么样好吃的 就是名气大 个人更偏爱他开的另外一家吃炸鱼炸虾的那家店',
                 'video_name': 'video_1558843280636.mp4', 'video_width': 480, 'video_height': 640, 'video_length': 8},
                {'url': 'http://haiwaivideo.src.haiwainet.cn/video/HKBBTVSSK/20190526/155882708425131267.mp4',
                 'desc': '在美国大学的校园里，随处可见一些可爱的动物们。似乎是因为见多了来来往往的学生们，这些小动物早已对人们司空见惯了，有时甚至还会大胆的走近向人们“卖萌”并且讨要食物。',
                 'video_name': 'video_1558827034490.mp4', 'video_width': 640, 'video_height': 360, 'video_length': 46},
                {'url': 'http://haiwaivideo.src.haiwainet.cn/video/HKBBTVSSK/20190525/155874189338114724.mp4',
                 'desc': '在国内人山人海排队才能买到的Lady M在尔湾轻轻松松就可以吃到了哦～幸福嘻嘻', 'video_name': 'video_1558741846635.mp4',
                 'video_width': 640,
                 'video_height': 360, 'video_length': 26},
                {'url': 'http://haiwaivideo.src.haiwainet.cn/video/HKBBTVSSK/20190525/155874027350049717.mp4',
                 'desc': '看准时间真的很重要啊 有想来打卡的小伙伴们记得看看时间 不然你看的景象就都是人了 有种此山是我开的感觉 so棒棒～不过应该是因为拉斯维加斯最近下了太多次雨的原因 颜色都有些褪了 小伙伴们快抓紧时间啦',
                 'video_name': 'video_1558740255106.mp4', 'video_width': 640, 'video_height': 480, 'video_length': 7},
                {'url': 'http://haiwaivideo.src.haiwainet.cn/video/HKBBTVSSK/20190524/155865598708049471.mp4',
                 'desc': '坐落于洛杉矶市中心的新美国联邦法院的设计既体现了现代精神，又植根于联邦建筑的经典原则。它采用传统的建筑元素，如庄严的大台阶、开阔的公共空间以及石灰石这类耐久材料来凸显城市公共形象。',
                 'video_name': 'video_1558655871975.mp4', 'video_width': 640, 'video_height': 360, 'video_length': 23},
                {'url': 'http://haiwaivideo.src.haiwainet.cn/video/HKBBTVSSK/20190524/155865431673410789.mp4',
                 'desc': '在安静的学习室里，两个美国大学生竟然不顾周围学生感受随意嬉戏打闹。这种不负责任的行为持续了近半个小时，期间并没有相关管理人员前来制止。我们所期望的开放自由的留学环境真的是这样的么？',
                 'video_name': 'video_1558654269585.mp4', 'video_width': 360, 'video_height': 640, 'video_length': 27},
                {'url': 'http://haiwaivideo.src.haiwainet.cn/video/HKBBTVSSK/20190524/155865154736795237.mp4',
                 'desc': '洛杉矶警察局是全美口碑最丑的哈哈哈臭名昭著与办事效率慢到令人发指，今天的追踪报道到底慢到哪儿了？来看',
                 'video_name': 'video_1558651397082.mp4', 'video_width': 640, 'video_height': 360, 'video_length': 64}]
    ,
    'topic': [[{'id': 1000163, 'name': '美食'}],
              [{'id': 1000001, 'name': '新闻频道'}, {'id': 1000151, 'name': '英国脱欧：梅姨笑容满面 欧洲却阴霾笼罩'}],
              [{'id': 1000174, 'name': '娱乐'}],
              [{'id': 1000174, 'name': '娱乐'}, {'id': 1000165, 'name': '旅游'}, {'id': 1000163, 'name': '美食'}],
              [{'id': 1000176, 'name': '海外华人'}], [{'id': 1000163, 'name': '美食'}],
              [{'id': 1000170, 'name': '风景民俗'}, {'id': 1000165, 'name': '旅游'}],
              [{'id': 1000176, 'name': '海外华人'}, {'id': 1000191, 'name': '涨姿势'}, {'id': 1000189, 'name': '趣味科普'}],
              [{'id': 1000184, 'name': '人文'}],
              [{'id': 1000176, 'name': '海外华人'}, {'id': 1000186, 'name': '纪实'}]]
    ,
    'summary': ['测试', '当地时间5月24日，英国伦敦，英国首相特蕾莎·梅在唐宁街10号首相府发表辞职声明，宣布将在6月7日辞去保守党党首职务，新首相的选举将从下周开始。',
                '老哥稳', '打卡Gordon Ramsay家的汉堡店 实话是很失望 不怎么样好吃的 就是名气大 个人更偏爱他开的另外一家吃炸鱼炸虾的那家店',
                '在美国大学的校园里，随处可见一些可爱的动物们。似乎是因为见多了来来往往的学生们，这些小动物早已对人们司空见惯了，有时甚至还会大胆的走近向人们“卖萌”并且讨要食物。',
                '在国内人山人海排队才能买到的Lady M在尔湾轻轻松松就可以吃到了哦～幸福嘻嘻',
                '看准时间真的很重要啊 有想来打卡的小伙伴们记得看看时间 不然你看的景象就都是人了 有种此山是我开的感觉 so棒棒～不过应该是因为拉斯维加斯最近下了太多次雨的原因 颜色都有些褪了 小伙伴们快抓紧时间啦',
                '坐落于洛杉矶市中心的新美国联邦法院的设计既体现了现代精神，又植根于联邦建筑的经典原则。它采用传统的建筑元素，如庄严的大台阶、开阔的公共空间以及石灰石这类耐久材料来凸显城市公共形象。',
                '在安静的学习室里，两个美国大学生竟然不顾周围学生感受随意嬉戏打闹。这种不负责任的行为持续了近半个小时，期间并没有相关管理人员前来制止。我们所期望的开放自由的留学环境真的是这样的么？',
                '洛杉矶警察局是全美口碑最丑的哈哈哈臭名昭著与办事效率慢到令人发指，今天的追踪报道到底慢到哪儿了？来看']
    ,
    'address': ['address 100', 'goldren street', 'love bridge 101', 'fireboy 454']
    , 'creator': ['叶圣陶', '契诃夫', '莎士比亚', '狄更斯', '路遥', '钱钟书']
    , 'media_name': ['美联社', '法新社', '鬼脚七', '头条号']
    , 'media_id': [45, 78, 989, 778, 1231, 2313, 4343]
    , 'mid': ['asdafa', 'afbidgbhkg', 'uyufuayf', 'asfhaksfuaf', 'IYIUY', 'AFHjkafg', 'Fljfklj', 'adfaoiuuH']
    , 'insert_time': [1558313098885, 1558919691797, 1558913380661, 1558843304779, 1558827055286, 1558741862034,
                      1558740263318, 1558655910878, 1558654285608, 1558651482613]
    , 'imgs': [[
                   'http://1400201594.vod2.myqcloud.com/fcc5f3dcvodcq1400201594/a57f805c5285890789313952982/5285890789313952983.jpg'],
               ['http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190527/155891951126754338.jpg',
                'http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190527/155891944536486204.jpg'], [
                   'http://1257886685.vod2.myqcloud.com/84b5094avodca1257886685/410ff81d5285890789173708188/5285890789173708189.jpg',
                   'http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190527/155891339823453551.jpg'], [
                   'http://1257886685.vod2.myqcloud.com/b11c9e13voduse1257886685/410e707e5285890789173705867/5285890789173705868.jpg',
                   'http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190526/155884332212832792.jpg'], [
                   'http://1257886685.vod2.myqcloud.com/11a15ca5vodusw1257886685/acb12cbe5285890789154379447/5285890789154379448.jpg',
                   'http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190526/155882711275674085.jpg'], [
                   'http://1257886685.vod2.myqcloud.com/b11c9e13voduse1257886685/3f4855775285890789173682442/5285890789173682443.jpg',
                   'http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190525/155874190069377707.jpg'], [
                   'http://1257886685.vod2.myqcloud.com/11a15ca5vodusw1257886685/3f4851795285890789173682363/5285890789173682364.jpg',
                   'http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190525/155874027732560369.jpg'], [
                   'http://1257886685.vod2.myqcloud.com/11a15ca5vodusw1257886685/acade6365285890789154373508/5285890789154373509.jpg',
                   'http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190524/155865607332350644.jpg'], [
                   'http://1257886685.vod2.myqcloud.com/b11c9e13voduse1257886685/acade2585285890789154373438/5285890789154373439.jpg',
                   'http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190524/155865432416418299.jpg'], [
                   'http://1257886685.vod2.myqcloud.com/b11c9e13voduse1257886685/3f3a06d85285890789173679140/5285890789173679141.jpg',
                   'http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190524/155865157144452462.jpg']]
    , 'cover': [
        'http://1400201594.vod2.myqcloud.com/fcc5f3dcvodcq1400201594/a57f805c5285890789313952982/5285890789313952983.jpg',
        'http://haiwaivideo.src.haiwainet.cn/image/HKBBTVSSK/20190527/155891951126754338.jpg',
        'http://1257886685.vod2.myqcloud.com/84b5094avodca1257886685/410ff81d5285890789173708188/5285890789173708189.jpg',
        'http://1257886685.vod2.myqcloud.com/b11c9e13voduse1257886685/410e707e5285890789173705867/5285890789173705868.jpg',
        'http://1257886685.vod2.myqcloud.com/11a15ca5vodusw1257886685/acb12cbe5285890789154379447/5285890789154379448.jpg',
        'http://1257886685.vod2.myqcloud.com/b11c9e13voduse1257886685/3f4855775285890789173682442/5285890789173682443.jpg',
        'http://1257886685.vod2.myqcloud.com/11a15ca5vodusw1257886685/3f4851795285890789173682363/5285890789173682364.jpg',
        'http://1257886685.vod2.myqcloud.com/11a15ca5vodusw1257886685/acade6365285890789154373508/5285890789154373509.jpg',
        'http://1257886685.vod2.myqcloud.com/b11c9e13voduse1257886685/acade2585285890789154373438/5285890789154373439.jpg',
        'http://1257886685.vod2.myqcloud.com/b11c9e13voduse1257886685/3f3a06d85285890789173679140/5285890789173679141.jpg']
    ,
    'iid': ['45646788', '111111111546468', '6645648', '78978945', '15646664', '45646978991', '111111134564', '54564646']
    , 'media_desc': ['中文网络著名的互联网', '开发电梯媒体和广告发布', ' 依托于数字技术、互联网']
    , 'province': ['广州', '深圳', '福建', '河南', '贵州', '江苏', '浙江', '内蒙古']
    , 'country': ['中国', '美国', "越南", '俄罗斯', '英国', '']
    , 'city': ['北京', '上海', '杭州', '南京', '长安']
    , 'city_code': ['1010', '2312', '96775', '23131', '', '1231', '1441']
    , 'req_id': ['41c1eb3cc8464b5db07e3fdbff3d9162', '3cc8b5db07e3fdbff3d916asd2', 'ebdasdabaff3d9162',
                 '878cadpjpjpphp', '887831aeaea', '9893daea2113hjk3b1', '878hjkbnmzb1231', 'aacih988123',
                 'iggd9898779', 'i0899asdada', '9sadagaa']
    , 'strings': ['asdad', 'asfafas', 'cvvdsfas', 'sadaa']
    , 'type': [1, 2, 3, 4, 5, 6]
    , 'twotype': [0, 1]
    , 'district': ['华东', '华北', '西北', '西南']
}
