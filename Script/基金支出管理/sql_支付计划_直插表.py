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
cl_bussnisstype_code = ['KC24','K10025']
cl_bussnisstype_name = ['中心报销','两定机构月结支付']
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

    path = '../../Data_sql/基金支出管理/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'SMRTS_PAY_PLAN'+str(otherStyleTime3)+'.sql'
    file_name_item = path + 'SMRTS_PAY_PLAN_ITEM'+str(otherStyleTime3)+'.sql'
    SMRTS_PAY_PLAN_file = open(file_name, 'w', encoding='utf-8')
    SMRTS_PAY_PLAN_ITEM_file = open(file_name_item, 'w', encoding='utf-8')

    # 主子表sql
    str_head_zhu = "insert into SMRTS_PAY_PLAN values ("
    str_head_item = "insert into SMRTS_PAY_PLAN_ITEM values ("

    no = 1
    while (n > 0):

        ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        CREATE_BY = '-1'
        CREATE_DATE = otherStyleTime
        LAST_MODIFIED_BY = '-1'
        LAST_MODIFIED_DATE = otherStyleTime
        LAST_MODIFIED_VERSION = '1'
        P1 = '2020-07'
        P2 = '001'
        P3 = '城镇职工基本医疗保险'
        P4 = 'YW' + otherStyleTime4 + str(n)
        P5 = P4
        P6 = '00'
        P7 = '上海市统筹'
        P8 = country_code
        P9 = '上海市医保中心'
        # num = int(random.uniform(0, 2))
        num = 1
        P10 = cl_bussnisstype_code[num]
        P11 = cl_bussnisstype_name[num]
        P12 = '3'
        P13 = '1111.11'
        P14 = ''
        P15 = ''
        P16 = ''
        P17 = ''
        P18 = ''
        P19 = ''
        P20 = ''
        P21 = ''
        P22 = ''
        P23 = ''
        P24 = '0'
        P25 = ''
        P26 = ''
        P27 = ''
        P28 = ''
        P29 = ''
        P30 = ''
        AUDIT_STATUS = '00'
        TASK_ID = ''
        NODE_ID = ''
        PROC_DEF_ID = ''
        PROC_INST_ID = ''
        BILL_NO = 'ZFJH' + otherStyleTime4 + str(n)
        BILL_DATE = ''
        VOU_GUID = ''
        VOU_NO = ''
        VOU_DATE = ''
        VOU_STATUS = ''
        SUMMARY = '支付计划'
        EXCHANGE_PLAN_STATUS = '1'
        EXCHANGE_PLAN_ID = 'd514bf63c05f42ecaeee1fb0719681e6'
        VOU_GUID1 = ''
        VOU_NO1 = ''
        VOU_DATE1 = ''
        IS_RETURN = ''


        # 子表
        ID1 = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        ID2 = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        ID3 = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        item_S1 = '310'
        item_S2 = '城镇职工基本医疗保险'
        item_S3 = '2020-07'
        item_S4 = '00400001'
        item_S5 = '上海市支付计划往来单位001'

        item_S402 = '00400002'
        item_S502 = '上海市支付计划往来单位002'

        item_S403 = '00400003'
        item_S503 = '上海市支付计划往来单位003'

        item_S6 = '11111'
        item_S7 = '111111'
        item_S8 = '900'
        item_S9 = '18000'
        item_S10 = '1111.11'
        item_S11 = '12'
        item_S12 = '13'
        item_S13 = '14'
        item_S14 = '15'
        item_S15 = '16'
        item_S16 = '17'
        item_S17 = '18'
        item_S18 = '19'
        item_S19 = '20'
        item_S20 = '21'
        item_S21 = '22'
        item_S22 = '23'
        item_S23 = '24'
        item_S24 = '25'
        item_S25 = '26'
        item_S26 = '27'
        item_S27 = '28'
        item_S28 = '29'
        item_S29 = '30'
        item_S30 = '31'
        item_S31 = '32'
        item_S32 = '33'
        item_S33 = '34'
        item_S34 = '35'
        item_S35 = '36'
        item_S36 = '37'
        item_S37 = '38'
        item_S38 = '39'
        item_S39 = '40'
        item_S40 = '41'
        item_S41 = '42'
        item_S42 = '43'
        item_S43 = '44'
        item_S44 = '45'
        item_S45 = '事业单位'
        item_S46 = 'xxx'
        item_S47 = ''
        item_S48 = ''
        item_S49 = ''
        item_S50 = ''
        item_S51 = ''
        item_S52 = ''
        item_S53 = ''
        item_S54 = ''
        item_S55 = ''
        item_S56 = ''
        item_S57 = ''
        item_S58 = ''
        item_S59 = ''
        item_S60 = ''
        item_S61 = ''
        item_S62 = ''
        item_S63 = ''
        item_S64 = ''
        item_S65 = ''
        item_S66 = ''
        item_S67 = ''
        item_S68 = ''
        item_S69 = ''
        item_S70 = ''
        item_S71 = ''
        item_S72 = ''
        item_S73 = ''
        item_S74 = ''
        item_S75 = ''
        item_S76 = ''
        item_S77 = ''
        item_S78 = ''
        item_S79 = ''
        item_S80 = ''
        item_S81 = ''
        item_S82 = ''
        item_S83 = ''
        item_S84 = ''
        item_S85 = ''
        item_S86 = ''
        item_S87 = ''
        item_S88 = ''
        item_S89 = ''
        item_S90 = ''
        item_S91 = ''
        item_S92 = ''
        item_S93 = ''
        item_S94 = ''
        item_S95 = ''
        item_S96 = ''
        item_S97 = ''
        item_S98 = ''
        item_S99 = '202007310000232847'
        item_S100 = P4
        item_PID = ''
        item_EXCHANGE_PLAN_STATUS = '1'
        item_EXCHANGE_PLAN_ID = 'd514bf63c05f42ecaeee1fb0719681e6'
        item_DETAIL_NO = BILL_NO + '1'

        item_DETAIL_NO2 = BILL_NO + '2'

        item_DETAIL_NO3 = BILL_NO + '3'

        item_BILL_DATE = str(otherStyleTime2)
        item_SUMMARY = '支付计划明细'
        item_PAY_STATUS = ''
        item_VOU_GUID = ''
        item_VOU_NO = ''
        item_VOU_DATE = ''
        item_VOU_STATUS = ''
        item_VOU_GUID1 = ''
        item_VOU_NO1 = ''
        item_VOU_DATE1 = ''
        item_IS_RETURN = ''
        item_CANCEL_PAY = '1'
        item_CANCEL_BY = ''
        item_CANCEL_TIME = ''
        item_CANCEL_REASON = ''
        item_ORDER_NO = '1'



        line = str_head_zhu + '"' + ID + '", "' + CREATE_BY + '", ' + 'TO_TIMESTAMP(\'' + CREATE_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + LAST_MODIFIED_BY + '", TO_TIMESTAMP(\'' + LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), "' + \
               LAST_MODIFIED_VERSION + '", "' + P1 + '", "' + P2 + '", "' + P3 + '", "' + P4 + '", "' + P5 + '", "' + P6 + '", "' + P7 + '", "' + P8 + '", "' + P9 + '", "' + P10 + '", "' + P11 + '", "' + P12 + '", "' + P13 + '", "' + P14 + '", "' + P15\
               + '", "' + P16 + '", "' + P17 + '", "' + P18 + '", "' + P19 + '", "' + P20 + '", "' + P21 + '", "' + P22 + '", "' + P23 + '", "' + P24 + '", "' + P25 + '", "' + P26 + '", "' + P27 + '", "' + P28 + '", "' + P29 + '", "' + P30 + '", "' + \
               AUDIT_STATUS + '", "' + TASK_ID + '", "' + NODE_ID + '", "' + PROC_DEF_ID + '", "' + PROC_INST_ID + '", "' + BILL_NO + '", "' + BILL_DATE + '", "' + VOU_GUID + '", "' + VOU_NO + '", "' + VOU_DATE + '", "' + VOU_STATUS + '", "' + SUMMARY \
               + '", "' + EXCHANGE_PLAN_STATUS + '", "' + EXCHANGE_PLAN_ID + '", "' + VOU_GUID1 + '", "' + VOU_NO1 + '", "' + VOU_DATE1 + '", "' + IS_RETURN + '");'

        line_item1 = str_head_item + '"' + ID1 + '", "' + CREATE_BY + '", ' + 'TO_TIMESTAMP(\'' + CREATE_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + LAST_MODIFIED_BY + '", TO_TIMESTAMP(\'' + LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), "' + \
               LAST_MODIFIED_VERSION + '", "' + item_S1 + '", "' + item_S2 + '", "' + item_S3 + '", "' + item_S4 + '", "' + item_S5 + '", "' + item_S6 + '", "' + item_S7 + '", "' + item_S8 + '", "' + item_S9 + '", "' + item_S10 + '", "' + item_S11 + '", "' + item_S12 + '", "' + item_S13 + '", "' \
               + item_S14 + '", "' + item_S15 + '", "' + item_S16 + '", "' + item_S17 + '", "' + item_S18 + '", "' + item_S19 + '", "' + item_S20 + '", "' + item_S21 + '", "' + item_S22 + '", "' + item_S23 + '", "' + item_S24 + '", "' + item_S25 + '", "' + item_S26 + '", "' + item_S27 + '", "' + \
               item_S28 + '", "' + item_S29 + '", "' + item_S30 + '", "' + item_S31 + '", "' + item_S32 + '", "' + item_S33 + '", "' + item_S34 + '", "' + item_S35 + '", "' + item_S36 + '", "' + item_S37 + '", "' + item_S38 + '", "' + item_S39 + '", "' + item_S40 + '", "' + item_S41 + '", "' + \
               item_S42 + '", "' + item_S43 + '", "' + item_S44 + '", "' + item_S45 + '", "' + item_S46 + '", "' + item_S47 + '", "' + item_S48 + '", "' + item_S49 + '", "' + item_S50 + '", "' + item_S51 + '", "' + item_S52 + '", "' + item_S53 + '", "' + item_S54 + '", "' + item_S55 + '", "' + \
               item_S56 + '", "' + item_S57 + '", "' + item_S58 + '", "' + item_S59 + '", "' + item_S60 + '", "' + item_S61 + '", "' + item_S62 + '", "' + item_S63 + '", "' + item_S64 + '", "' + item_S65 + '", "' + item_S66 + '", "' + item_S67 + '", "' + item_S68 + '", "' + item_S69 + '", "' + \
               item_S70 + '", "' + item_S71 + '", "' + item_S72 + '", "' + item_S73 + '", "' + item_S74 + '", "' + item_S75 + '", "' + item_S76 + '", "' + item_S77 + '", "' + item_S78 + '", "' + item_S79 + '", "' + item_S80 + '", "' + item_S81 + '", "' + item_S82 + '", "' + item_S83 + '", "' + \
               item_S84 + '", "' + item_S85 + '", "' + item_S86 + '", "' + item_S87 + '", "' + item_S88 + '", "' + item_S89 + '", "' + item_S90 + '", "' + item_S91 + '", "' + item_S92 + '", "' + item_S93 + '", "' + item_S94 + '", "' + item_S95 + '", "' + item_S96 + '", "' + item_S97 + '", "' + \
               item_S98 + '", "' + item_S99 + '", "' + item_S100 + '", "' + item_PID + '", "' + item_EXCHANGE_PLAN_STATUS + '", "' + item_EXCHANGE_PLAN_ID + '", "' + item_DETAIL_NO + '", "' + item_BILL_DATE + '", "' + item_SUMMARY + '", "' + item_PAY_STATUS + '", "' + item_VOU_GUID + \
               '", "' + item_VOU_NO + '", "' + item_VOU_DATE + '", "' + item_VOU_STATUS + '", "' + item_VOU_GUID1 + '", "' + item_VOU_NO1 + '", "' + item_VOU_DATE1 + '", "' + item_IS_RETURN + '", "' + item_CANCEL_PAY + '", "' + item_CANCEL_BY + '", "' + item_CANCEL_TIME + '", "' + \
               item_CANCEL_REASON + '", "' + item_ORDER_NO + '");'
        line_item2 = str_head_item + '"' + ID2 + '", "' + CREATE_BY + '", ' + 'TO_TIMESTAMP(\'' + CREATE_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + LAST_MODIFIED_BY + '", TO_TIMESTAMP(\'' + LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), "' + \
               LAST_MODIFIED_VERSION + '", "' + item_S1+ '", "' + item_S2+ '", "' + item_S3+ '", "' + item_S402+ '", "' + item_S502+ '", "' + item_S6+ '", "' + item_S7+ '", "' + item_S8+ '", "' + item_S9+ '", "' + item_S10+ '", "' + item_S11+ '", "' + item_S12+ '", "' + item_S13 + '", "' \
               + item_S14+ '", "' + item_S15+ '", "' + item_S16+ '", "' + item_S17+ '", "' + item_S18+ '", "' + item_S19+ '", "' + item_S20+ '", "' + item_S21+ '", "' + item_S22+ '", "' + item_S23+ '", "' + item_S24+ '", "' + item_S25+ '", "' + item_S26+ '", "' + item_S27+ '", "' + \
               item_S28+ '", "' + item_S29+ '", "' + item_S30+ '", "' + item_S31+ '", "' + item_S32+ '", "' + item_S33+ '", "' + item_S34+ '", "' + item_S35+ '", "' + item_S36+ '", "' + item_S37+ '", "' + item_S38+ '", "' + item_S39+ '", "' + item_S40+ '", "' + item_S41+ '", "' + \
               item_S42+ '", "' + item_S43+ '", "' + item_S44+ '", "' + item_S45+ '", "' + item_S46+ '", "' + item_S47+ '", "' + item_S48+ '", "' + item_S49+ '", "' + item_S50+ '", "' + item_S51+ '", "' + item_S52+ '", "' + item_S53+ '", "' + item_S54+ '", "' + item_S55+ '", "' + \
               item_S56+ '", "' + item_S57+ '", "' + item_S58+ '", "' + item_S59+ '", "' + item_S60+ '", "' + item_S61+ '", "' + item_S62+ '", "' + item_S63+ '", "' + item_S64+ '", "' + item_S65+ '", "' + item_S66+ '", "' + item_S67+ '", "' + item_S68+ '", "' + item_S69+ '", "' + \
               item_S70+ '", "' + item_S71+ '", "' + item_S72+ '", "' + item_S73+ '", "' + item_S74+ '", "' + item_S75+ '", "' + item_S76+ '", "' + item_S77+ '", "' + item_S78+ '", "' + item_S79+ '", "' + item_S80+ '", "' + item_S81+ '", "' + item_S82+ '", "' + item_S83+ '", "' + \
               item_S84+ '", "' + item_S85+ '", "' + item_S86+ '", "' + item_S87+ '", "' + item_S88+ '", "' + item_S89+ '", "' + item_S90+ '", "' + item_S91+ '", "' + item_S92+ '", "' + item_S93+ '", "' + item_S94+ '", "' + item_S95+ '", "' + item_S96+ '", "' + item_S97+ '", "' + \
               item_S98+ '", "' + item_S99+ '", "' + item_S100+ '", "' + item_PID+ '", "' + item_EXCHANGE_PLAN_STATUS+ '", "' + item_EXCHANGE_PLAN_ID+ '", "' + item_DETAIL_NO2+ '", "' + item_BILL_DATE+ '", "' + item_SUMMARY+ '", "' + item_PAY_STATUS+ '", "' + item_VOU_GUID + \
               '", "' + item_VOU_NO+ '", "' + item_VOU_DATE+ '", "' + item_VOU_STATUS+ '", "' + item_VOU_GUID1+ '", "' + item_VOU_NO1+ '", "' + item_VOU_DATE1+ '", "' + item_IS_RETURN+ '", "' + item_CANCEL_PAY+ '", "' + item_CANCEL_BY+ '", "' + item_CANCEL_TIME+ '", "' + \
               item_CANCEL_REASON+ '", "' + item_ORDER_NO + '");'
        line_item3 = str_head_item + '"' + ID3 + '", "' + CREATE_BY + '", ' + 'TO_TIMESTAMP(\'' + CREATE_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + LAST_MODIFIED_BY + '", TO_TIMESTAMP(\'' + LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), "' + \
               LAST_MODIFIED_VERSION + '", "' + item_S1 + '", "' + item_S2 + '", "' + item_S3 + '", "' + item_S403 + '", "' + item_S503 + '", "' + item_S6 + '", "' + item_S7 + '", "' + item_S8 + '", "' + item_S9 + '", "' + item_S10 + '", "' + item_S11 + '", "' + item_S12 + '", "' + item_S13 + '", "' \
               + item_S14 + '", "' + item_S15 + '", "' + item_S16 + '", "' + item_S17 + '", "' + item_S18 + '", "' + item_S19 + '", "' + item_S20 + '", "' + item_S21 + '", "' + item_S22 + '", "' + item_S23 + '", "' + item_S24 + '", "' + item_S25 + '", "' + item_S26 + '", "' + item_S27 + '", "' + \
               item_S28 + '", "' + item_S29 + '", "' + item_S30 + '", "' + item_S31 + '", "' + item_S32 + '", "' + item_S33 + '", "' + item_S34 + '", "' + item_S35 + '", "' + item_S36 + '", "' + item_S37 + '", "' + item_S38 + '", "' + item_S39 + '", "' + item_S40 + '", "' + item_S41 + '", "' + \
               item_S42 + '", "' + item_S43 + '", "' + item_S44 + '", "' + item_S45 + '", "' + item_S46 + '", "' + item_S47 + '", "' + item_S48 + '", "' + item_S49 + '", "' + item_S50 + '", "' + item_S51 + '", "' + item_S52 + '", "' + item_S53 + '", "' + item_S54 + '", "' + item_S55 + '", "' + \
               item_S56 + '", "' + item_S57 + '", "' + item_S58 + '", "' + item_S59 + '", "' + item_S60 + '", "' + item_S61 + '", "' + item_S62 + '", "' + item_S63 + '", "' + item_S64 + '", "' + item_S65 + '", "' + item_S66 + '", "' + item_S67 + '", "' + item_S68 + '", "' + item_S69 + '", "' + \
               item_S70 + '", "' + item_S71 + '", "' + item_S72 + '", "' + item_S73 + '", "' + item_S74 + '", "' + item_S75 + '", "' + item_S76 + '", "' + item_S77 + '", "' + item_S78 + '", "' + item_S79 + '", "' + item_S80 + '", "' + item_S81 + '", "' + item_S82 + '", "' + item_S83 + '", "' + \
               item_S84 + '", "' + item_S85 + '", "' + item_S86 + '", "' + item_S87 + '", "' + item_S88 + '", "' + item_S89 + '", "' + item_S90 + '", "' + item_S91 + '", "' + item_S92 + '", "' + item_S93 + '", "' + item_S94 + '", "' + item_S95 + '", "' + item_S96 + '", "' + item_S97 + '", "' + \
               item_S98 + '", "' + item_S99 + '", "' + item_S100 + '", "' + item_PID + '", "' + item_EXCHANGE_PLAN_STATUS + '", "' + item_EXCHANGE_PLAN_ID + '", "' + item_DETAIL_NO3 + '", "' + item_BILL_DATE + '", "' + item_SUMMARY + '", "' + item_PAY_STATUS + '", "' + item_VOU_GUID + \
               '", "' + item_VOU_NO + '", "' + item_VOU_DATE + '", "' + item_VOU_STATUS + '", "' + item_VOU_GUID1 + '", "' + item_VOU_NO1 + '", "' + item_VOU_DATE1 + '", "' + item_IS_RETURN + '", "' + item_CANCEL_PAY + '", "' + item_CANCEL_BY + '", "' + item_CANCEL_TIME + '", "' + \
               item_CANCEL_REASON + '", "' + item_ORDER_NO + '");'





        line = line.replace('\"', '\'')
        line_item1 = line_item1.replace('\"', '\'')
        line_item2 = line_item2.replace('\"', '\'')
        line_item3 = line_item3.replace('\"', '\'')
        no += 1
        n -= 1

        SMRTS_PAY_PLAN_file.write(line + '\n')
        SMRTS_PAY_PLAN_file.write(line_item1 + '\n')
        SMRTS_PAY_PLAN_ITEM_file.write(line_item2 + '\n')
        SMRTS_PAY_PLAN_ITEM_file.write(line_item3 + '\n')



if __name__ == '__main__':
    # 传参： country_code, n
    make_sql('00', 5)


