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

    headers = ['AAA027', 'AAA321', 'AAA322', 'AAB034', 'AAE056', 'AAE080', 'AAE082', 'AAE140', 'AAE239', 'AAE310', 'AAE311', 'AAE418', 'AIC152', 'AAZ400', 'UUID', 'VOU_NO']

    rows = []

    no = 1
    while (n > 0):
        AAA027 = '00'
        AAA321 = '1'
        AAA322 = otherStyleTime3 + ran_strx("0123456789", 10)
        AAB034 = agency_code
        AAE056 = round(random.uniform(1000, 10), 2)
        AAE080 = round(random.uniform(100000, 10), 2)
        AAE082 = round(random.uniform(10000, 10), 2)
        AAE140 = insurance_code
        AAE239 = '1'
        AAE310 = otherStyleTime2
        AAE311 = otherStyleTime2
        AAE418 = '202006021220'
        AIC152 = round(random.uniform(100000, 10), 2)
        AAZ400 = '8836'
        UUID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        VOU_NO = ''

        row =[AAA027, AAA321, AAA322, AAB034, AAE056, AAE080, AAE082, AAE140, AAE239, AAE310, AAE311, AAE418, AIC152, AAZ400, UUID, VOU_NO]
        rows.append(row)
        no += 1
        n -= 1

    path = '../../Data_excel/基金收入/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + '征缴收入国库对账表数据接入表'+str(otherStyleTime3)+'.xlsx'
    dt = pd.DataFrame(rows, columns=headers)
    dt.to_excel(file_name, index=0)


if __name__ == '__main__':
    # 传参： agency_code, insurance_code, n
    make_excel('00', '310', 10)


