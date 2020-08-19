import asyncio
import time
from pyppeteer import launch


async def main():
    browser = await launch(args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = await browser.newPage()
    await page.setViewport({'width': 1000, 'height': 1200})
    # await page.goto('https://www.xiaohongshu.com/explore')
    await page.goto('https://www.xiaohongshu.com/discovery/item/5f391758000000000100a384')
    time.sleep(1)
    # clip = await page.evaluate('''() =>{
    #     return {
    #         x: 0,
    #         y: 20,
    #     }
    # }''')
    # print(clip)
    await page.screenshot(path='example.png')
    # await page.screenshot(path='example.png', clip=clip)
    await page.pdf(path='example.pdf')
    dimensions = await page.evaluate('''() =>{
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')

    print(dimensions)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

