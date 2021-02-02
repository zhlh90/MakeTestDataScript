# -*- coding: utf-8 -*
import datetime

import pandas as pd
import random
import os

#业务类型
bussnisstype = ['K1002401', 'K1002402', 'K1002403', 'K1002404',
                'K10025', 'K10026', 'K90004', 'K90005', 'K90006',
                'K90007', 'K90008', 'K90009', 'K90010', 'K90011',
                'K90012', 'K90013', 'K90014', 'K90015', 'K90016', 'K90017', 'K90018']
bussnisstype_in = ['K90004', 'K90008', 'K90009', 'K90010', 'K90011', 'K90012', 'K90013', 'K90014', 'K90015']

# 从字符串中随机取n个字符组成字符串
def ran_strx(strx, n):
    items = list(strx)
    str2 = ''
    for i in range(0, n):
        random.randint(0, len(items)-1)
        str1 = items[random.randint(0, len(items)-1)]
        str2 += str(str1)
    return str2

#获得当前时间
now = datetime.datetime.now()
#转换为指定的格式:
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
otherStyleTime1 = now.strftime("%Y%m%d%H")
otherStyleTime2 = now.strftime("%Y-%m-%d")
otherStyleTime3 = now.strftime("%Y%m%d%H%M%S")

def make_excel(agency_code, insurance_code, n):

    headers = ['BUSINESS_DATE', 'SUBSIDIZED_AREA', 'GRANT_UNIT', 'SUMMARY', 'SUBSIDY_AMOUNT', 'BUSINESS_TYPE',
               'INSURANCE_CODE', 'AGENCY_CODE', 'REGION_CODE']

    rows = []

    no = 1
    while (n > 0):
        BUSINESS_DATE = otherStyleTime2
        SUBSIDIZED_AREA = '测试区域' + ran_strx("0123456789", 8)
        GRANT_UNIT = '测试单位' + ran_strx("0123456789", 8)
        SUMMARY = '摘要' + otherStyleTime
        SUBSIDY_AMOUNT = round(random.uniform(100000, 10), 2)
        BUSINESS_TYPE = random.choice(bussnisstype_in)
        INSURANCE_CODE = insurance_code
        AGENCY_CODE = agency_code
        REGION_CODE = '310000'


        row =[BUSINESS_DATE, SUBSIDIZED_AREA, GRANT_UNIT, SUMMARY, SUBSIDY_AMOUNT, BUSINESS_TYPE, INSURANCE_CODE, AGENCY_CODE,REGION_CODE]
        rows.append(row)
        no += 1
        n -= 1

    path = '../../Data_excel/基金收入/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + '财政补贴收入数据接入表'+str(otherStyleTime3)+'.xlsx'
    dt = pd.DataFrame(rows, columns=headers)
    dt.to_excel(file_name, index=0)


if __name__ == '__main__':
    # 传参： agency_code, insurance_code, n
    make_excel('00', '310', 10)


