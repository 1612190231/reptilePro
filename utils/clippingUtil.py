import time
import asyncio
from pyppeteer import launch


async def clipping(url):
    browser = await launch(args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = await browser.newPage()
    await page.setViewport({'width': 1000, 'height': 1200})
    # await page.goto('https://www.xiaohongshu.com/explore')
    await page.goto(url)
    # time.sleep(2)

    dicts = {}
    items_like = await page.xpath('//span[@class="like"]/span')
    for item_like in items_like:
        dicts['like'] = await(await item_like.getProperty('textContent')).jsonValue()
    items_star = await page.xpath('//span[@class="star"]/span')
    for item in items_star:
        dicts['star'] = await(await item.getProperty('textContent')).jsonValue()
    items_comment = await page.xpath('//span[@class="comment"]/span')
    for item in items_comment:
        dicts['comment'] = await(await item.getProperty('textContent')).jsonValue()

    return dicts.values()


asyncio.get_event_loop().run_until_complete(clipping('https://www.xiaohongshu.com/discovery/item/5f33a8ff00000000010032de'))
