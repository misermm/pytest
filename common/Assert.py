

from common import Log
import json, allure
import jsonpath

class Assertions:
    def __init__(self):
        self.log = Log.MyLog(__name__)

    # 断言2个字典中key相同的值是否相等
    def assert_result(self, except_dict, yaml_dict):
        assert_list = []  # 保存assertError信息
        for ikey, ivalue in except_dict.items():
            for dkey, dvalue in yaml_dict.items():
                if not isinstance(ikey, str):
                    if ikey == dkey:
                        result = self.assert_equal(yaml_dict[dkey], except_dict[ikey])
                        if True != result:
                            result.insert(0, ikey)
                            assert_list.append(result)
                else:
                    if ikey.upper() == dkey.upper():
                        result = self.assert_equal(yaml_dict[dkey], except_dict[ikey])
                        if True != result:
                            result.insert(0, ikey)
                            assert_list.append(result)
        if len(assert_list) == 0:
            with allure.step('所有断言通过。'):
               self.log.info('所有断言通过。')
        else:
            with allure.step('断言失败！:{}'.format(assert_list)):
                self.log.warning('断言失败！:{}'.format(assert_list))
                raise AssertionError('断言失败！:{}'.format(assert_list))
        # return assert_list

    # def assert_allure_show_error(self, assert_list):
    #     '''
    #     判断是否有AssertionError，有则抛出，体现在allure报告中
    #     :param assert_list: assert返回值
    #     :return:
    #     '''
    #     if len(assert_list) == 0:
    #         with allure.step('所有断言通过。'):
    #            self.log.info('所有断言通过。')
    #     else:
    #         with allure.step('断言失败！:{}'.format(assert_list)):
    #             self.log.warning('断言失败！:{}'.format(assert_list))
    #             raise AssertionError('断言失败！:{}'.format(assert_list))

    # 判断单个值是否相等
    def assert_allure_show(self, assert_list):
        '''
        判断是否有AssertionError，有则抛出，体现在allure报告中
        :param assert_list: assert返回值
        :return:
        # assert_list = []  # 保存assertError信息
                        # assert_list.append(self.assert_.assert_equal(data_people['name'], 1))
                        # assert_list.append(self.assert_.assert_equal(data_people['name'], name))
                        # assert_list.append(self.assert_.assert_equal(data_people['name'], 2))
                        # # 判断是否有AssertionError，有则抛出，体现在allure报告中
                        # self.assert_.assert_allure_show(assert_list)
        '''
        if True not in assert_list:
            with allure.step('所有断言失败:{}'.format(assert_list)):
                self.log.error('所有断言失败:{}'.format(assert_list))
                raise AssertionError('所有断言失败:{}'.format(assert_list))
        else:
            result = []
            for i in assert_list:
                if i != True:
                    result.append(i)
                else:
                    pass
            if len(result) == 0:
                with allure.step('所有断言通过。'):
                   self.log.info('所有断言通过。')
            else:
                with allure.step('断言失败！:{}'.format(result)):
                    self.log.warning('断言失败！:{}'.format(result))
                    raise AssertionError('断言失败！:{}'.format(result))



        # for assertError in assert_list:
        #     if True == assertError:
        #         assert_list.remove(assertError)
        #     if len(assert_list) == 1 and assertError == True:
        #         with allure.step('所有断言通过'):
        #             self.log.info('所有断言通过')
        #     else:
        #         self.log.info(assertError)
        #     # if isinstance(assertError, AssertionError):
        # if True not in assert_list:
        #     with allure.step('断言失败:{}'.format(assert_list)):
        #         raise AssertionError('断言失败:{}'.format(assert_list))

    def assert_equal(self, expected_value, value):
        """
        验证response状态码
        :param code:
        :param expected_value:
        :return:
        """
        try:
            assert str(expected_value) == str(value)
            return True
        except AssertionError:
            # self.log.error("接口：{0}。statusCode error, expected_code is {1}, statusCode is {2}".format(ApiName, expected_code, code))
            with allure.step("Assert error：expected_value is {0}, value is {1}".format(expected_value, value)):
                self.log.error("Assert error：expected_value is {0}, value is {1}".format(expected_value, value))
            return [expected_value, value]
        except Exception as e:
            self.log.error(e)
            # raise

    def assert_in(self, expected_value, value):
        """
        验证response状态码
        :param code:
        :param expected_value:
        :return:
        """
        try:
            assert expected_value in value
            return True
        except AssertionError:
            # self.log.error("接口：{0}。statusCode error, expected_code is {1}, statusCode is {2}".format(ApiName, expected_code, code))
            with allure.step("Assert in error：expected_value is {0}, value is {1}".format(expected_value, value)):
                self.log.error("Assert in error：expected_value is {0}, value is {1}".format(expected_value, value))
            return (expected_value, value)
        except Exception as e:
            self.log.error(e)
            # raise

    def assert_body_json(self, body, expr, expected_msg, ApiName):
        """
        响应体为json格式，验证response body中任意属性的值
        :param body:
        :param expr:
        :param expected_msg:
        :return:
        """
        try:
            msg = jsonpath.jsonpath(body, expr) # 返回值是列表类型
            msg = ''.join('%s' %id for id in msg)
            assert msg == expected_msg
            return True

        except:
            self.log.error("接口：{0}。Response body msg != expected_msg, expected_msg is {1}, msg is {2}， body is {3}".format(ApiName, expected_msg, msg, body))
            raise

    def assert_in_json(self, body, expected_msg, ApiName):
        """
        响应体为json格式，验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            self.log.error("接口：{0}。Response body Does not contain expected_msg, expected_msg is {1}" .format(ApiName, expected_msg))
            raise

    def assert_in_text(self, body, expected_msg, ApiName):
        """
        响应体为非json格式，验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body in expected_msg
            return True

        except:
            self.log.error("接口：{0}。Response body != expected_msg, expected_msg is {1}, body is {2}".format(ApiName, expected_msg, body))
            raise

    def assert_text(self, body, expected_msg, ApiName):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            self.log.error("接口：{0}。Response body != expected_msg, expected_msg is {1}, body is {2}".format(ApiName, expected_msg, body))
            raise

    def assert_time(self, time, expected_time, ApiName):
        """ 验证响应时间小于预期最大响应时间 """
        try:
            assert time < expected_time
            return True

        except:
            self.log.error("接口：{0}。Response time > expected_time, expected_time is {1}ms, time is {2}ms".format(ApiName, expected_time, time))
            raise


if __name__ == '__main__':
    # pass
    pass