# 1. 导包
import logging
import pytest

# 2. 自定义测试类
# 注意: 必须继承自 unittest.TestCase
from api.login_api import LoginApi
from common.read_data import build_data
from common.verify_result import common_assert
from config import BASE_DIR


class TestLogin:
    """测试类"""

    # 3. 自定义测试方法
    @pytest.mark.parametrize('desc, body, expect_result', build_data(BASE_DIR + '/data/login.json'))
    def test_login(self, desc, body, expect_result):
        print(desc, body, expect_result)
        print(f'【{desc}】接口测试')
        logging.info(f'【{desc}】接口测试')

        # 发送请求
        # 实例化对象，调用方法
        login_api = LoginApi()
        response = login_api.login(body)

        # 断言
        json_data = response.json()
        print("json_data =", json_data)
        logging.info(f'json data ={json_data}')

        # assert 200 == response.status_code
        # assert expect_result.get('success') == json_data.get("success")
        # assert expect_result.get('code') == json_data.get("code")
        # assert expect_result.get('message') in json_data.get("message")  # 右边包含左边
        common_assert(expect_result, response)
