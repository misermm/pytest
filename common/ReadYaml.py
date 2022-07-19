import yaml


# 读取
def read_yaml(test_data_path):
    with open(test_data_path, encoding='utf-8') as f:
        data = yaml.safe_load(f.read())
    return data


# 写入
def write_yaml(data, test_data_path):
    with open(test_data_path, 'w', encoding='utf-8') as f:
        data = yaml.dump(data, f, sort_keys=False, allow_unicode=True)
    return data


if __name__ == '__main__':
    # data = read_yaml('../datas/data_org/create_org.yaml')
    # print(data)
    # data = {"id": "", "subId": "", "personCode": "", "name": 'self.name', "hiringPlanId": "", "beforeName": "曾用123",
    #                 "idType": "3133100225", "idNum": 'self.id', "birth": 'self.birth', "isAgainJob": "0",
    #                 "age": 'self.age', "sex": 'self.sex', "nationality": "CHN", "partyFigure": "0120000002", "nation": "011502",
    #                 "maritalStatus": "0130000001", "height": "180.00", "bloodType": "3012000335", "weight": "79.00",
    #                 "orgType": "3732000004", "orgId": "ceb345077a8011eb85d9ac1f6b14614a",
    #                 "deptId": "14216c7d89324c66bc6aa68e9ba884cd", "department": "", "threeOrg": "",
    #                 "postId": "", "postRank": "3173000008", "postTime": "2017-04-05",
    #                 "personType": "0135000001", "perState": "0145000001", "perType": "3235000002",
    #                 "inOrgTime": "2015-04-14", "probationPeriod": "3247000002", "lastPreRegularTime": "2021-05-06",
    #                 "positionCategory": "3724000019", "positionLevelCategory": "3725000003", "workTime": "2016-04-05",
    #                 "workAdjustmentTime": "1.00", "bankWorkTime": "2014-04-22", "bankWorkAdjustmentTime": "2.00",
    #                 "workYears": "4.01", "bankWorkYears": "4.96", "serviceBankTime": "5.98", "education": "11",
    #                 "firstEducation": "21", "residentPlace": "110101000000", "residentType": "3017000001",
    #                 "idCardPlace": "户口所在地123", "nowHomePlace": "现所在地住址123", "homeAddress": "家庭地址123",
    #                 "phoneNum": "13121122211", "entryType": "3202000002", "talentLabel": "人才标签123", "isExecutives": "00901",
    #                 "checkType": "3730000003", "siPayArea": "1064000016", "fundArea": "1064000015", "health": "3016000001",
    #                 "physicalResult": "3731000002", "threePartiesAgreement": "1", "isGreyList": "1",
    #                 "greyResultList": "3731000002", "isBackSurvey": "1"}
    # data = {"b001005": "测试县1", "b001002": "7A5148891F4D4F0DBD0DC3137AE4AC6E", "id": "",
    #         "b001211": "3049000003", "B001228": "3723000001", "b001229": "110000000000", "b001240": "101011",
    #         "b001255": "0002f3d07d9e11eb85d9ac1f6b14614a", "b001215": "3105400306", "b001201": "1000",
    #         "b001231": "2018-04-10", "b001406": "1111111111", "b001402": "2222222222aaaa",
    #         "b001403": "2019-01-01", "b001202": "3333333333333333aa", "b001404": "2020-03-02",
    #         "b001234": "44444444444444a", "b001405": "2021-03-09", "b001206": "55555555", "b001407": "0",
    #         "b001249": "13121122211", "uploadFile": "", "b001209": "", "b001225": "办公地址123"}
    # data = {"postName": "测试岗位1", "postRank": "3173000004", "postCount": "3129100213", "postProperty": "3022000004",
    #                 "postNaturalPerson": "1", "qualificationNo": "1", "ispostkey": "00901", "keyyears": 1,
    #                 "orgType": "3049000013,3049000012,3049000011,3049000010,3049000009,3049000008,3049000007,3049000006,3049000004,3049000003,3049000002,3049000001",
    #                 "remark": "备注1232"}
    # data = ['*雇员姓名', '*证件号码', '*计税类型', '应发金额', '基本工资', '岗位工资', '应出勤天数', '事假扣款', '病假扣款', '迟到扣款', '早退扣款',
    #  '旷工扣款', '缺勤扣款', '加班费', '税前其他计税部分', '税前其他免税部分', '税前捐赠免税部分', '税前商保计税部分', '商业健康险', '税延养老保险',
    #  '企业年金免税部分', '养老保险(个人)', '医疗保险(个人)', '失业保险(个人)', '住房公积金(个人)', '养老保险(公司)', '医疗保险(公司)', '失业保险(公司)',
    #  '工伤保险(公司)', '生育保险(公司)', '住房公积金(公司)', '养老扣款月次', '医疗扣款月次', '失业扣款月次', '公积金扣款月次', '累计子女教育扣除额',
    #  '累计继续教育扣除额', '累计大病医疗扣除额', '累计住房贷款利息扣除额', '累计住房租金扣除额', '累计赡养老人扣除额', '税后扣款', '企业年金税后扣除',
    #  '税后其他免税补贴', '税后独生子女补贴']
    # data = {"orgId": "2b0c31231c6972681dbcc31f4a9879ab", "batch": "00900", "postName": "自动-岗位-复制1", "superId": "",
    #         "jobclan": "60110003", "jobcategory": "60110004", "postLine": "3015000001", "workOut": "1",
    #         "ispostkey": "00900", "bankclassify": "60150001", "keyyears": "1", "yearholiday": "2",
    #         "mapZG": {"c017000": "00901", "c017200": 'null', "lastOperator": 'null',
    #                   "subid": "815bd6842a644f1990694743e7104ff5", "professionalname": "自动-专业资格-1",
    #                   "createTime": 'null', "c017204Txt": "自动-专业资格-1", "c017206": "工作经验要求123", "c017205": "知识技能123",
    #                   "c017208": "其它要求123", "id": "96830297ef55c81cf370837d97b402ef", "c017207": "能力素质要求123",
    #                   "c017202": 'null', "c017201": 'null', "c017204": "5001f1bcc9a4be7bdcdb2ccb958cbfb7",
    #                   "lastUpdateTime": 'null', "c017203": "036510"},
    #         "mapZB": {"lastOperator": 'null', "createTime": 'null', "c400207": 7, "c400206": 6, "c400205": 5,
    #                   "c400204": 4, "id": 96830297, "c400203": 3, "c400202": 2, "c400201": 1, "lastUpdateTime": 'null'},
    #         "mapZZ": [{"subid": "82c7e053abb943039b9536a4025ba419", "c008005": "职责3", "lastOperator": 'null',
    #                    "createTime": 'null', "id": 13, "c008000": "00900", "c008200": 2, "c008201": "3134100256",
    #                    "lastUpdateTime": 'null', "isEdit": 'false', "_XID": "row_84"},
    #                   {"subid": "dc60eb6e35cf487590361d9e740b080f", "c008005": "职责1", "lastOperator": 'null',
    #                    "createTime": 'null', "id": 13, "c008000": "00900", "c008200": 1, "c008201": "3134100228",
    #                    "lastUpdateTime": 'null', "isEdit": 'false', "_XID": "row_85"},
    #                   {"subid": "f4e3592fea83480f880dbdd609b0e5c4", "c008005": "职责2", "lastOperator": 'null',
    #                    "createTime": 'null', "id": 13, "c008000": "00901", "c008200": 2, "c008201": "3134100229",
    #                    "lastUpdateTime": 'null', "isEdit": 'false', "_XID": "row_86"}]}
    # data = {"orgId": "6a5e589bf0857b065ab4751c10b45205", "batch": "00900", "postName": "自动化-岗位1", "superId": "",
    #         "jobclan": "60110004", "jobcategory": "60110003", "postLine": "3015000002", "workOut": "1",
    #         "ispostkey": "00901", "bankclassify": "60150005", "keyyears": "1", "yearholiday": "2",
    #         "mapZG": {"c017203": "036510", "c017204": "5001f1bcc9a4be7bdcdb2ccb958cbfb7", "c017205": "知识技能123",
    #                   "c017206": "工作经验要求123", "c017207": "能力素质要求123", "c017208": "其它要求123"},
    #         "mapZB": {"c400201": 1, "c400202": 2, "c400203": 3, "c400204": 4, "c400205": 5, "c400206": 6, "c400207": 7},
    #         "mapZZ": [
    #             {"id": 5, "c008005": "职责1", "c008200": 1, "c008201": "3134100228", "isEdit": 'true', "_XID": "row_136"},
    #             {"id": 49, "c008005": "职责2", "c008200": 2, "c008201": "3134100229", "isEdit": 'true', "_XID": "row_137"},
    #             {"id": 46, "c008005": "职责3", "c008200": 3, "c008201": "3134100256", "isEdit": 'true', "_XID": "row_138"}]}
    data = {"height": 188, "weight": 80, "leisureMonth": 2, "internshipStartTime": "2018-05-07",
            "internshipEndTime": "2018-05-18", "probationStartTime": "", "probationEndTime": "",
            "idNum": "520326197801316907", "idType": "3133100225", "birth": "1978-01-31", "sex": "01002", "age": 43,
            "name": "测试代1", "nationality": "3048000544", "nation": "011501", "email": "123@123.kdm",
            "phoneNumber": "13122213113", "partyFigure": "0120000002", "partyTime": "2015-05-01",
            "religion": "60080002", "healthy": "3016000322", "specialty": "个人特长123", "hobby": "爱好123",
            "entryType": "3202000001", "isTrial": "00900", "isProbation": "00900", "isOutStaff": "00900",
            "trialStartTime": "", "trialEndTime": "", "organization": "60070001", "probationEduAm": 0, "empLevel": "3",
            "nativePlace": "0105110102", "nativePlaceRemark": "籍贯说明123", "residentPlace": "0105110101",
            "residentType": "3017000337", "nowHomePlace": "现居住地址123", "idCardPlace": "家庭住址123",
            "siPayArea": "1064000001", "siPayAreaForOld": "1064000002", "fundArea": "1064000003",
            "marryStatus": "01301", "workTime": "2016-05-10", "jobTime": "2017-05-08", "inOrgTime": "2018-05-01",
            "bankId": "621226100108077", "orgAreId": "a1f60884b34ed853588687c141eab501",
            "orgId": "a1f60884b34ed853588687c141eab501", "orgIdName": "总行",
            "deptId": "6a5e589bf0857b065ab4751c10b45205", "deptIdName": "总行自动-撤销有人58", "department": "",
            "departmentName": "", "postId": "e53d1d289750bf8f48951ed8feec6b6e",
            "adminPosition": "1e122f590bc74389868fd0950fa50a3f", "adminPositionLevel": "01750008",
            "wagePosition": "1e122f590bc74389868fd0950fa50a3f", "wagePositionLevel": "01750008",
            "proTecPosition": "273844387fc79822f45b74a5b0ce4c32", "proTecPositionLevel": "01750001",
            "preEmpFlag": "00901"}
    # 先创建文件夹
    # write_yaml(data, '../datas/dongguan/person/create_person.yaml')
    a = read_yaml('../datas/dongguan/person/add_educate_work.yaml')
    print(a)
