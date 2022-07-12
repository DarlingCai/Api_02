# 1. 导包
from api.login_api import LoginApi
import logging


# 2. 自定义测试类
class TestLogin:
    """测试类"""

    # 3. 自定义测试方法
    def test01_login_success(self):
        # 测试数据
        body = {
            "mobile": "13800000002",
            "password": "123456"
        }
        # 发送请求
        # 实例化对象
        login_api = LoginApi()
        # 实例对象调用实例方法，获取响应对象
        response = login_api.login(body)

        # 断言
        json_data = response.json()
        print(f'json_data = {json_data}')
        logging.info(f'json_data = {json_data}')
        assert 200 == response.status_code
        assert json_data.get("success")
        assert 10000 == json_data.get("code")
        assert "操作成功" in json_data.get("message")

    def test02_user_err(self):
        # 测试数据
        body = {
            "mobile": "13800003442",
            "password": "123456"
        }
        # 发送请求
        # 实例化对象
        login_api = LoginApi()
        # 实例对象调用实例方法，获取响应对象
        response = login_api.login(body)
        # 断言
        json_data = response.json()
        print("json_data =", json_data)
        logging.info(f'json_data = {json_data}')
        assert 200 == response.status_code
        assert not json_data.get("success")
        assert 20001 == json_data.get("code")
        assert "错误" in json_data.get("message")

    def test03_pwd_err(self):
        # 测试数据
        body = {
            "mobile": "13800000002",
            "password": "123abc"
        }
        # 发送请求
        # 实例化对象
        login_api = LoginApi()
        # 实例对象调用实例方法，获取响应对象
        response = login_api.login(body)

        # 断言
        json_data = response.json()
        print("json_data =", json_data)
        logging.info(f'json_data = {json_data}')
        assert 200 == response.status_code
        assert not json_data.get("success")
        assert 20001 == json_data.get("code")
        assert "错误" in json_data.get("message")
