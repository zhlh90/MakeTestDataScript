# -*- coding: utf-8 -*
import datetime

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

    headers = ['TRANSFER_DATE', 'TRANSFER_SOURCE', 'TRANSFER_PERSON', 'AMOUNT', 'INSURANCE_CODE', 'AGENCY_CODE',
               'REGION_CODE']

    rows = []

    no = 1
    while (n > 0):

        TRANSFER_DATE = otherStyleTime1
        TRANSFER_SOURCE = ran_strx("0123456789", 2)
        TRANSFER_PERSON = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 4)
        AMOUNT = round(random.uniform(100000, 10), 2)
        INSURANCE_CODE = insurance_code
        AGENCY_CODE = agency_code
        REGION_CODE = '00'


        row =[TRANSFER_DATE, TRANSFER_SOURCE, TRANSFER_PERSON, AMOUNT, INSURANCE_CODE, AGENCY_CODE,REGION_CODE]
        rows.append(row)
        no += 1
        n -= 1

    path = '../../Data_excel/基金收入/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + '转移收入数据接入表1.xlsx'
    dt = pd.DataFrame(rows, columns=headers)
    dt.to_excel(file_name, index=0)


if __name__ == '__main__':
    # 传参： agency_code, insurance_code, n
    make_excel('00', '110', 100000)


