import json

import allure
import requests
from common import Log, Hash
from config import conf


class httpRequest:

    def __init__(self, env):
        self.log = Log.MyLog(__name__)
        # self.session = self.get_cookie_ganzhou() # 赣州
        if env == 7:
            self.session = self.get_guoxin_per_cookie_insight_HR(env)  # 东莞
        elif env == 13:
            self.session = self.get_cookie_dhr(env)  # 东莞
        else:
            self.session = self.get_cookie_insight_HR(env)  # 东莞
        self.boundary = '----WebKitFormBoundary' + str(Hash.GetHash().secret_key())

    def change_header(self, head, value):
        self.session.headers[head] = value

    def get_cookie_dhr(self, env):
        session = requests.session()
        login_url = conf.confLogin(env)['host'] + conf.confLogin(env)['logon']
        session.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        session.headers['Authorization'] = conf.confLogin(env)['Authorization']
        # session.headers['User-Agent'] = conf.confLogin(env)['UserAgent']
        try:
            res = session.post(login_url, data=conf.confLogin(env)['param'], timeout=(10, 20))
            print(f'登录res.json：{res.json()}')
            session.headers['Authorization'] = 'Bearer' + ' ' + res.json()['data']['access_token']
            self.log.info('系统登陆成功。{}'.format(res.text))
            return session
        except Exception as e:
            self.log.error('登陆异常！：{}'.format(e))
            return False

    def get_cookie_ganzhou(self):
        '''获取cookie'''
        session = requests.session()
        login_url = conf.confLogin(2)['host'] + conf.confLogin(2)['logon']
        session.headers['Content-Type'] = 'application/json;charset=UTF-8'
        try:
            res = session.post(login_url, json=conf.confLogin(2)['param'], timeout=(10, 20))
            session.headers['Set-Cookie'] = '{}'.format(res.headers.get('Set-Cookie'))
            self.log.info('系统登陆成功。{}'.format(res.text))
            return session
        except Exception as e:
            self.log.error('登陆异常！：{}'.format(e))
            return False
            # return e

    def get_cookie_insight_HR(self, env):
        session = requests.session()
        login_url = conf.confLogin(env)['host'] + conf.confLogin(env)['logon']
        session.headers['Content-Type'] = 'application/json;charset=UTF-8'
        session.headers['Authorization'] = conf.confLogin(env)['Authorization']
        # session.headers['User-Agent'] = conf.confLogin(env)['UserAgent']
        try:
            res = session.post(login_url, timeout=(10, 20))
            print(f'登录res.json：{res.json()}')
            session.headers['Authorization'] = res.json()['token_type'].capitalize() + ' ' + res.json()['access_token']
            self.log.info('系统登陆成功。{}'.format(res.text))
            return session
        except Exception as e:
            self.log.error('登陆异常！：{}'.format(e))
            return False

    def get_guoxin_per_cookie_insight_HR(self, env):
        session = requests.session()
        login_url = conf.confLogin(env)['host'] + conf.confLogin(env)['logon']
        param = conf.confLogin(env)['param']
        session.headers['Content-Type'] = 'application/json;charset=UTF-8'
        # session.headers['Authorization'] = conf.confLogin(env)['Authorization']
        # session.headers['User-Agent'] = conf.confLogin(env)['UserAgent']
        try:
            if type(param) is str:  # 类型是字符串时再转
                param = json.loads(param)  # 字符串转字典
            res = session.post(login_url, json=param, timeout=(10, 20))
            # session.headers['token'] = res.json()['token_type'].capitalize() + ' ' + res.json()['access_token']
            # print(f'人员系统登录后data:{token}')
            # session.headers['token'] = res.json()['data']
            self.log.info('系统登陆成功。{}'.format(res.text))
            # 将token存储起来
            respInfo = json.loads(res.text)
            # yaml
            return session
        except Exception as e:
            self.log.error('登陆异常！：{}'.format(e))
            return False

    def get_request(self, url, **kwargs):
        '''get请求'''
        try:
            self.session.headers['Content-Type'] = 'application/json;charset=UTF-8'
            response = self.session.get(url, **kwargs, timeout=(10, 20))
            self.log.info('接口：{0}, 响应：{1}'.format(url, response.text))
            return response
        except Exception as e:
            self.log.error('异常的get请求url:{0}'.format(e))
            return e
        #
        # # 后续要增加接口请求超时自动跳过且抛异常
        # time_total = response.elapsed.total_seconds() # 响应时间：秒
        # time_consuming = response.elapsed.microseconds / 1000 # 响应时间：毫秒

    # 普通的只有file的form请求
    def post_files_request(self, url, filePath,
                           content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', *args,
                           **kwargs):
        '''post请求---application/json'''
        try:
            self.session.headers['Content-Type'] = 'multipart/form-data; boundary=' + self.boundary
            res = self.session.post(url, data=self.form_boundary(filePath, content_type), timeout=(10, 20))
            response = res.json()
            with allure.step('上传附件, {}'.format(response)):
                self.log.info('上传附件, {}'.format(response))
            self.log.info('接口：{0}, 响应：{1}'.format(url, response))
            return response['data']
        except Exception as e:
            self.log.error('异常的post-json请求url:{0}'.format(e))
            return e

    # 包含planId的form请求
    def post_files_plan_request(self, url, filePath, planId, *args, **kwargs):
        '''post请求---application/json'''
        try:
            self.session.headers['Content-Type'] = 'multipart/form-data; boundary=' + self.boundary
            res = self.session.post(url, data=self.form_boundary_model(filePath, planId), timeout=(10, 20))
            response = res.json()
            # assert 'fileId' in response['data'], '上传失败！, : {}'.format(response)
            with allure.step('上传附件, {}'.format(response)):
                self.log.info('上传附件, {}'.format(response))
            self.log.info('接口：{0}, 响应：{1}'.format(url, response))
            return response['data']
        except Exception as e:
            self.log.error('异常的post-json请求url:{0}'.format(e))
            return e

    def post_json_request(self, url, *args, **kwargs):
        '''post请求---application/json'''
        try:
            self.session.headers['Content-Type'] = 'application/json;charset=UTF-8'
            response = self.session.post(url, *args, **kwargs, timeout=(10, 5000))
            if response.request.body:
                body = response.request.body.decode('unicode_escape')
            else:
                body = None
            with allure.step('接口: {}'.format(url)):
                with allure.step('参数: {}'.format(body)):
                    with allure.step('响应: {}'.format(response.text)):
                        self.log.info('接口：{0}, 参数：{1}, 响应：{2}'.format(url, body, response.text))
            return response
        except Exception as e:
            self.log.error('异常的post-json请求url:{0}'.format(e))
            return e
        # time_total = response.elapsed.total_seconds()
        # time_consuming = response.elapsed.microseconds / 1000

    def post_form_request(self, url, *args, **kwargs):
        '''post请求---application/x-www-form-urlencoded'''
        try:
            self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
            response = self.session.post(url, *args, **kwargs, timeout=(10, 20))
            response.encoding = response.apparent_encoding
            body = response.request.body
            self.log.info('接口：{0}, 响应：{1}'.format(url, response.text))
            # self.log.info('接口：{0}, 参数：{1}'.format(url, body))
            return response
        except Exception as e:
            self.log.error('异常的post-from请求url:{0}'.format(e))
            return e
        # time_total = response.elapsed.total_seconds()
        # time_consuming = response.elapsed.microseconds / 1000

    def put_request(self, url, *args, **kwargs):
        '''put请求'''
        try:
            self.session.headers['Content-Type'] = 'application/json;charset=UTF-8'
            response = self.session.put(url, *args, **kwargs, timeout=(10, 20))
            self.log.info('接口：{0}, 响应：{1}'.format(url, response.text))
            return response
        except Exception as e:
            self.log.error('异常的post-from请求url:{0}'.format(e))
            return e

    def delete_request(self, url, **kwargs):
        '''delete请求'''
        try:
            self.session.headers['Content-Type'] = 'application/json;charset=UTF-8'
            response = self.session.delete(url, **kwargs, timeout=(10, 50000))
            body = response.request.body.decode('unicode_escape')
            self.log.info('接口：{0}, 参数：{1}, 响应：{2}'.format(url, body, response.text))
            return response
        except Exception as e:
            self.log.error('异常的delete请求url:{0}'.format(e))
            return e

    # 上传文件
    def form_boundary(self, filePath, content_type):
        from collections import OrderedDict
        from urllib3 import encode_multipart_formdata
        with open(filePath, 'rb') as f:
            params = OrderedDict([("file", (filePath.split('/')[-1], f.read(),
                                            content_type))])
            m = encode_multipart_formdata(params, boundary=self.boundary)
            # print(m[0])
        return m[0]

    # 上传excel模板
    def form_boundary_model(self, filePath, planId):
        from collections import OrderedDict
        from urllib3 import encode_multipart_formdata
        with open(filePath, 'rb') as f:
            params = OrderedDict([("planId", (None, planId)), ("file", (filePath.split('/')[-1], f.read(),
                                                                        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))])
            m = encode_multipart_formdata(params, boundary=self.boundary)
            # print(m[0])
        return m[0]

    def post_files_param_request(self, url, filePath, tmpFileType, *args, **kwargs):
        '''post请求---application/json'''
        try:
            self.session.headers['Content-Type'] = 'multipart/form-data; boundary=' + self.boundary
            res = self.session.post(url, data=self.form_boundary_model1(filePath, tmpFileType), timeout=(10, 20))
            response = res.json()
            # assert 'fileId' in response['data'], '上传失败！, : {}'.format(response)
            with allure.step('上传附件, {}'.format(response)):
                self.log.info('上传附件, {}'.format(response))
            self.log.info('接口：{0}, 响应：{1}'.format(url, response))
            return response
        except Exception as e:
            self.log.error('异常的post-json请求url:{0}'.format(e))
            return e

    def form_boundary_model1(self, filePath, tmpFileType):
        from collections import OrderedDict
        from urllib3 import encode_multipart_formdata
        with open(filePath, 'rb') as f:
            if tmpFileType:
                params = OrderedDict([("uploadFile", (filePath.split('/')[-1], f.read(),
                                                      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))])
            else:
                params = OrderedDict(
                    [("tmpFileType", (None, tmpFileType)), ("uploadFile", (filePath.split('/')[-1], f.read(),
                                                                           'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))])
            m = encode_multipart_formdata(params, boundary=self.boundary)
            print(m[0])
        return m[0]

    # ****************************************国信*************************************************
    def guoxin_per_post_json_request(self, url, token, *args, **kwargs):
        '''post请求---application/json'''
        try:
            self.session.headers['Content-Type'] = 'application/json;charset=UTF-8'
            if len(token) > 0:
                self.session.headers['token'] = token
            response = self.session.post(url, *args, **kwargs, timeout=(10, 5000))
            if response.request.body:
                body = response.request.body.decode('unicode_escape')
            else:
                body = None
            with allure.step('接口: {}'.format(url)):
                with allure.step('参数: {}'.format(body)):
                    with allure.step('响应: {}'.format(response.text)):
                        self.log.info('接口：{0}, 参数：{1}, 响应：{2}'.format(url, body, response.text))
            return response
        except Exception as e:
            self.log.error('异常的post-json请求url:{0}'.format(e))
            return e
        # time_total = response.elapsed.total_seconds()
        # time_consuming = response.elapsed.microseconds / 1000


if __name__ == '__main__':
    httpRequest().form_boundary()
    pass
    # get_cookie()
    # A = httpclient()
    # A.get_request('1',header=None)
