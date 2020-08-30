import asyncio
import time
from pyppeteer import launch


async def screen_cap(url, item, name):
    browser = await launch(args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = await browser.newPage()
    await page.setViewport({'width': 1000, 'height': 1200})
    # await page.goto('https://www.xiaohongshu.com/explore')
    await page.goto(url)
    time.sleep(2)
    # clip = await page.evaluate('''() =>{
    #     return {
    #         x: 0,
    #         y: 20,
    #     }
    # }''')
    # print(clip)
    html = await page.content()
    print(html)
    path = './photo/screen-' + name + '-' + str(item) + '.png'
    await page.screenshot(path=path)
    # await page.screenshot(path='example.png', clip=clip)
    # await page.pdf(path='example.pdf')
    await browser.close()

