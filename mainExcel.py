import xlrd


def excel():
    # 打开Excel文件
    wb = xlrd.open_workbook(
        'D:\\Users\\lu\\Documents\\WeChat Files\\wxid_ah9mt1pem9x812\\FileStorage\\File\\2020-08\\0819李宁发布链接汇总-已更新数据.xlsx')
    # 通过excel表格名称(rank)获取工作表
    sheet = wb.sheet_by_name('KOL')
    dat = []  # 创建空list
    # 循环读取表格内容（每次读取一行数据）
    for item in range(sheet.nrows):
        cells = sheet.row_values(item)  # 每行数据赋值给cells
        # 因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
        url = cells[7]
        print(url)
    return dat


excel()
