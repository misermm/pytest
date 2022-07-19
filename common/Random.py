import random
import string
import time
from common import Log
import re
# 导入某个模块的部分类或方法
from datetime import datetime, timedelta, date
# 导入常量并重命名
from common import constant as const

# 随机手机号
def get_phone_num():
    second_spot = random.choice([3, 4, 5, 7, 8])
    third_spot = {3: random.randint(0, 9),
             4:  random.choice([5, 7, 9]),
             5: random.choice([i for i in range(10) if i != 4]),
             7: random.choice([i for i in range(10) if i not in [4, 9]]),
             8: random.randint(0, 9), }[second_spot]
    remain_spot = random.randint(9999999, 100000000)
    phone_num = "1{}{}{}".format(second_spot, third_spot, remain_spot)
    return phone_num

def floatNum(num, hao):
    if isinstance(num, str):
        num = eval(num)
    else:
        pass
    return num

def dateCompare(date1, date2, fmt='%Y-%m-%d'):
    """
    比较两个真实日期之间的大小，date1 > date2 则返回True, = 返回None，小于返回False
    """
    d1 = datetime.strptime(str(date1), fmt)
    d2 = datetime.strptime(str(date2), fmt)
    if d1>d2:
        return True
    elif d1 == d2:
        return None
    else:
        return False

def roundNum(_float, _len=2):
    """
    _float: float
    _len: int, 指定四舍五入需要保留的小数点后几位数为_len
    type ==> float, 返回四舍五入后的值
    """
    if isinstance(_float, float):
        if str(_float)[::-1].find('.') <= _len:
            return (_float)
        if str(_float)[-1] == '5':
            return (round(float(str(_float)[:-1] + '6'), _len))
        else:
            return (round(float(_float), _len))
    else:
        return (round(float(_float), _len))

# 随机银行卡号
def randomBankNum(name='工商银行', num=15):
    if num == 19:
        if name == '建设银行':
            bank = random.randrange(6227007201360049787, 6227007201360049987, 1)
        elif name == '招商银行':
            bank = random.randrange(6215593700011926793, 6215593700011926993, 1)
        elif name == '工商银行':
            bank = random.randrange(6212261001080775106, 6212261001080799999, 1)
        else:
            # name == '中国银行'
            bank = random.randrange(6217856200015168391, 6217856200015168591, 1)
    else:
        # num == 15:
        if name == '建设银行':
            bank = random.randrange(622700720130001, 622700720139999, 1)
        elif name == '招商银行':
            bank = random.randrange(621559370000001, 621559370009999, 1)
        elif name == '工商银行':
            bank = random.randrange(621226100100001, 621226100109999, 1)
        else:
            # name == '中国银行':
            bank = random.randrange(621785620000001, 621785620009999, 1)
    return str(bank)

# 获取当前时间
def get_time(timeStr):
  return datetime.now().strftime(timeStr)  # %Y-%m-%d %H:%M:%S.%f

# 昨天
def getYesterday():
  yesterday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
  return yesterday

# 明天
def getTomorrow():
  tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
  return tomorrow

# 计算两个日期间相差多少天
def dayToDay(date1, date2):
    import time
    import datetime
    # %Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
    # date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
    # date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
    date1 = time.strptime(date1, "%Y-%m-%d")
    date2 = time.strptime(date2, "%Y-%m-%d")
    # 根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
    # date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    # date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    if date1==date2:
        return 0
    else:
        # 返回两个变量相差的值，就是相差天数
        return abs(int(str(date2 - date1).split()[0]))

# 计算月份有多少天
def monthDays(year, month):
    import calendar
    a = calendar.monthrange(year, month)[1]
    return a

# 返回日期的月末日期
def monthEndDay(date):
    """
    年份 date(2017-09-08格式)
    :return:本月第一天日期和本月最后一天日期
    """
    import calendar
    date = date + '-11'
    if date.count('-') != 2:
        raise ValueError('- is error')
    year, month = str(date).split('-')[0], str(date).split('-')[1]
    end = calendar.monthrange(int(year), int(month))[1]
    start_date = '%s-%s-01' % (year, month)
    end_date = '%s-%s-%s' % (year, month, end)
    return str(end_date)

def choice_data(data):
  """ 获取data数组中，随机整型数据 """
  _list = data.split(",")
  num = random.choice(_list)
  return num


