from reptilePro.reptiles import reptileWeb
import time
import tkinter.filedialog
import random


def get_file(result):
    # # 新建excel文档
    # # 创建一个workbook 设置编码
    # workbook = xlwt.Workbook(encoding='utf-8')
    # # 创建一个worksheet
    # worksheet = workbook.add_sheet('TaoBaoComment')

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    file_url = '..\\data\\comments\\comment-XHS'
    file_name = tkinter.filedialog.asksaveasfilename(initialfile='comment-' + now, filetypes=[('txt', '*.txt')],
                                                     initialdir=file_url)
    file_name = file_name + '.txt'

    with open(file_name, 'a', encoding='utf-8') as file:
        # print(result)
        # 写入excel
        for items in range(0, 10):
            # 参数对应 行, 列, 值
            result_content = result["data"]["comments"][items % 10]["content"]
            file.write(''.join(result_content) + '\n')
            print(result_content)

    # 保存
    file.close()
    return file_name
