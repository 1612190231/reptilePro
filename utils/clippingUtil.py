import requests
import re


def clipping(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    print(res.text)

    pattern = re.compile(' -?[1-9]\\d*')
    like = re.match(
        '<span class="like" data-v-5e3e939c><i data-v-5e3e939c></i> <span data-v-5e3e939c>-?[1-9]\\d*</span></span>',
        res.text)
    star = re.match(
        '<span class="star" data-v-5e3e939c><i data-v-5e3e939c></i> <span data-v-5e3e939c>-?[1-9]\\d*</span></span>',
        res.text)
    comment = re.match(
        '<span class="comment" data-v-5e3e939c><i data-v-5e3e939c></i> <span data-v-5e3e939c>-?[1-9]\\d*</span></span>',
        res.text)
    print(like)
    print(star)
    print(comment)


clipping('https://www.xiaohongshu.com/discovery/item/5f33a8ff00000000010032de')
