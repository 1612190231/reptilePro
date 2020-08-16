# coding=UTF-8
import requests
import time
import json


def get_content(url):

    # print(cookie)
    # xy-platform-info/host/connection/accept-Encoding不变
    headers = {
        "Host": "www.xiaohongshu.com",
        "Connection": "Keep-Alive",
        "Authorization": "wxmp.bf5ab29b-331b-4792-8f79-5323c5b6a72b",
        "Device-Fingerprint": "WHJMrwNw1k/EJNxp1A5IErQFfJ7C0u0CfrgrGr9mT5g7gVrTDMIf0vVtqh1IminW/3lE2f0nbNoLvIw2LNGllD4pQxN9Fftv3dCW1tldyDzmauSxIJm5Txg==1487582755342",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "X-Sign": "X922822f0bec250b47a7d7c560f4b8a72",
        "content-type": "application/json",
        "Referer": "https://servicewechat.com/wxffc08ac7df482a27/382/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br"
    }
    # res = requests.get(url, verify=False).text
    res = requests.get(url, headers=headers, verify=False).text
    print(res)

    # 简化json的输出格式
    res2 = json.loads(res)
    res3 = json.dumps(res2, indent=4)
    result = json.loads(res3)

    return result

