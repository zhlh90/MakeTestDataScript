# -*- coding: utf-8 -*
import datetime
# import cx_Oracle
import pymysql
import random
import string

# 银行类型
cl_banktype = ['00', '01']
# cl_bussniss_type = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13','15','16']
cl_bussniss_type = ['01', '02', '03', '04', '10', '12', '13','15','16']
cl_pay_target = ['00', '01', '02', '03', '04', '05', '06']
cl_hospital_lv = ['00', '01', '02', '03', '04', '05', '06']
cl_medical_type = ['00', '01', '02', '03', '04', '05']
# 经办机构
cl_agency_code = ['00','01','1300']
cl_agency_name = ['上海保险事业管理局','黄浦区保险事业管理局','河北省']

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

    starttime = datetime.datetime.now()
    # 建立数据库连接
    db = pymysql.Connect(
        host='10.10.66.158',##mysql服务器地址
        port=3306,##mysql服务器端口号
        user='rsyb',##用户名
        passwd='1',##密码
        db='ybjjdb',##数据库名
        charset='utf8'##连接编码
    )
    #创建游标
    cr = db.cursor()

    no = 1
    while (n > 0):

        ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        CREATE_BY = 'script'
        CREATE_DATE = datetime.datetime.now()
        LAST_MODIFIED_BY = '-1'
        LAST_MODIFIED_DATE = datetime.datetime.now()
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
        REC_TIME = datetime.datetime.now()
        REC_STATUS = ''
        MARK_TYPE = 0
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
        OPERATE_STATE = ''
        OPERATE_TIME = datetime.datetime.now()
        OPERATOR_ID = ''
        AGENCY_NAME = cl_agency_name[agency_code_num]

        sqlG = "insert into SMAM_PAYMENTS_DETAIL values (%(ID)s, %(CREATE_BY)s, %(CREATE_DATE)s, %(LAST_MODIFIED_BY)s, %(LAST_MODIFIED_DATE)s, %(LAST_MODIFIED_VERSION)s, %(AGENCY_CODE)s, %(BALANCE_TYPE)s, %(BANK_NOTE)s, %(BK_SEQ)s, %(BUS_FUN_NO)s, %(COUNT)s, %(CURRENCY)s, %(DEAL_DATE)s, %(DEAL_TIME)s, %(DR_FLAG)s, %(OPPO_SIDE_BANK)s, %(OPPO_SIDE_NAME)s, %(OPPO_SIDE_NO)s, %(OUR_SIDE_NAME)s, %(OUR_SIDE_NO)s, %(REMARK)s, %(SERIAL_NUM)s, %(SPARE1)s, %(SPARE2)s, %(SPARE3)s, %(SURPLUS_COUNT)s, %(OUR_SIDE_PARENT_NO)s, %(INSURANCE_CODE)s, %(PLAN_ID)s, %(REC_NO)s, %(REC_TIME)s, %(REC_STATUS)s, %(MARK_TYPE)s, %(AUDIT_STATUS)s, %(TASK_ID)s, %(NODE_ID)s, %(PROC_DEF_ID)s, %(PROC_INST_ID)s, %(DATA_FROM)s, %(SESSION_ID)s, %(ACC_BRANCH)s, %(VOUCH_TYPE)s, %(VOUCH_NO)s, %(BUSI_TYPE)s, %(USE_PURPOSE)s, %(PAY_DATE)s, %(BATCH_NO)s, %(INSURANCE_NAME)s, %(SUMMARY)s, %(DEBIT_AMT)s, %(CREDIT_AMT)s, %(TRAN_CODE)s, %(EXCHANGE_PLAN_ID)s, %(OPERATE_STATE)s, %(OPERATE_TIME)s, %(OPERATOR_ID)s, %(AGENCY_NAME)s)"
        value = {
        "ID":ID,
        "CREATE_BY":CREATE_BY,
        "CREATE_DATE":CREATE_DATE,
        "LAST_MODIFIED_BY":LAST_MODIFIED_BY,
        "LAST_MODIFIED_DATE":LAST_MODIFIED_DATE,
        "LAST_MODIFIED_VERSION":LAST_MODIFIED_VERSION,
        "AGENCY_CODE":AGENCY_CODE,
        "BALANCE_TYPE":BALANCE_TYPE,
        "BANK_NOTE":BANK_NOTE,
        "BK_SEQ":BK_SEQ,
        "BUS_FUN_NO":BUS_FUN_NO,
        "COUNT":COUNT,
        "CURRENCY":CURRENCY,
        "DEAL_DATE":DEAL_DATE,
        "DEAL_TIME":DEAL_TIME,
        "DR_FLAG":DR_FLAG,
        "OPPO_SIDE_BANK":OPPO_SIDE_BANK,
        "OPPO_SIDE_NAME":OPPO_SIDE_NAME,
        "OPPO_SIDE_NO":OPPO_SIDE_NO,
        "OUR_SIDE_NAME":OUR_SIDE_NAME,
        "OUR_SIDE_NO":OUR_SIDE_NO,
        "REMARK":REMARK,
        "SERIAL_NUM":SERIAL_NUM,
        "SPARE1":SPARE1,
        "SPARE2":SPARE2,
        "SPARE3":SPARE3,
        "SURPLUS_COUNT":SURPLUS_COUNT,
        "OUR_SIDE_PARENT_NO":OUR_SIDE_PARENT_NO,
        "INSURANCE_CODE":INSURANCE_CODE,
        "PLAN_ID":PLAN_ID,
        "REC_NO":REC_NO,
        "REC_TIME":REC_TIME,
        "REC_STATUS":REC_STATUS,
        "MARK_TYPE":MARK_TYPE,
        "AUDIT_STATUS":AUDIT_STATUS,
        "TASK_ID":TASK_ID,
        "NODE_ID":NODE_ID,
        "PROC_DEF_ID":PROC_DEF_ID,
        "PROC_INST_ID":PROC_INST_ID,
        "DATA_FROM":DATA_FROM,
        "SESSION_ID":SESSION_ID,
        "ACC_BRANCH":ACC_BRANCH,
        "VOUCH_TYPE":VOUCH_TYPE,
        "VOUCH_NO":VOUCH_NO,
        "BUSI_TYPE":BUSI_TYPE,
        "USE_PURPOSE":USE_PURPOSE,
        "PAY_DATE":PAY_DATE,
        "BATCH_NO":BATCH_NO,
        "INSURANCE_NAME":INSURANCE_NAME,
        "SUMMARY":SUMMARY,
        "DEBIT_AMT":DEBIT_AMT,
        "CREDIT_AMT":CREDIT_AMT,
        "TRAN_CODE":TRAN_CODE,
        "EXCHANGE_PLAN_ID":EXCHANGE_PLAN_ID,
        "OPERATE_STATE":OPERATE_STATE,
        "OPERATE_TIME":OPERATE_TIME,
        "OPERATOR_ID":OPERATOR_ID,
        "AGENCY_NAME":AGENCY_NAME,

        }
        cr.execute(sqlG, value)

        no += 1
        n -= 1

    cr.close()
    db.commit()
    db.close()
    endtime = datetime.datetime.now()
    print("耗时H：" + str(round((endtime - starttime).seconds / 3600, 2)))


if __name__ == '__main__':
    # 第一参数：0-上海 1-黄埔，2-河北省
    # 第二参数：0-310 1-390
    # 第三参数：数据条数
    make_sql(0,1,1)
    make_sql(1,1,1)


