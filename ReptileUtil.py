# coding=UTF-8
import requests
import time
import json


def run(source, key):
    tmp_re = source.replace(key, "", 1)
    return tmp_re


def get_content(url, cookie_dict, current_page):
    # 伪装请求头
    cookie = ''
    for k, v in cookie_dict.items():
        cookie_temp = ('%s=%s; ' % (k, v))
        cookie = "{}{}".format(cookie, cookie_temp)

    # print(cookie)
    headers = {
        "Cookie": cookie,
        "referer": "https://detail.tmall.com/item.htm?spm=a1z10.4-b-s.w4007-18945924930.2.624155f7boAyho&id=602659642364",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
    }
    # print(headers)

    # 伪装param
    t_param = time.time()
    # print(t_param)
    t_list = str(t_param).split(".")
    callback = "jsonp" + str(int(t_list[1][3:]) + 1)
    # print(t_list)
    params = {
        "callback": callback,
        "_ksTS": t_list[0] + t_list[1][:3] + "_" + t_list[1][3:],
        "currentPage": current_page
    }
    print(params)
    # print(params)

    # 获取返回实体
    rubbish = callback + '('
    # print(rubbish)
    temp = requests.get(url, params=params, headers=headers).text.rstrip(')')
    # print(temp)
    res = run(temp, rubbish)
    # print(res)

    # 简化json的输出格式
    res2 = json.loads(res)
    res3 = json.dumps(res2, indent=4)
    result = json.loads(res3)
    print(result)

    return result

