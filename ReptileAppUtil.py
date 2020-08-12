# coding=UTF-8
import requests
import time
import json


def get_content(url):

    # print(cookie)
    headers = {
        "X-B3-TraceId": "b9b910571e1a0700",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; HMA-TL00 Build/HUAWEIHMA-TL00) Resolution/1080*2244 Version/6.56.0 Build/6560162 Device/(HUAWEI;HMA-TL00) discover/6.56.0 NetType/CellNetwork",
        "shield": "a1e95c6804ee04920b5c6c474951346e",
        "xy-platform-info": "platform=android&build=6560162&deviceId=3883749a-702f-3299-b9ca-4b5ce0645f15",
        "Host": "edith.xiaohongshu.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }

    res = requests.get(url, headers=headers).text
    print(res)

    # 简化json的输出格式
    res2 = json.loads(res)
    res3 = json.dumps(res2, indent=4)
    result = json.loads(res3)

    return result

