import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://www.baidu.com/')
    await page.screenshot(path='example.png')
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

