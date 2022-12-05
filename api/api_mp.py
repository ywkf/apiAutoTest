import api
import requests

from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiMp:

    # 初始化
    def __init__(self):
        # 登录接口url
        self.url_login = api.host + "/mp/v1_0/authorizations"
        log.info("正在初始化自媒体登录url: {}".format(self.url_login))
        # 发布文章接口url
        self.url_article = api.host + "/mp/v1_0/articles"
        log.info("正在初始化自媒体发布文章url: {}".format(self.url_article))

    # 登录
    def api_mp_login(self, mobile, code):
        """
        :param mobile: 手机号
        :param code: 验证码
        :return: 响应对象
        """
        data = {"mobile": mobile, "code": code}
        log.info("正在调用自媒体登录接口，请求数据: {}".format(data))
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 发布文章
    def api_mp_article(self, title, content, channel_id):
        """
        :param title: 文章标题
        :param content: 文章内容
        :param channel_id: 频道id
        :param cover: 封面 0：为自动
        :return: 响应对象
        """
        data = {"title": title, "content": content, "channel_id": channel_id, "cover": {"type": 0, "image": []}}
        log.info("正在调用自媒体发布文章接口，请求数据: {}".format(data))
        return requests.post(url=self.url_article, json=data, headers=api.headers)