import json
from copy import deepcopy

def read_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def get_data_from_json(filepath):
    """
    统一的测试数据读取器
    :param filepath: json文件路径
    :return: 每条用例为dict的list，自动添加case_id，expect_result兼容处理
    """
    datas = read_json(filepath)
    arrs = []
    for case_id, data in datas.items():
        case_data = deepcopy(data)
        case_data["case_id"] = case_id
        # expect_result兼容处理
        expect_result = case_data.get('expect_result')
        if isinstance(expect_result, str) and '&' in expect_result:
            case_data['expect_result'] = expect_result.split('&')
        arrs.append(case_data)
    return arrs


if __name__ == '__main__':
    print(get_data_from_json())
