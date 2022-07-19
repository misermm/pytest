import json
import requests
from common import Log
from common import Assert
from config import conf

class httpclient:

    test = Assert.Assertions()
    log = Log.MyLog(__name__)

    def get_cookie(self, data):
        '''获取cookie'''
        header = {'Content-Type': 'application/json'}
        url = conf.host + "/eHR/mvc/login/logon"
        try:
            res = requests.post(url, json=data, headers=header, timeout=10)
            cookie = res.headers.get('Set-Cookie')
            # print(cookie)
            return cookie
        except BaseException:
            self.log.error('get_cookie:error!')

    def get_request(self,url, header, param=None,**kwargs):
        '''get请求'''
        try:
            if param is None:
                response = requests.get(url = url, headers = header)
            else:
                response = requests.get(url = url, headers = header, params= param)
            return response
        except Exception as e:
            self.log.error('异常的get请求url:{0}'.format(url))
            self.log.error('RequestException Info: %s' % e)
            return

        # 后续要增加接口请求超时自动跳过且抛异常
        # time_total = response.elapsed.total_seconds() # 响应时间：秒
        # time_consuming = response.elapsed.microseconds / 1000 # 响应时间：毫秒

    def post_json_request(self, url, *args, **kwargs):
        '''post请求---application/json'''
        try:
            response = requests.post(url, *args, **kwargs, timeout=(10, 5000))
            return response
        except Exception as e:
            self.log.error('异常的post-json请求url:{0}'.format(url))
            self.log.error('RequestException Info: %s' % e)
            return

        # time_total = response.elapsed.total_seconds()
        # time_consuming = response.elapsed.microseconds / 1000

    def post_form_request(self, url, *args, **kwargs):
        '''post请求---application/x-www-form-urlencoded'''
        # try:
        #     if data is None:
        #         response = requests.post(url = url, headers = header)
        #     else:
        #         response = requests.post(url = url, data = data, headers = header)
        #     return response
        # except Exception as e:
        #     self.log.error('异常的post-from请求url:{0}'.format(url))
        #     self.log.error('RequestException Info: %s' % e)
        #     return
        try:
            # self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
            response = requests.post(url, *args, **kwargs)
            self.log.info('接口：{0}, 响应：{1}'.format(url, response.text))
            return response
        except Exception as e:
            self.log.error('异常的post-from请求url:{0}'.format(e))
            return e

        # time_total = response.elapsed.total_seconds()
        # time_consuming = response.elapsed.microseconds / 1000


if __name__ == '__main__':
    # pass
    get_cookie()
    # A = httpclient()
    # A.get_request('1',header=None)