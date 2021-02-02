# -*- coding: utf-8 -*
import datetime
import string

import pandas as pd
import random
import os

# 银行类型
cl_banktype = ['00', '01']
cl_bussniss_type = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
cl_pay_target = ['00', '01', '02', '03', '04', '05', '06']
cl_hospital_lv = ['00', '01', '02', '03', '04', '05', '06']
cl_medical_type = ['00', '01', '02', '03', '04', '05']

# 从字符串中随机取n个字符组成字符串
def ran_strx(strx, n):
    items = list(strx)
    str2= ''
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

    headers = ['AAA027','AAA041','AAA042','AAA115','AAA321','AAA322','AAB001','AAB034','AAB084','AAB119','AAB120',
               'AAB121','AAB165','AAD009','AAE003','AAE056','AAE080','AAE082','AAE140','AAE239','AAE418','AAE530',
               'AAE531','AAF020','AAZ288','AAZ400','UUID']

    rows = []

    no = 1
    while (n > 0):

        AAA027 = '00'
        AAA041 = round(random.uniform(1000, 10), 2)
        AAA042 = round(random.uniform(1000, 10), 2)
        AAA115 = '10'
        AAA321 = ran_strx("12345690",1)
        AAA322 = otherStyleTime3 + ran_strx("0123456789", 10)
        AAB001 = 'DWBH' + ran_strx("1234567890", 8)
        AAB034 = agency_code
        AAB084 = round(random.uniform(100000, 10), 2)
        AAB119 = ran_strx("123456789", 4)
        AAB120 = round(random.uniform(100000, 10), 2)
        AAB121 = round(random.uniform(100000, 10), 2)
        AAB165 = '10'
        AAD009 = ran_strx("1234567890", 8)
        AAE003 = '202008'
        AAE056 = round(random.uniform(1000, 10), 2)
        AAE080 = round(random.uniform(100000, 10), 2)
        AAE082 = round(random.uniform(10000, 10), 2)
        AAE140 = insurance_code
        AAE239 = '1'
        AAE418 = '202008041220'
        AAE530 = otherStyleTime2
        AAE531 = otherStyleTime
        AAF020 = otherStyleTime
        AAZ288 = ran_strx("1234567890", 8)
        AAZ400 = '8836'
        UUID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))


        row =[AAA027, AAA041, AAA042, AAA115, AAA321, AAA322, AAB001, AAB034, AAB084, AAB119, AAB120, AAB121, AAB165, AAD009, AAE003, AAE056, AAE080, AAE082, AAE140, AAE239, AAE418, AAE530, AAE531, AAF020, AAZ288, AAZ400, UUID]
        rows.append(row)
        no += 1
        n -= 1

    path = '../../Data_excel/基金收入/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + '单位缴费收入台账'+str(otherStyleTime3)+'.xlsx'
    dt = pd.DataFrame(rows, columns=headers)
    dt.to_excel(file_name, index=0)


if __name__ == '__main__':
    # 传参： agency_code, insurance_code, n
    make_excel('00', '310', 1)


