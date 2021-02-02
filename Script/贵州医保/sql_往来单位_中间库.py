# -*- coding: utf-8 -*
import datetime

# import pandas as pd
import random
import os

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
otherStyleTime4 = now.strftime("%Y%m%d%H%M")

def make_sql(country_code, n):

    path = '../../Data_sql/往来单位/往来单位同步SQL/';
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'MID_ORG_UNIT'+str(otherStyleTime3)+'.sql'
    MID_ORG_UNIT_file = open(file_name, 'w', encoding='utf-8')

    # 往来单位表sql
    str_head_zhu = "insert into MID_ORG_UNIT values ("

    no = 1
    while (n > 0):
        # 往来单位表
        CO_CODE = ran_strx("0123456789", 3)
        CO_SI_CODE = ran_strx("0123456789", 40)
        CO_NAME = '往来单位' + otherStyleTime4 +str(n)
        CO_SHORT = '往' + otherStyleTime4 +str(n)
        COUNTY_CODE = country_code
        COUNTY_NAME = '默认区划'
        CO_TYPE_CODE = '2'
        # CO_TYPE_CODE = '10'
        CO_TYPE_NAME = '药房'
        # CO_TYPE_NAME = '国有企业'
        LINKMAN = ''
        TELEPHONE = ran_strx("0123456789", 8)
        ADDRESS = '北京市海淀区西北旺用友路' + str(n) + '号'
        ACCOUNT_NO = ran_strx("0123456789", 16)
        ACCOUNT_NAME = CO_NAME
        BANK_CODE = '313'
        BANK_NAME = '上海银行'
        COMBINE_ACC_NUM = ran_strx("0123456789", 12)
        ENABLED = '1'
        HOSPITAL_TYPE_CODE = ''
        HOSPITAL_TYPE_NAME = ''
        IS_PAY = '0'
        INSURANCE_CODE = ''
        INSURANCE_NAME = ''
        SET_YEAR = '2020'
        FIELD1 = ''
        FIELD2 = ''
        FIELD3 = ''
        AGENCY_CODE = '520201'
        STATE = '0'

        line = str_head_zhu + '"' + CO_CODE + '", "' + CO_SI_CODE + '", "' + CO_NAME + '", "' + CO_SHORT + '", "' + \
               COUNTY_CODE + '", "' + COUNTY_NAME + '", "' + CO_TYPE_CODE + '", "' + CO_TYPE_NAME + '", "' + LINKMAN + '", "' + \
               TELEPHONE + '", "' + ADDRESS + '", "' + ACCOUNT_NO + '", "' + ACCOUNT_NAME + '", "' + BANK_CODE + '", "' + \
               BANK_NAME + '", "' + COMBINE_ACC_NUM + '", "' + ENABLED + '", "' + HOSPITAL_TYPE_CODE + '", "' + \
               HOSPITAL_TYPE_NAME + '", "' + IS_PAY + '", "' + INSURANCE_CODE + '", "' + INSURANCE_NAME + '", "' + \
               SET_YEAR + '", "' + FIELD1 + '", "' + FIELD2 + '", "' + FIELD3 + '", "' + AGENCY_CODE + '", "' + STATE + '");'

        line = line.replace('\"', '\'')

        no += 1
        n -= 1

        MID_ORG_UNIT_file.write(line + '\n')


if __name__ == '__main__':
    # 传参： country_code, n
    make_sql('520201', 10)


