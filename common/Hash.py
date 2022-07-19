import base64
import hashlib
import os
import random
import time


class GetHash:

    @staticmethod
    def Base64(name):
        Name = name.encode('utf-8')
        # name_bs64 = str(base64.b64encode(Name))
        name_bs64 = str(base64.b64encode(Name))[2:-1]
        name_bs64 = name_bs64.replace('=','-')
        # print(name_bs64)
        return name_bs64

    @staticmethod
    def Base64Hash():
        tmp = os.urandom(13)
        secret_key = base64.b64encode(tmp)
        secret_key = str(secret_key)[2:-3]
        return secret_key

    @staticmethod
    def secret_key(length=16, allowed_chars=None, secret_key=None):
        """
        生成随机字符串
        :param length: 随机字符串长度
        :param allowed_chars: 随机字符串字符取值范围
        :param secret_key: 生成随机字符串的随机字符串
        :return:
        """
        if secret_key is None:
            secret_key = "n96pwzsjtqscs3l46k7ef80e7gxfvouf3yvz"
        if allowed_chars is None:
            allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

        random.seed(
            hashlib.sha256(
                ("%s%s%s" % (
                    random.getstate(),
                    time.time(),
                    secret_key)).encode('utf-8')
            ).digest())
        ret = ''.join(random.choice(allowed_chars) for i in range(length))
        return ret



if __name__ == '__main__':
    gethash = GetHash()
    base = GetHash.get_random_secret_key()
    print(base)
    print(len(base))