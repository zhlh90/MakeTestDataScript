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
otherStyleTime4 = now.strftime("%Y%m%d%H%M")
otherStyleTime5 = now.strftime("%Y-%m")

def make_sql(agency_code, n):

    path = '../../Data_sql/统收统支/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'SURP_COUNTY_FORM_APPLY_TEST'+str(otherStyleTime3)+'.sql'
    smcs_cash_file = open(file_name, 'w', encoding='utf-8')

    # 主表sql
    str_head_zhu = "insert into SURP_COUNTY_FORM_APPLY_TEST values ("

    no = 1
    while (n > 0):

        ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        YEAR_MONTH = otherStyleTime5
        YEAR = '2020'
        MONTH = '08'
        QUARTER = '3'
        INSURANCE_CODE = '110'
        INSURANCE_NAME = '城镇企业职工基本养老保险'
        AGENCY_CODE = agency_code
        AGENCY_NAME = '长安区保险事业管理局'
        APPLY_PAY_MONEY = str(round(random.uniform(10000, 10), 2))
        REC_ACCOUNT_NO = '130100123456789001-001'
        REC_ACCOUNT_NAME = '石家庄市本级保险事业管理局支出户001-001'
        REC_BANK_NODE_NAME = '上海银行石家庄市支行1号'
        REC_BANK_NODE_SEQ = '130100123456'
        REC_BANK_TYPE_CODE = '313'
        REC_BANK_TYPE_NAME = '上海银行'
        REGION_CODE = '130000'
        REGION_NAME = '河北省'
        APPLY_FORM_NO = 'YK' + otherStyleTime4 + str(n)
        IF_COLLECTED = '0'
        OPERATE_STATE = '0'
        OPERATE_TIME = otherStyleTime
        OPERATOR_ID = 'smifc1'
        CREATE_USER_NAME = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
        PARENT_COLLECTED_FORM_NO = ''
        CHECK_STATUS = ''
        CHECK_AMOUNT = ''
        CHECK_DATE = ''
        CHECK_INFO = ''
        CHECK_PERSON = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        BUSINESS_DATE = otherStyleTime2
        PURPOSE = '测试-数据接入'
        APPLY_TIME = otherStyleTime
        STATUS = '0'

        line = str_head_zhu + '"' + ID + '", "' + YEAR_MONTH + '", "' + YEAR + '", "' + MONTH + '", "' + QUARTER + '", "' + \
               INSURANCE_CODE + '", "' + INSURANCE_NAME + '", "' + AGENCY_CODE + '", "' + AGENCY_NAME + '", "' + APPLY_PAY_MONEY + '", "' + \
               REC_ACCOUNT_NO + '", "' + REC_ACCOUNT_NAME + '", "' + REC_BANK_NODE_NAME + '", "' + REC_BANK_NODE_SEQ + '", "' + \
               REC_BANK_TYPE_CODE + '", "' + REC_BANK_TYPE_NAME + '", "' + REGION_CODE + '", "' + REGION_NAME + '", "' + \
               APPLY_FORM_NO + '", "' + IF_COLLECTED + '", "' + OPERATE_STATE + '", ' + 'TO_TIMESTAMP(\'' + OPERATE_TIME + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + OPERATOR_ID + '", "' + \
               CREATE_USER_NAME + '", "' + PARENT_COLLECTED_FORM_NO + '", "' + CHECK_STATUS + '", "' + CHECK_AMOUNT + '", "' + \
               CHECK_DATE + '", "' + CHECK_INFO + '", "' + CHECK_PERSON + '", "' + BUSINESS_DATE + '", "' + PURPOSE + '", ' + 'TO_TIMESTAMP(\'' + APPLY_TIME + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + STATUS + '");'

        line = line.replace('\"', '\'')
        no += 1
        n -= 1

        smcs_cash_file.write(line + '\n')


if __name__ == '__main__':
    # 传参： agency_code, n
    make_sql('130101', 2)


