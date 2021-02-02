# -*- coding: utf-8 -*
import datetime

# import pandas as pd
import random
import string
import os

# 银行类型
cl_banktype = ['00', '01']
# cl_bussniss_type = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13','15','16']
cl_bussniss_type = ['01', '02', '03', '04', '10', '12', '13','15','16']
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

def make_sql(country_code, n):

    path = '../../Data_sql/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'SMR_FISCAL_REVENUE_RECON'+str(otherStyleTime3)+'.sql'
    smcs_cash_file = open(file_name, 'w', encoding='utf-8')

    # 主表sql
    str_head_zhu = "insert into SMR_FISCAL_REVENUE_RECON values ("

    no = 1
    while (n > 0):

        ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        CREATE_BY = '-1'
        CREATE_DATE = otherStyleTime
        LAST_MODIFIED_BY = '-1'
        LAST_MODIFIED_DATE = otherStyleTime
        LAST_MODIFIED_VERSION = '1'
        AAE036 = otherStyleTime2
        AAB001 = round(random.uniform(1000000, 10), 2)
        AAA601 = '03'
        AAA602 = '昌平区医保中心上缴财政专户单7'
        AAE140 = '001'
        AAA603 = round(random.uniform(100000, 10), 2)
        AAA604 = round(random.uniform(10000, 10), 2)
        AAA605 = round(random.uniform(1000, 10), 2)
        AAZ400 = '6300000020'
        UUID = ID
        PLAN_ID = ''
        REC_STATUS = ''
        REC_NO = ''
        REC_TIME = ''
        EXCHANGE_PLAN_ID = 'b1a8c8c3e2084e36b7a94ddedf681c3a'
        EXCHANGE_PLAN_STATUS = '1'
        VOU_GUID = ''
        VOU_NO = ''
        VOU_DATE = ''
        VOU_STATUS = '0'
        FIELD01 = ''
        FIELD02 = ''
        FIELD03 = ''
        FIELD04 = ''
        FIELD05 = ''
        FIELD06 = ''
        FIELD07 = ''
        FIELD08 = ''
        FIELD09 = ''
        FIELD10 = ''
        FIELD11 = ''
        FIELD12 = ''
        FIELD13 = ''
        FIELD14 = ''
        FIELD15 = ''
        FIELD16 = ''
        FIELD17 = ''
        FIELD18 = ''
        FIELD19 = ''
        FIELD20 = ''
        AMT01 = ''
        AMT02 = ''
        AMT03 = ''
        AMT04 = ''
        AMT05 = ''
        AMT06 = ''
        AMT07 = ''
        AMT08 = ''
        AMT09 = ''
        AMT10 = ''
        AAB034 = country_code

        line = str_head_zhu + '"' + ID + '", "' + CREATE_BY + '", ' + 'TO_TIMESTAMP(\'' + CREATE_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + LAST_MODIFIED_BY + '", TO_TIMESTAMP(\'' + LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), "' + \
               LAST_MODIFIED_VERSION + '", "' + AAE036 + '", "' + str(AAB001) + '", "' + AAA601 + '", "' + AAA602 + '", "' + AAE140 + '", "' + str(AAA603) + '", "' + str(AAA604) + '", "' + str(AAA605) + '", "' + AAZ400 + '", "' + UUID + '", "' + PLAN_ID + '", "' + REC_STATUS + \
               '", "' + REC_NO + '", "' + REC_TIME + '", "' + EXCHANGE_PLAN_ID + '", "' + EXCHANGE_PLAN_STATUS + '", "' + VOU_GUID + '", "' + VOU_NO + '", "' + VOU_DATE + '", "' + VOU_STATUS + '", "' + FIELD01 + '", "' + FIELD02 + '", "' + FIELD03 + '", "' +\
               FIELD04 + '", "' + FIELD05 + '", "' + FIELD06 + '", "' + FIELD07 + '", "' + FIELD08 + '", "' + FIELD09 + '", "' + FIELD10 + '", "' + FIELD11 + '", "' + FIELD12 + '", "' + FIELD13 + '", "' + FIELD14 + '", "' + FIELD15 + '", "' + FIELD16 + '", "' \
               + FIELD17 + '", "' + FIELD18 + '", "' + FIELD19 + '", "' + FIELD20 + '", "' + AMT01 + '", "' + AMT02 + '", "' + AMT03 + '", "' + AMT04 + '", "' + AMT05 + '", "' + AMT06 + '", "' + AMT07 + '", "' + AMT08 + '", "' + AMT09 + '", "' + AMT10 + '", "' + AAB034 + '");'

        line = line.replace('\"', '\'')
        no += 1
        n -= 1

        smcs_cash_file.write(line + '\n')


if __name__ == '__main__':
    # 传参： country_code, n
    make_sql('00', 134)