def random_float(data):
  """ 获取data范围内，随机浮点型数据 """
  try:
    start_num, end_num, accuracy = data.split(",")
    start_num = float(start_num)
    end_num = float(end_num)
    accuracy = int(accuracy)
    if start_num <= end_num:
      num = random.uniform(start_num, end_num)
    else:
      num = random.uniform(end_num, start_num)
    num = round(num, accuracy)
    return num
  except BaseException as e:
    Log.MyLog(__name__).error("调用{0}-{1}范围内的{2}位随机浮点数失败，{3}".format(start_num, end_num, accuracy, e))
    raise


def random_int(scope):
  """ 获取scope范围内，随机整型数据 """
  try:
    start_num, end_num = scope.split(",")
    start_num = int(start_num)
    end_num = int(end_num)
    if start_num <= end_num:
      num = random.randint(start_num, end_num)
    else:
      num = random.randint(end_num, start_num)
    return num
  except BaseException as e:
    Log.MyLog(__name__).error("调用{0}范围内的随机整数失败，{1}".format(scope, e))
    raise


"""
string的常用属性
string.ascii_letters  输出所有字母的字符串
string.ascii_lowercase  输出所有小写字母的字符串
string.ascii_uppercase  输出所有大写字母的字符串
string.letters  同string.ascii_letters(大小写前后可能有别)
string.lowercase  同string.ascii_lowercase
string.uppercase  同string.ascii_uppercase
string.octdigits  输出所有8进制数字字符串
string.hexdigits  输出所有16进制数字字符串
string.digits 输出所有数字的字符串
string.punctuation  输出所有标点符号的字符串
string.whitespace 输出所有空白符号的字符串
"""


def random_string(num_len):
  """ 获取字符长度为num_len，从a-zA-Z0-9生成的随机字符，最大支持生成62位 """
  try:
    num_len = int(num_len)
    strings = ''.join(random.sample(string.ascii_letters + string.digits, num_len))
    return strings
  except BaseException as e:
    Log.MyLog(__name__).error("从a-zA-Z0-9生成{0}位的随机字符失败，{1}".format(num_len, e))
    raise


"""
    python中时间日期格式化符号：
    ------------------------------------
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称  # 乱码
    %% %号本身

    # datetime.timedelta 代表两个时间之间的时间差
    # time.strftime(fmt[,tupletime]) 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定
    # time.strptime(str,fmt='%a %b %d %H:%M:%S %Y') 根据fmt的格式把一个时间字符串解析为时间元组
    # time.mktime(tupletime) 接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）

"""


# def get_time(time_type, layout='%Y-%m-%d %H:%M:%S', unit="0,0,0,0,0"):
#   """
#   获取随机时间
#   time_type: 现在的时间now， 其他时间else
#   layout: 时间类型
#   unit: 时间单位：[seconds, minutes, hours, days, weeks] 秒，分，时，天，周，所有参数都是可选的，并且默认都是0
#   """
#   ti = datetime.datetime.now()
#   if time_type != "now" and layout == '%Y-%m-%d %H:%M:%S':
#     resolution = unit.split(",")
#     try:
#       ti = ti + datetime.timedelta(seconds=int(resolution[0]), minutes=int(resolution[1]),
#                                    hours=int(resolution[2]), days=int(resolution[3]), weeks=int(resolution[4]))
#       ti = ti.strftime(layout)
#       ti = int(time.mktime(time.strptime(ti, "%Y-%m-%d %H:%M:%S")))
#       return ti
#     except BaseException as e:
#       Log.MyLog(__name__).error("获取其他时间错误！{0}".format(e))
#       raise
#   else:
#     try:
#       ti = ti.strftime(layout)
#       ti = int(time.mktime(time.strptime(ti, '%Y-%m-%d %H:%M:%S')))
#       return ti
#     except BaseException as e:
#       Log.MyLog(__name__).error("获取当前时间错误！{0}".format(e))
#       raise

# def get_districtcodes():
#     districtcodes = []
#     with open('./districtcode.txt', mode='r', encoding='utf-8') as f:
#         for l in f.readlines():
#             districtcodes.append(l.strip()[:6])
#     return districtcodes
#
# def generate_ID():
#     """
#     获取随机身份证
#     :return:
#     """
#     try:
#         # 生成前六位地区号码
#         first_list = get_districtcodes()
#         first = random.choice(first_list)
#
#         # 生成年份
#         now = time.strftime('%Y')
#         #1948为第一代身份证执行年份
#         second = random.randint(1948,int(now))
#
#         # 生成月份
#         three = random.randint(1,12)
#         if three < 10:
#             three = '0' + str(three)
#
#         # 生成日期
#         four = random.randint(1,31)
#         if four < 10:
#             four = '0' + str(four)
#
#         # 生成身份证后四位
#         five = random.randint(1,9999)
#         if five < 10:
#             five = '000' + str(five)
#         elif 10 < five < 100:
#             five = '00' + str(five)
#         elif 100 < five < 1000:
#             five = '0' + str(five)
#
#         IDcard = str(first)+str(second)+str(three)+str(four)+str(five)
#         # print('随机生成的身份证号码为：'+IDcard)
#         return IDcard
#     except BaseException as e:
#         Log.MyLog().error('生成随机身份证号失败:{}'.format(e))

