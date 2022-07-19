
import yaml
from common import Log
#
# def get_test_data(test_data_path):
#     http = []  # 存储请求对象
#     expected = []  # 存储预期结果
#     try:
#         with open(test_data_path,encoding = 'utf-8') as f:
#             dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
#             test = dat['tests']
#             for td in test:
#                 http.append(td.get('http', {}))
#                 expected.append(td.get('expected', {}))
#         parameters = zip( http, expected)
#         list_params = list(parameters)
#         # print(list_params)
#         return list_params
#     except BaseException as e:
#         Log.MyLog().error("获取yaml数据错误！{0}".format(e))

def get_test_data(test_data_path):
    # for demo
    case = []  # 存储测试用例名称
    http = []  # 存储请求对象
    expected = []  # 存储预期结果
    with open(test_data_path,encoding = 'utf-8') as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = dat['tests']
        for td in test:
            case.append(td.get('case', ''))
            http.append(td.get('http', {}))
            expected.append(td.get('expected', {}))
    parameters = zip(case, http, expected)
    list_params = list(parameters)
    return case, list_params

if __name__ == '__main__':
    pass
    get_test_data(r'C:\Users\xumeng.it\PycharmProjects\ciic_api_env\datas\datas_Organization_management\test_getSysQueryPage1.yaml')