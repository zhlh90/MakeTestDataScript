# -*- coding:utf-8 -*-
import datetime
import os
import random


#获得当前时间
import time

now = datetime.datetime.now()
#转换为指定的格式:
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
otherStyleTime1 = now.strftime("%Y%m%d%H")
otherStyleTime2 = now.strftime("%Y-%m-%d")
otherStyleTime3 = now.strftime("%Y%m%d%H%M%S")
otherStyleTime4 = now.strftime("%Y%m%d%H%M")

# 生成txt文件。传参：生成文件名称，DealNo，MsgId
def makeTxtFile(country_code, n):
    # 增加换行符
    path = '../../Data_txt/转移支出/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    filepath = path + '转移支出' + otherStyleTime3 +'.txt'
    # tree.write(filepath, encoding='utf-8', xml_declaration=True)
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding='UTF-8') as f:
            print(f)

    with open(filepath, "a", encoding='UTF-8') as f:
        no = 1
        while (n > 0):
            ID = 'ZYZC' + otherStyleTime4 + str(n) + '|'
            jine1 = round(random.uniform(100000, 10), 2)
            jine2 = round(random.uniform(10000, 10), 2)

            str_data = ID + '00|上海市统筹|310|城镇职工基本医疗保险|张三|230128199909143832|00|上海市医保中心|' + str(jine1)+'|' + \
                       str(jine2)+'|' + '保定人民医院11|保定医保中心11|99999994|保定社保|102|中国工商银行|测试|' + otherStyleTime2 +'\n'

            f.write(str_data)

            no += 1
            n -= 1


if __name__ == '__main__':
    # 生成xml文件。传参：生成文件名称，单位编号，日期
    country_code = '00'
    makeTxtFile(country_code, 2)
