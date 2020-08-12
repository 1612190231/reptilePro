import FileUtil
import CookieFollow
import EntryUrlUtil
import DictCloudUtil
import ReptileAppUtil


def main():
    # url = EntryUrlUtil.get_input("淘宝评论Reptile", "示例：https://rate.tmall.com/list_detail_rate.htm?itemId=602659642364&sellerId=1917047079")
    url = "https://edith.xiaohongshu.com/api/sns/v1/note/feed?note_id=5f29006200000000010063d6&page=1&num=5&fetch_mode=1&source=explore&ads_track_id=&fid=159722038710c6e963dbbad5fd42c77e0537628ea23b&device_fingerprint=20200613220359c4840fb1684bf704caef443a4283647201119f19be3f485e&device_fingerprint1=20200613220359c4840fb1684bf704caef443a4283647201119f19be3f485e&channel=HuaweiCloud&versionName=6.56.0&deviceId=3883749a-702f-3299-b9ca-4b5ce0645f15&platform=android&sid=session.1597220392759032153511&identifier_flag=4&t=1597221131&x_trace_page_current=explore_feed&lang=zh-Hans&uis=light HTTP/1.1"
    # print(url)
    # self.url = MutualUtil.mutual_operation(root)
    # self.url = "https://rate.tmall.com/list_detail_rate.htm?itemId=602659642364&sellerId=1917047079"
    # self.url = "https://www.baidu.com"

    # cookie = CookieFollow.get_cookie(url)
    # file = FileUtil.get_file(url, cookie)
    # # print(file)
    # DictCloudUtil.get_cloud(file)

    result = ReptileAppUtil.get_content(url)
    print(result)
    return 0


if __name__ == "__main__":
    main()

