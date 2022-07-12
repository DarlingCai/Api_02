# 1. 导包
from api.emp_api import EmpApi
from api.login_api import LoginApi
from common.db_util import DBUtil


# 2. 自定义测试类
class TestEmp:
    """测试类"""
    # 类属性
    mobile = '11122223333'  # 手机号
    headers = None

    def setup_class(self):
        print('类前置：清理数据')

        # 删除
        sql = f"delete from bs_user where mobile='{self.mobile}'"
        n = DBUtil.iud_data(sql)
        print(n)

        print('类前置：获取token，清理数据')
        body = {
            "mobile": "13800000002",
            "password": "123456"
        }

        # 获取登陆成功的认证请求头
        login_api = LoginApi()  # 实例化对象
        TestEmp.headers = login_api.get_au_headers(body)  # 实例化对象调用实例方法
        print(f'headers = {TestEmp.headers}')

    def teardown_class(self):
        print('类后置：清理数据')
        # 删除
        sql = f"delete from bs_user where mobile='{self.mobile}'"
        n = DBUtil.iud_data(sql)
        print(n)

    # 3. 自定义测试方法
    def test_emp(self):
        # 实例化员工管理API对象
        emp_api = EmpApi()

        # 1. 添加员工(手机号唯一)，断言
        body = {"username": "mikejiang",
                "mobile": self.mobile,
                "timeOfEntry": "2021-08-02",
                "formOfEmployment": 1,
                "workNumber": "001",
                "departmentName": "偷偷学习组",
                "departmentId": "1422400509205118976",
                "correctionTime": "2021-08-30T16:00:00.000Z"}

        # 发送请求
        response = emp_api.add_emp(body, self.headers)
        json_data = response.json()
        print(f'添加员工：{json_data}')

        # 断言
        assert 200 == response.status_code
        assert json_data.get("success")
        assert 10000 == json_data.get("code")
        assert "操作成功" in json_data.get("message")

        # 提取员工id
        query = json_data.get('data').get('id')
        print(f'员工id：{query}')

        # 2. 查询员工，断言
        # 发请求
        response = emp_api.query_emp(query, self.headers)
        json_data = response.json()
        print(f'查询员工：{json_data}')
        # 断言
        assert 200 == response.status_code
        assert json_data.get("success")
        assert 10000 == json_data.get("code")
        assert "操作成功" in json_data.get("message")

        # 3. 修改员工，断言
        # 发请求
        body = {"username": "yyds"}
        response = emp_api.modify_emp(body, query, self.headers)
        json_data = response.json()
        print(f'修改员工：{json_data}')
        # 断言
        assert 200 == response.status_code
        assert json_data.get("success")
        assert 10000 == json_data.get("code")
        assert "操作成功" in json_data.get("message")

        # 4. 删除员工，断言
        # 发请求
        response = emp_api.delete_emp(query, self.headers)
        json_data = response.json()
        print(f'删除员工：{json_data}')
        # 断言
        assert 200 == response.status_code
        assert json_data.get("success")
        assert 10000 == json_data.get("code")
        assert "操作成功" in json_data.get("message")
