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
otherStyleTime4 = now.strftime("%H%M%S")

def make_sql(aab034, n):

    path = '../../Data_sql/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'SMAM_PAYMENTS_DETAIL'+str(otherStyleTime3)+'.sql'
    smcs_cash_file = open(file_name, 'w', encoding='utf-8')

    # 主表sql
    str_head_zhu = "insert into SMAM_PAYMENTS_DETAIL values ("

    no = 1
    while (n > 0):

        ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        CREATE_BY = '-1'
        CREATE_DATE = otherStyleTime
        LAST_MODIFIED_BY = '-1'
        LAST_MODIFIED_DATE = otherStyleTime
        LAST_MODIFIED_VERSION = '1'
        AAB034 = aab034
        BALANCE_TYPE = ''
        BANK_NOTE = ''
        BK_SEQ = otherStyleTime3 + ran_strx("0123456789", 10)
        BUS_FUN_NO = ''
        COUNT = str(round(random.uniform(1000, 10), 2))
        CURRENCY = ''
        DEAL_DATE = str(otherStyleTime)
        DEAL_TIME = str(otherStyleTime)
        DR_FLAG = ''
        OPPO_SIDE_BANK = '测试银行'
        OPPO_SIDE_NAME = '测试银行户名'
        OPPO_SIDE_NO = ran_strx("0123456789", 16)
        #经办机构账户名称，根据实际账户名称修改
        OUR_SIDE_NAME = '上海银行支出户'
        #经办机构账号，根据实际账户名称修改
        OUR_SIDE_NO = '31311112222333344443-1'
        REMARK = '备注'
        SERIAL_NUM = ''
        SPARE1 = ''
        SPARE2 = ''
        SPARE3 = ''
        SURPLUS_COUNT = str(round(random.uniform(1000, 10), 2))
        OUR_SIDE_PARENT_NO = ''
        AAE140 = '110'
        PLAN_ID = ''
        REC_NO = ''
        REC_TIME = ''
        REC_STATUS = ''
        MARK_TYPE = ''
        AUDIT_STATUS = '04'
        TASK_ID = ''
        NODE_ID = ''
        PROC_DEF_ID = ''
        PROC_INST_ID = ''
        DATA_FROM = ''
        SESSION_ID = ''
        ACC_BRANCH = '313'
        VOUCH_TYPE = 'ert'
        VOUCH_NO = '123456789'
        BUSI_TYPE = '001'
        USE = '用途'
        PAY_DATE = str(otherStyleTime)
        BATCH_NO = ''
        INSURANCE_NAME = '城镇职工基本医疗保险'
        SUMMARY = '摘要'
        DEBIT_AMT = str(round(random.uniform(1000, 10), 2))
        CREDIT_AMT = str(round(random.uniform(1000, 10), 2))
        TRAN_CODE = '123'
        EXCHANGE_PLAN_ID = ''

        line = str_head_zhu + '"' + ID + '", "' + CREATE_BY + '", ' + 'TO_TIMESTAMP(\'' + CREATE_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + LAST_MODIFIED_BY + '", TO_TIMESTAMP(\'' + LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), "' + \
               LAST_MODIFIED_VERSION + '", "' + AAB034 + '", "' + BALANCE_TYPE + '", "' + BANK_NOTE + '", "' + BK_SEQ + '", "' + BUS_FUN_NO + '", "' + COUNT + '", "' + CURRENCY + '", "' + DEAL_DATE + '", "' + DEAL_TIME + '", "' + DR_FLAG + '", "' + OPPO_SIDE_BANK + '", "' + OPPO_SIDE_NAME + '", "' + OPPO_SIDE_NO + '", "' + OUR_SIDE_NAME + '", "' + OUR_SIDE_NO + '", "' + REMARK + '", "' + SERIAL_NUM + '", "' + SPARE1 + '", "' + SPARE2 + '", "' + SPARE3 + '", "' + SURPLUS_COUNT + '", "' + OUR_SIDE_PARENT_NO + '", "' + AAE140 + '", "' + PLAN_ID + '", "' + REC_NO + '", "' + REC_TIME + '", "' + REC_STATUS + '", "' + MARK_TYPE + '", "' + AUDIT_STATUS + '", "' + TASK_ID + '", "' + NODE_ID + '", "' + PROC_DEF_ID + '", "' + PROC_INST_ID + '", "' + DATA_FROM + '", "' + SESSION_ID + '", "' + ACC_BRANCH + '", "' + VOUCH_TYPE + '", "' + VOUCH_NO + '", "' + BUSI_TYPE + '", "' + USE + '", "' + PAY_DATE + '", "' + BATCH_NO + '", "' + INSURANCE_NAME + '", "' + SUMMARY + '", "' + DEBIT_AMT + '", "' + CREDIT_AMT + '", "' + TRAN_CODE + '", "' + EXCHANGE_PLAN_ID + '");'

        line = line.replace('\"', '\'')
        no += 1
        n -= 1

        smcs_cash_file.write(line + '\n')


if __name__ == '__main__':
    # 传参： aab034, n
    make_sql('00', 1)


