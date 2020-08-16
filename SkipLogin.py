# coding=utf-8
from selenium import webdriver
import time
# 下面四行这么写是去掉谷歌浏览器上面提示的，第二行和第三行分别对应不同的提示
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
# options.add_argument('disable-infobars')
# browser = webdriver.Chrome(chrome_options=options)
#
# browser.maximize_window()
# 打开火狐浏览器
browser = webdriver.Firefox()
# 输入网址
browser.get("https://m.flycua.com/h5/#/")
# 点击登录，用下面注释的代码获取cookie，实现跳过登录，执行脚本的时候就不用这部分了
# browser.find_element_by_id("su").click()
# cookie1= browser.get_cookies()
# 打印登录前的cookie
# print (cookie1)
# 等待30秒，用这30秒时间完成登录操作
# time.sleep(30)
# 获取登录后的cookie
# cookie2= browser.get_cookies()
# 打印登录后的cookie
# print (cookie2)
#
# 加入要获取的cookie，写进去
browser.add_cookie({'name': 'tokenId', 'value': '8BB8FDD4FBB31F92424A7E0EBE872E01A4AF77654043DAD638E9F93B378F94E19A882A6C7E78999C9A5482985FDA333C3D1E5236C6BDA7935A89178F053FB490'})
# 再次输入网址
browser.get("https://m.flycua.com")

