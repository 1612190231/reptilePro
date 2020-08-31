# from reptilePro.reptiles import reptileWeb
import time
import tkinter.filedialog
import random

from reptiles import reptileWeb


def get_file(url, cookie):
    # # 新建excel文档
    # # 创建一个workbook 设置编码
    # workbook = xlwt.Workbook(encoding='utf-8')
    # # 创建一个worksheet
    # worksheet = workbook.add_sheet('TaoBaoComment')

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    file_url = 'data\\comment'
    file_name = tkinter.filedialog.asksaveasfilename(initialfile='comment-' + now, filetypes=[('txt', '*.txt')],
                                                     initialdir=file_url)
    file_name = file_name + '.txt'

    with open(file_name, 'a', encoding='utf-8') as file:
        for current_page in range(1, 2):
            result = reptileWeb.get_content(url, cookie, current_page)
            time.sleep(random.random()*3)
            # if len(result['rgv587_flag']) != 0:
            #     time.sleep(5)
            #     cookie = cookieFollowUtil.get_cookie(url)
            #     result = reptileWeb.get_content(url, cookie, current_page)

            # print(result)
            # 写入excel
            for items in range((current_page-1)*20, (current_page-1)*20+20):
                # 参数对应 行, 列, 值
                result_content = result["rateDetail"]["rateList"][items % 20]["rateContent"]
                file.write(''.join(result_content) + '\n')
                print(result_content)

    # 保存
    file.close()
    return file_name

