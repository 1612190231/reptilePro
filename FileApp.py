import time
import tkinter.filedialog
import xlwt
import xlrd
import xlutils.copy


def get_file(result):
    # 新建excel文档
    # 创建一个workbook 设置编码
    # workbook = xlwt.Workbook(encoding='utf-8')
    # # 创建一个worksheet
    # worksheet = workbook.add_sheet('xhs')
    # # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # filename = tkinter.filedialog.asksaveasfilename(initialfile='XHS-search', filetypes=[('xlsx', '*.xlsx')],
    #                                                 initialdir='D:\\Users\\lu\\Desktop')
    # filename = filename + '.xls'
    #
    # # 写入excel
    # worksheet.write(0, 0, "用户昵称")
    # worksheet.write(0, 1, "标题")
    # worksheet.write(0, 2, "点赞")
    # worksheet.write(0, 3, "发帖时间")

    # 打开已有workbook
    rb = xlrd.open_workbook('D:\\Users\\lu\\Desktop\\XHS-search.xls')
    workbook = xlutils.copy.copy(rb)
    # 获取已有worksheet
    worksheet = workbook.get_sheet(0)

    for items in range(100, 120):
        # 参数对应 行, 列, 值
        result_nickname = result["data"]["notes"][items % 20]["user"]["nickname"]
        result_title = result["data"]["notes"][items % 20]["title"]
        result_likes = result["data"]["notes"][items % 20]["likes"]
        result_time = result["data"]["notes"][items % 20]["time"]
        worksheet.write(items+1, 0, result_nickname)
        worksheet.write(items+1, 1, result_title)
        worksheet.write(items+1, 2, result_likes)
        worksheet.write(items+1, 3, result_time)

    # 保存新建的file
    # workbook.save(filename)

    # 保存已存在的file
    workbook.save("D:\\Users\\lu\\Desktop\\XHS-search.xls")
    return 0

