# -*- coding: utf-8 -*-
import asyncio
from pyppeteer import launch

# js脚本为了屏蔽淘宝的工具检测
js1 = '''() =>{
           Object.defineProperties(navigator,{
             webdriver:{
               get: () => false
             }
           })
        }'''

js2 = '''() => {
        alert (
            window.navigator.webdriver
        )
    }'''

js3 = '''() => {
        window.navigator.chrome = {
    runtime: {},
    // etc.
  };
    }'''

js4 = '''() =>{
Object.defineProperty(navigator, 'languages', {
      get: () => ['en-US', 'en']
    });
        }'''

js5 = '''() =>{
Object.defineProperty(navigator, 'plugins', {
    get: () => [1, 2, 3, 4, 5,6],
  });
        }'''

width, height = 1366, 768

# 登录函数
async def login(page):
    browser = await launch(devtools=True, userDataDir='./userdata',
                           args=[f'--window-size={width},{height}'], dumpio=True)
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    # 进入登录页面，运行js，填写用户名，密码
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
    await page.goto('https://login.taobao.com/member/login.jhtml')
    await page.evaluate(js1)
    await page.evaluate(js3)
    await page.evaluate(js4)
    await page.evaluate(js5)
    await page.click("#J_Quick2Static")
    await page.focus("#fm_login_id")
    await page.keyboard.sendCharacter("13357157455")
    await page.focus("#fm_login_password")
    await page.keyboard.sendCharacter("lck980621")
    await page.click("#J_SubmitStatic")
    await asyncio.sleep(5)
    # 跳转首页，打印cookie
    await page.goto('https://www.taobao.com')
    cookies2 = await page.cookies()
    print(cookies2)


# 主函数
async def main():
    # 初始化浏览器
    browser = await launch({'headless': False,
                            'dumpio': True,
                            'args': [
                                # '--disable-extensions',
                                # '--disable-bundled-ppapi-flash',
                                # '--mute-audio',
                                # '--no-sandbox',
                                # '--disable-setuid-sandbox',
                                '--disable-gpu',
                            ]})
    # 打开新标签页
    page = await browser.newPage()
    # 登录函数
    await login(page)


# 运行入口
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())