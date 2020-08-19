import requests
import re


def clipping(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    # print(res.text)

    like = re.match('<span class="like" data-v-5e3e939c=""><i data-v-5e3e939c=""></i> <span data-v-5e3e939c="">-?[1-9]\d*</span></span>')
    star = re.match('<span class="star" data-v-5e3e939c=""><i data-v-5e3e939c=""></i> <span data-v-5e3e939c="">-?[1-9]\d*</span></span>')
    print(like)
    print(star)

clipping('https://www.xiaohongshu.com/discovery/item/5f33a8ff00000000010032de')

