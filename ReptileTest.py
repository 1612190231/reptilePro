import asyncio
from pyppeteer import launch
from lxml import etree


async def main():
    # headless参数设为False，则变成有头模式
    browser = await launch(headless=False)

    page1 = await browser.newPage()

    # 设置页面视图大小
    await page1.setViewport(viewport={'width': 1280, 'height': 800})

    await page1.goto('https://www.toutiao.com/')
    await asyncio.sleep(2)
    # 打印页面文本
    page_text = await page1.content()

    page2 = await browser.newPage()
    await page2.setViewport(viewport={'width': 1280, 'height': 800})
    await page2.goto('https://news.163.com/domestic/')
    await page2.evaluate('window.scrollTo(0,document.body.scrollHeight)')
    page_text1 = await page2.content()

    await browser.close()

    return {'wangyi': page_text1, 'toutiao': page_text}


def parse(task):
    content_dic = task.result()
    wangyi = content_dic['wangyi']
    toutiao = content_dic['toutiao']

    # 头条数据解析
    tree = etree.HTML(toutiao)
    a_list = tree.xpath('//div[@class="title-box"]/a')
    for a in a_list:
        title = a.xpath('./text()')[0]
        print('toutiao:', title)

    # 网易数据解析
    tree = etree.HTML(wangyi)
    div_list = tree.xpath('//div[@class="data_row news_article clearfix "]')
    for div in div_list:
        title = div.xpath('.//div[@class="news_title"]/h3/a/text()')[0]
        print('wangyi:', title)


# 创建任务列表
tasks = []
# 创建任务对象
task1 = asyncio.ensure_future(main())
# 任务回调函数
task1.add_done_callback(parse)
tasks.append(task1)

# 将任务列表放入事件循环中，挂起任务并运行
asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))