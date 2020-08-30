import asyncio
from pyppeteer import launch

width, height = 1366, 768


async def main():
    browser = await launch(devtools=True, userDataDir='./userdata',
                           args=[f'--window-size={width},{height}'], dumpio=True)
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0')
    await page.goto('https://www.taobao.com')
    # await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await asyncio.sleep(100)


asyncio.get_event_loop().run_until_complete(main())

