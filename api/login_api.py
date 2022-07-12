"""
类名：LoginApi
实例属性：
login_url：保存登陆的url，"http://ihrm-test.itheima.net/api/sys/login"
实例方法：
    def login(self, body)：
        # 功能：发送登陆请求
        # :param body: 发送请求的请求体
        # :return: 发送登陆请求后的响应对象
    def get_au_headers(self, body):
        # 功能：获取认证请求头
        # :param body: 登陆的请求体数据
        # :return: 成功登陆的认证请求头
"""

# 1. 导包
import requests

class LoginApi:
    def __init__(self):
        # 实例属性，登陆网址
        self.login_url = "http://ihrm2-test.itheima.net/api/sys/login"

    def login(self, body):
        """
        功能：发送登陆请求
        :param body: 发送请求的请求体
        :return: 发送登陆请求后的响应对象
        """
        return requests.post(self.login_url, json=body)

    def get_au_headers(self, body):
        """
        功能：获取认证请求头
        :param body: 登陆的请求体数据
        :return: 成功登陆的认证请求头
        """
        # 发送请求登陆请求
        response = self.login(body)
        json_data = response.json()
        print(f"json data = {json_data}")

        # 提取token
        token = json_data.get('data')

        # 设置认证请求头
        headers = {
            'Authorization': token
        }

        return headers
