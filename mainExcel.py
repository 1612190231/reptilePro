import xlrd
import time
import asyncio
import ScreenCapture


def excel():
    # 打开Excel文件
    wb = xlrd.open_workbook(
        'D:\\Users\\lu\\Documents\\WeChat Files\\wxid_ah9mt1pem9x812\\FileStorage\\File\\2020-08\\0819李宁发布链接汇总-已更新数据.xlsx')

    # 通过excel表格名称(KOL)获取工作表
    sheet = wb.sheet_by_name('KOL')
    # kol = []  # 创建空list
    # 循环读取表格内容（每次读取一行数据）
    for item in range(sheet.nrows):
        cells = sheet.row_values(item)  # 每行数据赋值给cells
        url = cells[7]
        print(url)

        # 处理截图
        asyncio.get_event_loop().run_until_complete(ScreenCapture.screen_cap(url, item))
        time.sleep(5)

    # 通过excel表格名称(KOC)获取工作表
    sheet = wb.sheet_by_name('KOC')
    # koc = []  # 创建空list
    # 循环读取表格内容（每次读取一行数据）
    for item in range(sheet.nrows):
        cells = sheet.row_values(item)  # 每行数据赋值给cells
        url = cells[6]
        print(url)

        # 处理截图
        asyncio.get_event_loop().run_until_complete(ScreenCapture.screen_cap(url, item))
        time.sleep(5)


excel()
