# -*- coding: utf-8 -*
import datetime
import cx_Oracle
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
    # db = cx_Oracle.connect('ybjjdb/test1@10.10.66.159:1521/orcl')
    db = cx_Oracle.connect('ptmifc/1@10.10.66.159:1521/orcl')
    cr = db.cursor() #创建游标

    no = 1
    while (n > 0):

        ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        CREATE_BY = 'script'
        CREATE_DATE = datetime.datetime.now()
        LAST_MODIFIED_BY = '-1'
        LAST_MODIFIED_DATE = datetime.datetime.now()
        LAST_MODIFIED_VERSION = '1'
        FUND_BATCH_NO = 'script'+ str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        BATCH_NO = FUND_BATCH_NO
        BUSINESS_CODE = 'SMLX'
        AGENCY_CODE = '00'
        INSURANCE_CODE = '310'
        INSURANCE_NAME = '城镇职工基本医疗保险'
        COUNTRY_CODE = ''
        COUNTRY_NAME = ''
        PAY_TYPE = ''
        PAY_TYPE_NAME = ''
        TOTAL_MONEY = 15.00
        AGENCY_NAME = '上海市医疗保障局'
        PAY_NO = '6666222021252012'
        PAY_NAME = '上海医保局支出户'
        PAY_TIME = datetime.datetime.now()
        DATA_STATUS = '06'
        DATA_STATUS_NAME = '回盘成功'
        REFUND_VOUCHER = ''
        REFUND_REASON = ''
        BANK_CODE = '313'
        IDENTITY_CODE = '3102'
        IDENTITY_NAME = '划拨往来单位2'
        FAIL_REASON_CODE = ''
        FAIL_REASON = ''
        CANCEL_PAY_TIME = ''
        CANCEL_PEOPLE = ''
        CANCEL_PAY_REASON = ''
        IS_KH = 'Y'
        PAY_BANK_NAME = '上海银行'
        RECIP_BANK_NO = ''
        RECIP_ACC = '6666525201256352'
        RECIP_NAME = '划拨往来单位2'
        RECIP_BRANCH = '上海银行'
        SETTLE_TYPE = '03'
        SETTLE_TYPE_NAME = '网银支付'
        BUSINESS_TYPE = 'K90017'
        BUSINESS_TYPE_NAME = '基金划拨-利息上解'
        CHECK_TIME = ''
        CHECK_NO = ''
        PAY_PERIOD = '202011'
        PAY_ARRIVE_TIME = datetime.datetime.now()
        REFUND_VOU_GUID = ''
        REFUND_VOU_NO = ''
        EN_ACC_VOU_GUID = ''
        EN_ACC_VOU_NO = ''
        EN_ACC_VOU_DATE = ''
        REFUND_VOU_DATE = ''


        sqlG = " insert into SMSBM_MEDICAL_BANK_SINGLE(ID, CREATE_BY, CREATE_DATE, LAST_MODIFIED_BY, LAST_MODIFIED_DATE, LAST_MODIFIED_VERSION, FUND_BATCH_NO, BATCH_NO, BUSINESS_CODE, AGENCY_CODE, INSURANCE_CODE, INSURANCE_NAME, COUNTRY_CODE, COUNTRY_NAME, PAY_TYPE, PAY_TYPE_NAME, TOTAL_MONEY, AGENCY_NAME, PAY_NO, PAY_NAME, PAY_TIME, DATA_STATUS, DATA_STATUS_NAME, REFUND_VOUCHER, REFUND_REASON, BANK_CODE, IDENTITY_CODE, IDENTITY_NAME, FAIL_REASON_CODE, FAIL_REASON, CANCEL_PAY_TIME, CANCEL_PEOPLE, CANCEL_PAY_REASON, IS_KH, PAY_BANK_NAME, RECIP_BANK_NO, RECIP_ACC, RECIP_NAME, RECIP_BRANCH, SETTLE_TYPE, SETTLE_TYPE_NAME, BUSINESS_TYPE, BUSINESS_TYPE_NAME, CHECK_TIME, CHECK_NO, PAY_PERIOD, PAY_ARRIVE_TIME, REFUND_VOU_GUID, REFUND_VOU_NO, EN_ACC_VOU_GUID, EN_ACC_VOU_NO, EN_ACC_VOU_DATE, REFUND_VOU_DATE)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49,:50,:51,:52,:53) "

        cr.execute(sqlG, (ID, CREATE_BY, CREATE_DATE, LAST_MODIFIED_BY, LAST_MODIFIED_DATE, LAST_MODIFIED_VERSION, FUND_BATCH_NO, BATCH_NO, BUSINESS_CODE, AGENCY_CODE, INSURANCE_CODE, INSURANCE_NAME, COUNTRY_CODE, COUNTRY_NAME, PAY_TYPE, PAY_TYPE_NAME, TOTAL_MONEY, AGENCY_NAME, PAY_NO, PAY_NAME, PAY_TIME, DATA_STATUS, DATA_STATUS_NAME, REFUND_VOUCHER, REFUND_REASON, BANK_CODE, IDENTITY_CODE, IDENTITY_NAME, FAIL_REASON_CODE, FAIL_REASON, CANCEL_PAY_TIME, CANCEL_PEOPLE, CANCEL_PAY_REASON, IS_KH, PAY_BANK_NAME, RECIP_BANK_NO, RECIP_ACC, RECIP_NAME, RECIP_BRANCH, SETTLE_TYPE, SETTLE_TYPE_NAME, BUSINESS_TYPE, BUSINESS_TYPE_NAME, CHECK_TIME, CHECK_NO, PAY_PERIOD, PAY_ARRIVE_TIME, REFUND_VOU_GUID, REFUND_VOU_NO, EN_ACC_VOU_GUID, EN_ACC_VOU_NO, EN_ACC_VOU_DATE, REFUND_VOU_DATE))

        no += 1
        n -= 1

    cr.close()
    db.commit()
    db.close()
    endtime = datetime.datetime.now()
    print("耗时H：" + str(round((endtime - starttime).seconds / 3600, 2)))


if __name__ == '__main__':
    # 传参： aab034, n
    # 第一参数：0-上海 1-黄埔，2-河北省
    # 第二参数：0-310 1-390
    make_sql(0,0, 1)


