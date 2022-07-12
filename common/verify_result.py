def common_assert(expect_result, response):
    """
    功能：断言响应结果
    :param expect_result: 预期结果
    :param response: 响应结果对象
    :return: None
    """

    # 断言
    json_data = response.json()
    assert 200 == response.status_code
    assert expect_result.get('success') == json_data.get("success")
    assert expect_result.get('code') == json_data.get("code")
    assert expect_result.get('message') in json_data.get("message")  # 右边包含左边
