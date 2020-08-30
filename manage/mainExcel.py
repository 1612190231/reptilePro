import xlrd
import time
import asyncio

from reptilePro.utils import screenCaptureUtil, entryUtil


def main():
    url = entryUtil.get_input("小红书截图Reptile",
        "示例：D:\\Users\\lu\\Documents\\WeChat Files\\wxid_ah9mt1pem9x812\\FileStorage\\File\\2020-08\\0819李宁发布链接汇总-已更新数据.xlsx")
    # 打开Excel文件
    wb = xlrd.open_workbook(url)

    # 通过excel表格名称(KOL)获取工作表
    # sheet = wb.sheet_by_name('KOL')
    # kol = []  # 创建空list
    # 循环读取表格内容（每次读取一行数据）
    # for item in range(sheet.nrows):
    # cells = sheet.row_values(item+1)  # 每行数据赋值给cells
    # url = cells[7]
    # print(url)

    # 处理截图 可以去掉time.sleep
    # asyncio.get_event_loop().run_until_complete(ScreenCapture.screen_cap(url, item+1,'KOL'))
    # time.sleep(1)

    # 通过excel表格名称(KOC)获取工作表
    sheet = wb.sheet_by_name('KOC')
    koc = []  # 创建空list
    # 循环读取表格内容（每次读取一行数据）
    for item in range(101, sheet.nrows):
        cells = sheet.row_values(item + 1)  # 每行数据赋值给cells
        url = cells[0]
        print(url)
        #
        #     处理截图
        asyncio.get_event_loop().run_until_complete(screenCaptureUtil.screen_cap(url, item + 1, 'KOC'))
        time.sleep(2)


if __name__ == "__main__":
    main()


