import requests
import config


class EmpApi:
    def __init__(self):
        # 实例属性，网址
        self.emp_url = config.URL + "/api/sys/user"

    def query_emp(self, query, headers):
        """
        功能：查询指定id的员工
        :param query: 员工的id号
        :param headers: 请求头
        :return: 响应对象
        """
        return requests.get(self.emp_url + '/' + query, headers=headers)

    def modify_emp(self, body, query, headers):
        """
        功能：修改指定id的员工
        :param body: 修改员工的请求体
        :param query: 员工的id号
        :param headers: 请求头
        :return: 响应对象
        """
        return requests.put(self.emp_url + '/' + query, json=body, headers=headers)

    def delete_emp(self, query, headers):
        """
        功能：删除指定id的员工
        :param query: 员工的id号
        :param headers: 请求头
        :return: 响应对象
        """
        return requests.delete(self.emp_url + '/' + query, headers=headers)

    def add_emp(self, body, headers):
        """
        功能：添加员工
        :param body: 添加员工的请求体
        :param headers: 请求头
        :return: 响应对象
        """
        return requests.post(self.emp_url, json=body, headers=headers)
