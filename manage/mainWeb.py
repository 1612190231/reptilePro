# from reptilePro.files import fileWeb
# from reptilePro.utils import cookieUtil
# from reptilePro.utils import entryUtil
# from reptilePro.utils import dictCloudUtil
# from reptilePro.reptiles import reptileApp
# from reptilePro.files import fileJD
# from reptilePro.files import fileApp
# from reptilePro.files import fileAppComment
from files import fileWeb
from utils import entryUtil, cookieUtil, dictCloudUtil


def main():
    # 淘宝comment
    url = entryUtil.get_input("淘宝评论Reptile",
                                 "示例：https://rate.tmall.com/list_detail_rate.htm?itemId=602659642364&sellerId=1917047079")
    print(url)

    # 淘宝
    cookie = cookieUtil.get_cookie(url)
    file = fileWeb.get_file(url, cookie)
    print(file)
    dictCloudUtil.get_cloud(file)

    return 0


if __name__ == "__main__":
    main()

