# -*- coding: utf-8 -*
import datetime
import time

import pandas as pd
import random
import string
from Script import shenfenzhenghao
from enum import Enum
import os

# 银行类型
cl_banktype = ['00', '01']
cl_bussniss_type = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13','15','16']
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

def make_sql(country_code, rg_name, n):

    path = '../Data_sql/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'smcs_cash_pos_business'+str(otherStyleTime3)+'.sql'
    smcs_cash_file = open(file_name, 'w', encoding='utf-8')

    # 主表sql
    str_head_pos = "insert into smcs_cash_pos_business values ("

    no = 1
    while (n > 0):

        ID = ''.join(random.sample(string.ascii_lowercase + string.digits, 30))
        CREATE_BY = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
        CREATE_DATE = otherStyleTime
        LAST_MODIFIED_BY = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        LAST_MODIFIED_DATE = otherStyleTime
        LAST_MODIFIED_VERSION = '1'
        MESSAGE_TYPE = random.choice(['7', '8'])
        # APPLY_NO = ''.join(random.sample(string.ascii_lowercase + string.digits, 20))
        SERIAL_NO = ''.join(random.sample(string.ascii_lowercase + string.digits, 16))
        APPLY_SUB_NO = '01'
        # BILL_NO = ''.join(random.sample(string.ascii_lowercase + string.digits, 16))
        SETTLE_TYPE = '1'
        PAY_AMOUNT = 6
        PAY_DATE = otherStyleTime
        PAY_YEAR = '2020'
        APPLY_USER_NAME = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 4)
        APPLY_USER_CARD_ID = shenfenzhenghao.outIDcard()
        MEDICARE_ORDER_NO = ran_strx("0123456789", 10)
        OPT_COUNTY = country_code
        CENSUS_COUNTY = country_code
        INSURANCE_TYPE = '2'
        PAY_TYPE = '1'
        RES1 = ''
        RES2 = ''
        RES3 = ''
        RES4 = ''
        CENTER_CODE = country_code
        CENTER_NAME = rg_name
        APPLY_NO = country_code + str(n)
        BILL_NO = APPLY_NO + APPLY_SUB_NO
        EXCHANGE_PLAN_STATUS = ''
        EXCHANGE_PLAN_ID = ''



        line = str_head_pos + '"' + ID + '", "' + MESSAGE_TYPE + '", "' + SERIAL_NO + '", "' + APPLY_NO + '", "' + \
               APPLY_SUB_NO + '", "' + BILL_NO + '", "' + APPLY_USER_NAME + '", "' + APPLY_USER_CARD_ID + '", "' + \
               SETTLE_TYPE + '", "' + str(PAY_AMOUNT) + '", ' + 'TO_TIMESTAMP(\'' + PAY_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'),' + ' "' + PAY_YEAR + '", "' + \
               MEDICARE_ORDER_NO + '", "' + OPT_COUNTY + '", "' + CENSUS_COUNTY + '", "' + INSURANCE_TYPE +  '", "' \
               + PAY_TYPE + '", "' + CREATE_BY + '", ' + 'TO_TIMESTAMP(\'' + CREATE_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'),' + ' "' + LAST_MODIFIED_BY + '", ' + 'TO_TIMESTAMP(\'' + \
               LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'),' + ' "' + LAST_MODIFIED_VERSION + '", "' + RES1 + '", "' + RES2 + '", "' + \
               RES3 + '", "' + RES4 + '", "' + CENTER_CODE + '", "' + CENTER_NAME + '", "' + EXCHANGE_PLAN_STATUS + '", "' + EXCHANGE_PLAN_ID + '");'

        line = line.replace('\"', '\'')
        no += 1
        n -= 1

        smcs_cash_file.write(line + '\n')


if __name__ == '__main__':
    # 传参： country_code, rg_name, n
    make_sql('01', '上海市黄浦区', 1)


