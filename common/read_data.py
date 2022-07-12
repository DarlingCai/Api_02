import json


def build_data(filepath):
    """
    功能：读取json文件组装成[(), (), ()]格式的数据
    :param filepath: 指定处理的json文件
    :return: 组装完成的列表数据
    """
    # 1. 定义空列表
    case_data = []
    # 2. with open() 只读方式，打开文件，获取文件对象
    with open(filepath, 'r', encoding='utf-8') as f:
        # 3. 调用方法获取文件内容：读取的内容 = json.load(文件对象)
        json_data = json.load(f)
        # 4. 将获取的键值强制转换成元组，再追加到列表中
        for test_data in json_data:
            case_data.append(tuple(test_data.values()))

    return case_data

