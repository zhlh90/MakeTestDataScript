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

def make_sql(agency_code, insurance_code, n):

    path = '../../Data_sql/基金收入/国库对账表/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'SMR_TREASURY_RECON_DETAIL'+str(otherStyleTime3)+'.sql'
    smcs_cash_file = open(file_name, 'w', encoding='utf-8')

    # 主表sql
    str_head_zhu = "insert into SMR_TREASURY_RECON_DETAIL values ("

    no = 1
    while (n > 0):

        ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        CREATE_BY = '-1'
        CREATE_DATE = otherStyleTime
        LAST_MODIFIED_BY = '-1'
        LAST_MODIFIED_DATE = otherStyleTime
        LAST_MODIFIED_VERSION = '1'
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
        UUID = ID
        PLAN_ID = ''
        REC_STATUS = ''
        REC_NO = ''
        REC_TIME = ''
        EXCHANGE_PLAN_ID = 'adac5b13390d42699d5a0f498e97a091'
        EXCHANGE_PLAN_STATUS = '1'
        VOU_GUID = ''
        VOU_NO = ''
        VOU_DATE = ''
        VOU_STATUS = ''
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

        line = str_head_zhu + '"' + ID + '", "' + CREATE_BY + '", "'  + CREATE_DATE +  '","' + LAST_MODIFIED_BY + '", "' + LAST_MODIFIED_DATE + '", "' + \
               LAST_MODIFIED_VERSION + '", "' + AAA027 + '", "' + AAA321 + '", "' + AAA322 + '", "' + AAB034 + '", "' + str(AAE056) + '", "' + str(AAE080) + '", "' + str(AAE082) + '", "' + AAE140 + '", "' + str(AAE239) + '", "' + AAE310 + '", "' + AAE311 + '", "' + AAE418 \
               + '", "' + str(AIC152) + '", "' + AAZ400 + '", "' + UUID + '", "' + PLAN_ID + '", "' + REC_STATUS + '", "' + REC_NO + '", "' + REC_TIME + '", "' + EXCHANGE_PLAN_ID + '", "' + EXCHANGE_PLAN_STATUS + '", "' + VOU_GUID + '", "' + VOU_NO + '", "' + \
               VOU_DATE + '", "' + VOU_STATUS + '", "' + FIELD01 + '", "' + FIELD02 + '", "' + FIELD03 + '", "' + FIELD04 + '", "' + FIELD05 + '", "' + FIELD06 + '", "' + FIELD07 + '", "' + FIELD08 + '", "' + FIELD09 + '", "' + FIELD10 + '", "' + FIELD11 + \
               '", "' + FIELD12 + '", "' + FIELD13 + '", "' + FIELD14 + '", "' + FIELD15 + '", "' + FIELD16 + '", "' + FIELD17 + '", "' + FIELD18 + '", "' + FIELD19 + '", "' + FIELD20 + '", "' + AMT01 + '", "' + AMT02 + '", "' + AMT03 + '", "' + AMT04 + '", "' +\
               AMT05 + '", "' + AMT06 + '", "' + AMT07 + '", "' + AMT08 + '", "' + AMT09 + '", "' + AMT10  +'");'

        line = line.replace('\"', '\'')
        no += 1
        n -= 1

        smcs_cash_file.write(line + '\n')


if __name__ == '__main__':
    # 传参： agency_code, insurance_code, n
    make_sql('520201', '310', 10)


