import xlrd, xlwt, pytest, allure
from xlutils.copy import copy
from common import Log, ReadYaml, Assert
from config import conf


@allure.feature('Excel数据校验')
@allure.link(conf.host + '/eHR')
class TestExcelWork:

    log = Log.MyLog(__name__ + '.TestExcelWork')
    # 标准表头
    except_path = r'./datas/data_excel/except_header.yaml'
    header = ReadYaml.read_yaml(except_path)
    # excel文件全路径
    xlPath = r'D:\code\autotest/薪酬模板.xls'


    def setup_class(self):
        self.test_write_excel_xls(self, calculation='结果')
        self.assert_ = Assert.Assertions()

    @pytest.mark.excel
    def test_main(self):
        # 校验列头是否匹配
        header_len = self.test_check_header()
        # 写入“结果”列
        # self.test_write_excel_xls(calculation='结果')
        # # 获取列头编号(列：编号)
        # excelHeader = self.test_readHeader()
        # 获取错误数据
        changeList = self.test_calculation_value()
        # “结果”列写入PASS FAIL
        self.test_write_excel_xls()
        # 错误数据标红
        self.test_color_execl_rc(changeList)

    @allure.story('写入“结果”列及值')
    def test_write_excel_xls(self, calculation=None):
        # index = len(value)  # 获取需要写入数据的行数
        workbook = xlrd.open_workbook(self.xlPath)  # 打开工作簿
        sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
        table = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
        headerValues = table._cell_values[0]
        index = len(headerValues)  # 获取需要写入数据的行数
        # rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
        if '结果' == calculation:
            new_worksheet.write(0, len(self.header), ['结果'])
            print("结果列添加成功。")
        else:
            for i in range(0, index):
                new_worksheet.write(i + 1, len(self.header) + 1, headerValues[i]['结果'])
            # print(self.calculation[i]['结果'])
            print("xls格式表格【追加】写入数据成功！")
        new_workbook.save(self.xlPath)  # 保存工作簿

    @allure.story('错误标红')
    def test_color_execl_rc(self, error_list):
        styleBlueBkg = xlwt.easyxf('pattern: pattern solid, fore_colour red;')  # 红色
        rb = xlrd.open_workbook(self.xlPath)  # 打开t.xls文件
        ro = rb.sheets()[0]  # 读取表单0
        wb = copy(rb)  # 利用xlutils.copy下的copy函数复制
        ws = wb.get_sheet(0)  # 获取表单0
        for i in range(0, len(error_list)):
            map_error = error_list[i]
            row = map_error["行"]
            col = map_error["列"]
            ws.write(row, col, ro.cell(row, col).value, styleBlueBkg)
            # 结果列标红
            ws.write(row, len(self.header)-1, ro.cell(row, len(self.header)-1).value, styleBlueBkg)
            # self.log(u"错误行号为:  ", row)
        wb.save(self.xlPath)

    @allure.story('获取列头编号(列：编号)')
    def test_readHeader(self):
        # 用于读取excel
        xlBook = xlrd.open_workbook(self.xlPath)
        # 获取excel工作簿数
        sheet = xlBook.sheets()
        table = sheet[0]
        ncols = table.ncols
        headerValues = table._cell_values[0]

        headerMap = {}
        for i in range(0, ncols):
            headerMap[headerValues[i]] = i

        # print(headerMap)
        return headerMap

    @allure.story('列头检查')
    def test_check_header(self):
        # 用于读取excel
        xlBook = xlrd.open_workbook(self.xlPath)
        # 获取excel工作簿数
        sheet = xlBook.sheets()
        table = sheet[0]
        headerValues = table._cell_values[0]

        # 标准表头
        header = ReadYaml.read_yaml(self.except_path)

        if len(header) != len(headerValues):
            with allure.step('列头数量不一致！'):
                print('列头数量不一致！')
        # 排序校验表头
        header.sort()
        # 排序读取表头
        headerValues.sort()
        zipped = zip(header, headerValues)
        print('进行匹配列头：{}'.format([*zipped]))
        if headerValues == header:
            with allure.step('结果：列头正确。'):
                print('结果：列头正确。')
        else:
            with allure.step('结果：列头不匹配！'):
                print('结果：列头不匹配！')
            for i, j in zip(header, headerValues):
                if i != j:
                    with allure.step('不匹配列：{0}，{1}'.format(i, j)):
                        self.log.error('不匹配列：{0}，{1}'.format(i, j))
        return headerValues

    @allure.story('获取Excel中数据')
    def test_read_value(self):
        # 用于读取excel
        xlBook = xlrd.open_workbook(self.xlPath)
        # 获取excel工作簿数
        sheet = xlBook.sheets()
        table = sheet[0]
        # print(u"工作簿数为:  {}".format(len(sheet)))
        # 获取 表 数据的行列数
        nrows = table.nrows
        ncols = table.ncols
        # print(u"表数据行列为(%d, %d)" % (nrows, ncols))
        headerValues = table._cell_values[0]
        excel_data = []  # excel中值
        for i in range(0, nrows):
            if i == 0:  # 跳过第一行
                continue
            row = table.row_values(i)  # 按行读取数据
            dict_tmp = {}
            # 输出读取的数据
            for j in range(0, ncols):
                cellValue = row[j]
                dict_tmp[headerValues[j]] = cellValue
            excel_data.append(dict_tmp)

        with allure.step('获取的excel数据：{}'.format(excel_data)):
            return excel_data

    # @allure.story('获取计算结果')
    # def test_calculation_value(self):
    #     excelHeader = self.test_readHeader()
    #     changeList = []
    #     for row in range(0, len(self.calculation)):
    #         data = self.calculation[row] # 每行的数据
    #         with allure.step('第{0}行数据：{1}'.format(row + 1, data)):
    #             print('第{0}行数据：{1}'.format(row + 1, data))
    #         # calculationMap 获取的excel中数据，根据计算公式编写计算公式
    #         with allure.step('开始计算：'):
    #             print('开始计算：')
    #
    #             for col in range(len(data)-1):
    #                 # 公式（期望值）
    #                 formula = data['基本工资'] + data['岗位工资']
    #                 # 期望列
    #                 except_header = self.header[col]
    #                 # 判断列值
    #                 error_header = self.test_to_calculation(data, formula, except_header)
    #                 if error_header:
    #                     changeList.append({"行": (row + 1), "列": (excelHeader[error_header])})
    #
    #     with allure.step('错误数据：{}'.format(changeList)):
    #         print('错误数据：{}'.format(changeList))
    #     return changeList

    @allure.story('获取计算结果2')
    def test_calculation_value(self):
        data = self.test_read_value()
        calculation_header = ReadYaml.read_yaml(r'./datas/data_excel/calculation_header.yaml')
        excelHeader = self.test_readHeader()
        changeList = [] # 报错错误数据
        assert_list = []  # 保存assertError信息
        # for row in range(0, 2):
        data_0 = data[0]  # 第一行原始的数据
        data_1 = data[1]  # 第二行计算后数据
        with allure.step('第{0}行数据：{1}'.format(1 + 1, data_1)):
            print('第{0}行数据：{1}'.format(1 + 1, data_1))
        # calculationMap 获取的excel中数据，根据计算公式编写计算公式
        for key_0, value_0 in data_0.items():
            for key_1, value_1 in data_1.items():
                if key_0 == key_1:
                    if value_0 == value_1:
                        pass
                    else:
                        with allure.step('开始计算：{}'.format(key_1)):
                            # print('开始计算：')
                            # 公式（期望值）
                            formula = eval(calculation_header[key_1])
                            if '综合计算1' == key_1:
                                formula = self.test_value1(data_1)
                            elif '综合计算2' == key_1:
                                formula = self.test_value2(data_1)
                            # 判断列值
                            error_header = self.test_to_calculation(data_1, formula, key_1, assert_list)
                            if error_header:
                                changeList.append({"行": (1 + 1), "列": (excelHeader[error_header])})


        try:# 判断是否有AssertionError，有则抛出，体现在allure报告中
            self.assert_.assert_allure_show(assert_list)
        except Exception as e:
            self.log.error(e)

        # with allure.step('错误数据：{}'.format(changeList)):
        #     print('错误数据：{}'.format(changeList))
        return changeList

    # 其他复杂公式
    def test_value1(self, data):
        # 计算公式
        return 4

    def test_value2(self, data):
        return 2

    @allure.story('计算:')
    def test_to_calculation(self, data, formula,  except_header, assert_list):
        # 实际值
        value = data[except_header]
        if formula == value:
            data["结果"] = "PASS"
            assert_list.append(True)
            result = '{0}：期望={1}, 实际={2} 结果：{3}'.format(except_header, formula, value, "PASS")
            with allure.step(result):
                self.log.info(result)
            return False
        else:
            data["结果"] = "FAIL"
            assert_list.append((except_header, formula, value))
            result = '{0}：期望={1}, 实际={2} 结果：{3}'.format(except_header, formula, value, "FAIL")
            with allure.step(result):
                self.log.error(result)
            return except_header



if __name__ == '__main__':
    # 1. 填写标准请求头
    #    except_path = r'./datas/data_excel/except_header.yaml'
    # 2. 填写excel文件路径
    #    xlPath = r'C:\Users\daichenlei.it\Desktop\薪酬模板.xls'
    # 3. 将计算值复制到（创建完薪酬区间，未计算的导出数据）的excel中第3列
    # 4. 填写需计算的简单头部公式，可‘+’，‘-’，‘*’，‘/’(excel中，需计算的列，即第2列空，第3列有值的字段)
    #    格式： 缺勤扣款: data_1['早退扣款'] + data_1['缺勤扣款']
    #    ReadYaml.read_yaml(r'./datas/data_excel/calculation_header.yaml')
    # 5. 编写其他复杂公式
    # 6. 执行run_excel.py
    pass