class IdNumber(str):

  def __init__(self, id_number):
    super(IdNumber, self).__init__()
    self.id = id_number
    self.area_id = int(self.id[0:6])
    self.birth_year = self.id[6:10]
    self.birth_month = self.id[10:12]
    self.birth_day = self.id[12:14]

  def get_area_name(self):
    """根据区域编号取出区域名称"""
    return const.AREA_INFO[self.area_id]

  def get_birthday(self):
    """通过身份证号获取出生日期"""
    return "{0}-{1}-{2}".format(self.birth_year, self.birth_month, self.birth_day)

  def get_age(self):
    """通过身份证号获取年龄"""
    now = (datetime.now() + timedelta(days=1))
    year, month, day = now.year, now.month, now.day

    if year == self.birth_year:
      return 0
    else:
      if int(self.birth_month) > int(month) or (int(self.birth_month) == int(month) and int(self.birth_day) > int(day)):
        return int(year) - int(self.birth_year) - 1
      else:
        return int(year) - int(self.birth_year)

  def get_sex(self):
    """通过身份证号获取性别， 女生：0，男生：1"""
    sex = int(self.id[16:17]) % 2
    if sex == 0:
      sex = '01002'
    else:
      sex = '01001'
    return sex

  def get_check_digit(self):
    """通过身份证号获取校验码"""
    check_sum = 0
    for i in range(0, 17):
      check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])
    check_digit = (12 - (check_sum % 11)) % 11
    return check_digit if check_digit < 10 else 'X'

  def get_name(self, code):
    first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "好", "一", "乙", "二",
                  "十", "丁", "厂", "七", "卜", "人", "入", "八", "九", "几", "儿", "了", "力", "乃", "刀", "又",
                  "三", "于", "干", "亏", "士", "工", "土", "才", "寸", "下", "大", "丈", "与", "万", "上", "小", "口", "巾", "山",
                  "千", "乞", "川", "亿", "个", "勺", "久", "凡", "及", "夕", "丸", "么", "广", "亡", "门", "义", "之", "尸", "弓",
                  "己", "已", "子", "卫", "也", "女", "飞", "刃", "习", "叉", "马", "乡", "丰", "王", "井", "开", "夫", "天", "无",
                  "元", "专", "云", "扎", "艺", "木", "五", "支", "厅", "不", "太", "犬", "区", "历", "尤", "友", "匹", "车", "巨",
                  "牙", "屯", "比", "互", "切", "瓦", "止", "少", "日", "中", "冈", "贝", "内", "水", "见", "午", "牛", "手", "毛",
                  "气", "升", "长", "仁", "什", "片", "仆", "化", "仇", "币", "仍", "仅", "斤", "爪", "反", "介", "父", "从", "今",
                  "凶", "分", "乏", "公", "仓", "月", "氏", "勿", "欠", "风", "丹", "匀", "乌", "凤", "勾", "文", "六", "方", "火",
                  "为", "斗", "忆", "订", "计", "户", "认", "心", "尺", "引", "丑", "巴", "孔", "队", "办", "以", "允", "予", "劝",
                  "双", "书", "幻", "玉", "刊", "示", "末", "未", "击", "打", "巧", "正", "扑", "扒", "功", "扔", "去", "甘", "世",
                  "古", "节", "本", "术", "可", "丙", "左", "厉", "右", "石", "布", "龙", "平", "灭", "轧", "东", "卡", "北", "占",
                  "业", "旧", "帅", "归", "且", "旦", "目", "叶", "甲", "申", "叮", "电", "号", "田", "由", "史", "只", "央", "兄",
                  "叼", "叫", "另", "叨", "叹", "四", "生", "失", "禾", "丘", "付", "仗", "代", "仙", "们", "仪", "白", "仔", "他",
                  "斥", "瓜", "乎", "丛", "令", "用", "甩", "印", "乐", "句", "匆", "册", "犯", "外", "处", "冬", "鸟", "务", "包",
                  "饥", "主", "市", "立", "闪", "兰", "半", "汁", "汇", "头", "汉", "宁", "穴", "它", "讨", "写", "让", "礼", "训",
                  "必", "议", "讯", "记", "永", "司", "尼", "民", "出", "辽", "奶", "奴", "加", "召", "皮", "边", "发", "孕", "圣",
                  "对", "台", "矛", "纠", "母", "幼", "丝", "式", "刑", "动", "扛", "寺", "吉", "扣", "考", "托", "老", "执", "巩",
                  "圾", "扩", "扫", "地", "扬", "场", "耳", "共", "芒", "亚", "芝", "朽", "朴", "机", "权", "过", "臣", "再", "协",
                  "西", "压", "厌", "在", "有", "百", "存", "而", "页", "匠", "夸", "夺", "灰", "达", "列", "死", "成", "夹", "轨",
                  "邪", "划", "迈", "毕", "至", "此", "贞", "师", "尘", "尖", "劣", "光", "当", "早", "吐", "吓", "虫", "曲", "团",
                  "同", "吊", "吃", "因", "吸", "吗", "屿", "帆", "岁", "回", "岂", "刚", "则", "肉", "网", "年", "朱", "先", "丢",
                  "舌", "竹", "迁", "乔", "伟", "传", "乒", "乓", "休", "伍", "伏", "优", "伐", "延", "件", "任", "伤", "价", "份",
                  "华", "仰", "仿", "伙", "伪", "自", "血", "向", "似", "后", "行", "舟", "全", "会", "杀", "合", "兆", "企", "众",
                  "爷", "伞", "创", "肌", "朵", "杂", "危", "旬", "旨", "负", "各", "名", "多", "争", "色", "壮", "冲", "冰", "庄",
                  "庆", "亦", "刘", "齐", "交", "次", "衣", "产", "决", "充", "妄", "闭", "问", "闯", "羊", "并", "关", "米", "灯",
                  "州", "汗", "污", "江", "池", "汤", "忙", "兴", "宇", "守", "宅", "字", "安", "讲", "军", "许", "论", "农", "讽",
                  "设", "访", "寻", "那", "迅", "尽", "导", "异", "孙", "阵", "阳", "收", "阶", "防", "奸", "如", "妇", "好",
                  "她", "妈", "戏", "羽", "观", "欢", "买", "红", "纤", "级", "约", "纪", "驰", "巡", "寿", "弄", "麦", "形", "进",
                  "戒", "吞", "远", "违", "运", "扶", "抚", "坛", "技", "坏", "扰", "拒", "找", "批", "扯", "址", "走", "抄", "坝",
                  "贡", "攻", "赤", "折", "抓", "扮", "抢", "孝", "均", "抛", "投", "坟", "抗", "坑", "坊", "抖", "护", "壳", "志",
                  "扭", "块", "声", "把", "报", "却", "劫", "芽", "花", "芹", "芬", "苍", "芳", "严", "芦", "劳", "克", "苏", "杆",
                  "杠", "杜", "材", "村", "杏", "极", "李", "杨", "求", "更", "束", "豆", "两", "丽", "医", "辰", "励", "否", "还",
                  "歼", "来", "连", "步", "坚", "旱", "盯", "呈", "时", "吴", "助", "县", "里", "呆", "园"]
    second_name = ["天", "赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "楮", "卫", "蒋", "沈", "韩", "杨",
                   "朱", "秦", "尤", "许", "何", "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏", "陶", "姜",
                   "戚", "谢", "邹", "喻", "柏", "水", "窦", "章", "云", "苏", "潘", "葛", "奚", "范", "彭", "郎",
                   "鲁", "韦", "昌", "马", "苗", "凤", "花", "方", "俞", "任", "袁", "柳", "酆", "鲍", "史", "唐",
                   "费", "廉", "岑", "薛", "雷", "贺", "倪", "汤", "滕", "殷", "罗", "毕", "郝", "邬", "安", "心",
                   "乐", "于", "时", "傅", "皮", "卞", "齐", "康", "伍", "余", "元", "卜", "顾", "孟", "平", "黄",
                   "和", "穆", "萧", "尹", "姚", "邵", "湛", "汪", "祁", "毛", "禹", "狄", "米", "贝", "明", "臧",
                   "计", "伏", "成", "戴", "谈", "宋", "茅", "庞", "熊", "纪", "舒", "屈", "项", "祝", "董", "梁",
                   "杜", "阮", "蓝", "闽", "席", "季", "麻", "强", "贾", "路", "娄", "危", "江", "童", "颜", "郭",
                   "梅", "盛", "林", "刁", "锺", "徐", "丘", "骆", "高", "夏", "蔡", "田", "樊", "胡", "凌", "霍",
                   "虞", "万", "支", "柯", "昝", "管", "卢", "莫", "经", "房", "裘", "缪", "干", "解", "应", "宗",
                   "丁", "宣", "贲", "邓", "郁", "单", "杭", "洪", "包", "诸", "左", "石", "崔", "吉", "钮", "龚",
                   "程", "嵇", "邢", "滑", "裴", "陆", "荣", "翁", "荀", "羊", "於", "惠", "甄", "麹", "家", "封",
                   "芮", "羿", "储", "靳", "汲", "邴", "糜", "松", "井", "段", "富", "巫", "乌", "焦", "巴", "弓",
                   "牧", "隗", "山", "谷", "车", "侯", "宓", "蓬", "全", "郗", "班", "仰", "秋", "仲", "伊", "宫",
                   "宁", "仇", "栾", "暴", "甘", "斜", "厉", "戎", "祖", "武", "符", "刘", "景", "詹", "束", "龙",
                   "叶", "幸", "司", "韶", "郜", "黎", "蓟", "薄", "印", "宿", "白", "怀", "蒲", "邰", "从", "鄂",
                   "索", "咸", "籍", "赖", "卓", "蔺", "屠", "蒙", "池", "乔", "郁", "胥", "能", "苍", "双"]
    name = code + random.choice(first_name) + random.choice(second_name)
    return name

  @classmethod
  def verify_id(cls, id_number):
    """校验身份证是否正确"""
    if re.match(const.ID_NUMBER_18_REGEX, id_number):
      check_digit = cls(id_number).get_check_digit()
      return str(check_digit) == id_number[-1]
    else:
      return bool(re.match(const.ID_NUMBER_15_REGEX, id_number))

  @classmethod
  def generate_id(cls, sex=0):
    """随机生成身份证号，sex = 0表示女性，sex = 1表示男性"""

    # 随机生成一个区域码(6位数)
    id_number = str(random.choice(list(const.AREA_INFO.keys())))
    # 限定出生日期范围(8位数)
    start, end = datetime.strptime("1960-01-01", "%Y-%m-%d"), datetime.strptime("2000-12-30", "%Y-%m-%d")
    birth_days = datetime.strftime(start + timedelta(random.randint(0, (end - start).days + 1)), "%Y%m%d")
    id_number += str(birth_days)
    # 顺序码(2位数)
    id_number += str(random.randint(10, 99))
    # 性别码(1位数)
    id_number += str(random.randrange(sex, 10, step=2))
    # 校验码(1位数)
    return id_number + str(cls(id_number).get_check_digit())

  # 随机手机号
  @staticmethod
  def random_phone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
               "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

  # 随机邮箱号
  @staticmethod
  def random_email(emailType=None, rang=None):
    __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
    # 如果没有指定邮箱类型，默认在 __emailtype中随机一个
    if emailType == None:
      __randomEmail = random.choice(__emailtype)
    else:
      __randomEmail = emailType
    # 如果没有指定邮箱长度，默认在4-10之间随机
    if rang == None:
      __rang = random.randint(4, 10)
    else:
      __rang = int(rang)
    __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
    _email = __randomNumber + __randomEmail
    return _email

# '生成随机身份证号'
def test_idNumber(username):
  id = IdNumber.generate_id()
  idNum = IdNumber(id)
  name = idNum.get_name(username)
  birth = idNum.get_birthday()
  age = idNum.get_age()
  sex = idNum.get_sex()
  return {'idNum': idNum, 'name': name, 'birth': birth, 'age': age, 'sex': sex}


if __name__ == '__main__':
  # info = IdNumber.random_phone()
  # print(info)
  print(getYesterday())
  # info = IdNumber.generate_id()  # 女
  # # info = IdNumber.generate_id(1) # 男
  # print(info)
  # random.choice()
  # pass
  # print(choice_data("400,100,2"))
  # print(random_float("100,200.1,2"))
  # print(random_int("100,200"))
  # print(random_string(6))
  # print(get_time("now"))
  # print(get_time("else",unit="0,0,0,5,0"))
  # generate_ID()
