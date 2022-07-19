import urllib.parse

# 数据http格式化
def http_parse(name):
    param = urllib.parse.quote(':' + name + '##')
    return param