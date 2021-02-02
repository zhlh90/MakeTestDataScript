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
# 经办机构
cl_agency_code = ['00','01','1300','520201']
cl_agency_name = ['上海保险事业管理局','黄浦区保险事业管理局','河北省','六盘水市本级']

# 险种
cl_ins_code = ['310','390']
cl_ins_name = ['城镇职工基本医疗保险','城乡居民基本医疗保险']

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

def make_sql(agency_code_num,ins_no, n):

    path = '../../Data_sql/基础数据/'
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
        CREATE_BY = 'script'
        CREATE_DATE = otherStyleTime
        LAST_MODIFIED_BY = '-1'
        LAST_MODIFIED_DATE = otherStyleTime
        LAST_MODIFIED_VERSION = '1'
        AGENCY_CODE = cl_agency_code[agency_code_num]
        BALANCE_TYPE = ''
        BANK_NOTE = ''
        BK_SEQ = otherStyleTime3 + ran_strx("0123456789", 10)
        BUS_FUN_NO = ''
        COUNT = str(round(random.uniform(1000, 10), 2))
        CURRENCY = ''
        DEAL_DATE = otherStyleTime
        DEAL_TIME = otherStyleTime
        DR_FLAG = '1'
        OPPO_SIDE_BANK = '测试银行'
        OPPO_SIDE_NAME = '测试银行户名'
        OPPO_SIDE_NO = ran_strx("0123456789", 16)
        OUR_SIDE_NAME = '上海银行支出户'
        OUR_SIDE_NO = '31311112222333344443-1'
        REMARK = '备注'
        SERIAL_NUM = ''
        SPARE1 = ''
        SPARE2 = ''
        SPARE3 = ''
        SURPLUS_COUNT = str(round(random.uniform(1000, 10), 2))
        OUR_SIDE_PARENT_NO = ''
        INSURANCE_CODE = cl_ins_code[ins_no]
        PLAN_ID = ''
        REC_NO = ''
        REC_TIME = otherStyleTime
        REC_STATUS = ''
        MARK_TYPE = '0'
        AUDIT_STATUS = '04'
        TASK_ID = ''
        NODE_ID = ''
        PROC_DEF_ID = ''
        PROC_INST_ID = ''
        DATA_FROM = ''
        SESSION_ID = ''
        ACC_BRANCH = '313'
        VOUCH_TYPE = 'JZ'
        VOUCH_NO = '123456789'
        BUSI_TYPE = '001'
        USE_PURPOSE = '用途'
        PAY_DATE = otherStyleTime
        # 批次号
        BATCH_NO = ''
        INSURANCE_NAME = cl_ins_name[ins_no]
        SUMMARY = '摘要'
        DEBIT_AMT = str(round(random.uniform(1000, 10), 2))
        CREDIT_AMT = str(round(random.uniform(1000, 10), 2))
        TRAN_CODE = '123'
        EXCHANGE_PLAN_ID = ''
        OPERATE_STATE = '6'
        OPERATE_TIME = otherStyleTime
        OPERATOR_ID = ''
        AGENCY_NAME = cl_agency_name[agency_code_num]

        line = str_head_zhu + '"' + ID + '", "' + CREATE_BY + '", "' + CREATE_DATE + '", "' + LAST_MODIFIED_BY + '", "' + LAST_MODIFIED_DATE + '", "' + LAST_MODIFIED_VERSION + '", "' + AGENCY_CODE + '", "' + BALANCE_TYPE + '", "' + BANK_NOTE + '", "' + BK_SEQ + '", "' + BUS_FUN_NO + '", "' + COUNT + '", "' + CURRENCY + '", "' + DEAL_DATE + '", "' + DEAL_TIME + '", "' + DR_FLAG + '", "' + OPPO_SIDE_BANK + '", "' + OPPO_SIDE_NAME + '", "' + OPPO_SIDE_NO + '", "' + OUR_SIDE_NAME + '", "' + OUR_SIDE_NO + '", "' + REMARK + '", "' + SERIAL_NUM + '", "' + SPARE1 + '", "' + SPARE2 + '", "' + SPARE3 + '", "' + SURPLUS_COUNT + '", "' + OUR_SIDE_PARENT_NO + '", "' + INSURANCE_CODE + '", "' + PLAN_ID + '", "' + REC_NO + '", "' + REC_TIME + '", "' + REC_STATUS + '", "' + MARK_TYPE + '", "' + AUDIT_STATUS + '", "' + TASK_ID + '", "' + NODE_ID + '", "' + PROC_DEF_ID + '", "' + PROC_INST_ID + '", "' + DATA_FROM + '", "' + SESSION_ID + '", "' + ACC_BRANCH + '", "' + VOUCH_TYPE + '", "' + VOUCH_NO + '", "' + BUSI_TYPE + '", "' + USE_PURPOSE + '", "' + PAY_DATE + '", "' + BATCH_NO + '", "' + INSURANCE_NAME + '", "' + SUMMARY + '", "' + DEBIT_AMT + '", "' + CREDIT_AMT + '", "' + TRAN_CODE + '", "' + EXCHANGE_PLAN_ID + '", "' + OPERATE_STATE + '", "' + OPERATE_TIME + '", "' + OPERATOR_ID + '", "' + AGENCY_NAME + '");'

        line = line.replace('\"', '\'')
        no += 1
        n -= 1

        smcs_cash_file.write(line + '\n')


if __name__ == '__main__':
    # 第一参数：0-上海 1-黄埔，2-河北省，3-六盘水市本级
    # 第二参数：0-310 1-390
    # 第三参数：数据条数
    make_sql(3,0,5)


