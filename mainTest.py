import FileUtil
import CookieFollow
import EntryUrlUtil
import DictCloudUtil


def main():
    url = EntryUrlUtil.get_input("淘宝评论Reptile", "示例：https://rate.tmall.com/list_detail_rate.htm?itemId=602659642364&sellerId=1917047079")
    print(url)
    # self.url = MutualUtil.mutual_operation(root)
    # self.url = "https://rate.tmall.com/list_detail_rate.htm?itemId=602659642364&sellerId=1917047079"
    # self.url = "https://www.baidu.com"

    cookie = CookieFollow.get_cookie(url)
    file = FileUtil.get_file(url, cookie)
    # print(file)
    DictCloudUtil.get_cloud(file)


if __name__ == "__main__":
    main()

