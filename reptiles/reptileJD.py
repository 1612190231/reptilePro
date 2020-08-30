# coding=UTF-8
import requests
import time
import json


def run(source, key):
    tmp_re = source.replace(key, "", 1)
    return tmp_re


def get_content(url):
    # 获取返回实体
    rubbish = 'fetchJSON_comment98('
    # print(rubbish)
    temp = requests.get(url).text.rstrip(');')
    # print(temp)
    res = run(temp, rubbish)
    # print(res)

    # 简化json的输出格式
    res2 = json.loads(res)
    res3 = json.dumps(res2, indent=4)
    result = json.loads(res3)
    print(result)

    return result

