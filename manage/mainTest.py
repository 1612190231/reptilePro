from reptilePro.files import fileWeb
from reptilePro.utils import cookieUtil
from reptilePro.utils import entryUtil
from reptilePro.utils import dictCloudUtil
from reptilePro.reptiles import reptileApp
from reptilePro.files import fileJD
from reptilePro.files import fileApp
from reptilePro.files import fileAppComment


def main():
    # 淘宝comment
    url = entryUtil.get_input("淘宝评论Reptile",
                                 "示例：https://rate.tmall.com/list_detail_rate.htm?itemId=602659642364&sellerId=1917047079")
    # 京东comment
    # url = entryUtil.get_input("京东评论Reptile",
    #                              "示例：https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=66500623031&score=0&sortType=5&pageSize=10")
    # 小红书小程序search
    # url = "https://www.xiaohongshu.com/fe_api/burdock/weixin/v2/search/notes?keyword=%E5%AE%8C%E7%BE%8E%E6%97%A5%E8%AE%B0&sortBy=hot_desc&page=6&pageSize=20&needGifCover=true"
    # 小红书小程序comment
    # url = "https://www.xiaohongshu.com/fe_api/burdock/weixin/v2/notes/5f11e1d2000000000101d951/comments?pageSize=10"
    print(url)

    # 淘宝
    cookie = cookieUtil.get_cookie(url)
    file = fileWeb.get_file(url, cookie)
    print(file)
    dictCloudUtil.get_cloud(file)

    # 京东
    # page = 10
    # file = fileJD.get_file(url, page)
    # dictCloudUtil.get_cloud(file)

    # 小红书小程序search
    # result = reptileAppUtil.get_content(url)
    # print(result)
    # fileApp.get_file(result)

    # 小红书小程序comments
    # result = reptileAppUtil.get_content(url)
    # file = fileAppComment.get_file(result)
    # dictCloudUtil.get_cloud(file)

    return 0


if __name__ == "__main__":
    main()

