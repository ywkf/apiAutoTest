import requests

import api
from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiMis:

    # 初始化
    def __init__(self):
        # 登录url
        self.url_login = api.host + "/mis/v1_0/authorizations"
        log.info("正在初始化后台管理登录url: {}".format(self.url_login))
        # 查询文章url
        self.url_search = api.host + "/mis/v1_0/articles"
        log.info("正在初始化后台管理查询文章url: {}".format(self.url_search))
        # 审核文章url
        self.url_audit = api.host + "/mis/v1_0/articles"
        log.info("正在初始化后台管理审核文章url: {}".format(self.url_audit))

    # 登录
    def api_mis_login(self, account, password):
        """
        :param account: 账号
        :param password: 密码
        :return: 响应对象
        """
        # 参数数据
        data = {"account": account, "password": password}
        log.info("正在调用后台管理登录接口，请求数据为: {}".format(data))
        # 调用post方法
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 查询文章
    def api_mis_search(self):
        """
        :param title: 文章标题
        :param channel: 文章所属频道
        :return: 响应对象
        """
        # 参数数据
        data = {"title": api.article_title, "channel": api.channel}
        log.info("正在调用后台管理查询文章接口，请求数据为: {}".format(data))
        # 调用get方法
        return requests.get(url=self.url_search, params=data, headers=api.headers)

    # 审核文章
    def api_mis_audit(self):
        """
        :param article_ids: 文章id，发布文章后服务器生成
        :param status: 2 为审核通过
        :return: 响应对象
        """
        # 参数数据
        data = {"article_ids": [api.article_id], "status": 2}
        log.info("正在调用后台管理审核文章接口，请求数据为: {}".format(data))
        # 调用put方法
        return requests.put(url=self.url_audit, json=data, headers=api.headers)


