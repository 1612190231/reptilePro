# from reptilePro.files import fileWeb
# from reptilePro.utils import cookieUtil
# from reptilePro.utils import entryUtil
# from reptilePro.utils import dictCloudUtil
# from reptilePro.reptiles import reptileApp
# from reptilePro.files import fileJD
# from reptilePro.files import fileApp
# from reptilePro.files import fileAppComment
from files import fileWeb, fileJD
from utils import entryUtil, cookieUtil, dictCloudUtil


def main():
    # 京东comment
    url = entryUtil.get_input("京东评论Reptile",
    "示例：https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=66500623031&score=0&sortType=5&pageSize=10")

    print(url)

    # 京东
    page = 10
    file = fileJD.get_file(url, page)
    dictCloudUtil.get_cloud(file)

    return 0


if __name__ == "__main__":
    main()

