import time

import requests

import api
from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiApp:

    # 初始化
    def __init__(self):
        # 登录url
        self.url_login = api.host + "/app/v1_0/authorizations"
        log.info("正在初始化app登录url: {}".format(self.url_login))
        # 查询文章url
        self.url_article = api.host + "/app/v1_0/articles"
        log.info("正在初始化app查询文章url: {}".format(self.url_login))

    # 登录
    def api_app_login(self, mobile, code):
        data = {"mobile": mobile, "code": code}
        log.info("正在调用app登录接口，请求数据为: {}".format(data))
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 查询频道下所有文章
    def api_app_article(self):
        """
        :param channel_id: 频道id
        :param timestamp: 时间戳 单位毫秒
        :param with_top: 文章置顶 1：包含 0：不包含
        :return: 相应对象
        """
        # with_top: 1 为包含置顶，0 为不包含置顶
        data = {"channel_id": api.channel_id, "timestamp": int(time.time()), "with_top": 1}
        log.info("正在调用app查询频道下文章接口，请求数据为: {}".format(data))
        return requests.get(url=self.url_article, params=data, headers=api.headers)


