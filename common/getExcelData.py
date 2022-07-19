# -*- coding:utf-8 -*-
import xlrd

#1、打开excel表
from common import Path
from xlutils.copy import copy

def get_excelData(sheetName,startRow,endRow):
    way = Path.project_path()
    resList=[]
    #1、excel路径
    #excelDir='../datas/product/excel/档案管理接口测试用例.xls'
    excelDir = '{}/datas/product/excel/档案管理接口测试用例.xls'.format(way)
    #2、打开
    workBook=xlrd.open_workbook(excelDir,formatting_info=True)
    # workSheetNames=workBook.sheet_names()#获取所有的sheet页
    # print(workSheetNames)
    #3、根据名称获取指定的sheet页
    workSheet=workBook.sheet_by_name(sheetName)
    #4、读取单元格 cell(行，列)从0开始
    # 列7 请求参数  列8预期响应
    for one in range(startRow-1,endRow):
        reqBodyData=workSheet.cell(one,7).value #某个单元格的值，返回字符串,请求数据
        respData=workSheet.cell(one,8).value #某个单元格的值，返回字符串，响应数据
        #print(reqBodyData,respData)
        resList.append((reqBodyData,respData))
    return resList

def get_excelData2(sheetName,caseName,casePath):
    '''
    :param sheetName: sheet页名称
    :param caseName: 用例名称
    :return:
    '''
    way = Path.project_path()
    resList=[]
    #1、excel路径
    #excelDir = '{}/datas/product/excel/档案管理接口测试用例.xls'.format(way)
    #2、打开
    workBook=xlrd.open_workbook(casePath,formatting_info=True)
    # workSheetNames=workBook.sheet_names()#获取所有的sheet页
    # print(workSheetNames)
    #3、根据名称获取指定的sheet页
    workSheet=workBook.sheet_by_name(sheetName)
    #4、读取单元格 cell(行，列)从0开始
    #print(workSheet.col_values(0))
    idx=0#开始下标
    for one in workSheet.col_values(0):
        if caseName in one:
            reqBodyData=workSheet.cell(idx,7).value #某个单元格的值，返回字符串,请求数据
            respData=workSheet.cell(idx,8).value #某个单元格的值，返回字符串，响应数据
            resList.append((reqBodyData,respData,idx))
        idx+=1
    return resList


#复制新的表，用于将结果写入进去
#sheetIndex 标识获取哪个sheet页的数据
def set_excelData(sheetIndex,casePath):
    workBook=xlrd.open_workbook(casePath,formatting_info=True)
    workBookNew=copy(workBook)#复制到新的表里面
    workSheetNew=workBookNew.get_sheet(sheetIndex)#copy后需用get_sheet获取
    return workBookNew,workSheetNew

if __name__ == '__main__':
    # for one in get_excelData('档案库',2,3):  # one 元祖
    #     print(one[0])
    #print(get_excelData2('档案库','turn_in'))
    for one in get_excelData2('档案库','turn_in'):
        print(one)

