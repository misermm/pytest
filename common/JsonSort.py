# @Time : 2021/5/28 14:00
# @Author : Daichenlei
# json排序
import json

def sortJson(value):
    sortValue = sorted(value, key=lambda value: value, reverse=False)
    sortDict = {}
    for val in sortValue:
        sortDict[val] = value[val]
    print(sortDict)

  # 读取json文件内容,返回字典格式
def readJson(filePath):
  with open(filePath, 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
    return json_data

  # 将字典数据写入到json文件中
def writeJson(filePath, dict1):
  with open(filePath, 'a', encoding='utf8') as fp:
    json.dump(dict1, fp, ensure_ascii=False)
    #  如果ensure_ascii ' '为false，则返回值可以包含非ascii值

# 根据list中的json的某个key排序list
def sortJsonInList(JsonInList, key):
    # [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}]
    import operator
    sorted_x = sorted(JsonInList, key=operator.itemgetter(key))
    return sorted_x

if __name__ == '__main__':
  filePath1 = r'D:\code\Text\datas\test\1.json'
  filePath2 = r'D:\code\Text\datas\test\2.json'
  get = readJson(filePath1)
  post = readJson(filePath2)
  sortJson(get)
  sortJson(post)
