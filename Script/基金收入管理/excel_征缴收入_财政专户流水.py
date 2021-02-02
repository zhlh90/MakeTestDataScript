# -*- coding: utf-8 -*
import datetime

import pandas as pd
import random
import os
import string

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

    headers = ['AAE036', 'AAB001', 'AAA601', 'AAA602', 'AAE140', 'AAA603', 'AAA604', 'AAA605', 'AAZ400', 'UUID', 'VOU_NO', 'AAB034']

    rows = []

    no = 1
    while (n > 0):
        AAE036 = otherStyleTime2
        AAB001 = '1'
        AAA601 = '03'
        AAA602 = '昌平区医保中心上缴财政专户单7'
        AAE140 = insurance_code
        AAA603 = round(random.uniform(100000, 10), 2)
        AAA604 = round(random.uniform(10000, 10), 2)
        AAA605 = round(random.uniform(1000, 10), 2)
        AAZ400 = '6300000020'
        UUID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        VOU_NO = ''
        AAB034 = agency_code

        row =[AAE036, AAB001, AAA601, AAA602, AAE140, AAA603, AAA604, AAA605, AAZ400, UUID, VOU_NO, AAB034]
        rows.append(row)
        no += 1
        n -= 1

    path = '../../Data_excel/基金收入/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + '征缴收入财政专户流水数据接入表'+str(otherStyleTime3)+'.xlsx'
    dt = pd.DataFrame(rows, columns=headers)
    dt.to_excel(file_name, index=0)


if __name__ == '__main__':
    # 传参： agency_code, insurance_code, n
    make_excel('00', '310', 10)


