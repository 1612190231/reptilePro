import FileUtil
import CookieFollow
import EntryUrlUtil
import DictCloudUtil
import ReptileAppUtil
import FileApp
import FileAppComment


def main():
    # 淘宝comment
    url = EntryUrlUtil.get_input("淘宝评论Reptile", "示例：https://rate.tmall.com/list_detail_rate.htm?itemId=602659642364&sellerId=1917047079")
    # 小红书小程序search
    # url = "https://www.xiaohongshu.com/fe_api/burdock/weixin/v2/search/notes?keyword=%E5%AE%8C%E7%BE%8E%E6%97%A5%E8%AE%B0&sortBy=hot_desc&page=6&pageSize=20&needGifCover=true"
    # 小红书小程序comment
    # url = "https://www.xiaohongshu.com/fe_api/burdock/weixin/v2/notes/5f11e1d2000000000101d951/comments?pageSize=10"
    print(url)
    # self.url = MutualUtil.mutual_operation(root)
    # self.url = "https://rate.tmall.com/list_detail_rate.htm?itemId=602659642364&sellerId=1917047079"
    # self.url = "https://www.baidu.com"

    # 淘宝
    cookie = CookieFollow.get_cookie(url)
    file = FileUtil.get_file(url, cookie)
    print(file)
    DictCloudUtil.get_cloud(file)

    # 小红书小程序search
    # result = ReptileAppUtil.get_content(url)
    # print(result)
    # FileApp.get_file(result)

    # 小红书小程序comments
    # result = ReptileAppUtil.get_content(url)
    # file = FileAppComment.get_file(result)
    # DictCloudUtil.get_cloud(file)

    return 0


if __name__ == "__main__":
    main()

