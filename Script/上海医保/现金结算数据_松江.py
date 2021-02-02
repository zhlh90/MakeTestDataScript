# -*- coding: utf-8 -*
import datetime
import time

#import pandas as pd
import random
import string
from calendar import calendar

from Script import shenfenzhenghao
from enum import Enum
import os

# 银行类型
cl_banktype = ['00']
# cl_banktype = ['00', '01']


# cl_bussniss_type = ['01', '02', '03', '04', '10', '12', '13', '15', '16']
# cl_bussniss_type = ['02']   # 业务类型
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


# contry_code区县中心代码rg_name区县名，n条数
def make_sql(country_code, rg_name, cl_bussniss_type, n):

    path = '../../Data_sql/上海医保/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'smcs_cash'+cl_bussniss_type+str(otherStyleTime3)+'.sql'
    # file_name1 = path + 'smcs_cash_detail'+str(otherStyleTime3)+'.sql'
    # file_name2 = path + 'smcs_bank_account'+str(otherStyleTime3)+'.sql'
    smcs_cash_file = open(file_name, 'w', encoding='utf-8')
    # smcs_cash_detail_file = open(file_name1, 'w', encoding='utf-8')
    # smcs_bank_account_file = open(file_name2, 'w', encoding='utf-8')

    # 主表sql
    str_head_zhu = "insert into smcs_cash values ("
    str_head_mingxi = "insert into smcs_cash_detail values ("
    str_head_bankaccount = "insert into smcs_bank_account values ("

    no = 1
    while (n > 0):
# 生成小写字母加数字30位
        ID = ''.join(random.sample(string.ascii_lowercase + string.digits, 30))
        ID2 = ''.join(random.sample(string.ascii_lowercase + string.digits, 30))
        ID3 = ''.join(random.sample(string.ascii_lowercase + string.digits, 30))
        CREATE_BY = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
        CREATE_DATE = datetime.datetime.fromisoformat('2020-11-22 09:00:00').strftime("%Y-%m-%d %H:%M:%S")
        LAST_MODIFIED_BY = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        LAST_MODIFIED_DATE = otherStyleTime
        LAST_MODIFIED_VERSION = '1'
        MESSAGE_TYPE = '1'
        # APPLY_NO = ''.join(random.sample(string.ascii_lowercase + string.digits, 20))

        APPLY_SUB_NO = '01'
        APPLY_SUB_NO_cx = '02'

        # BILL_NO = ''.join(random.sample(string.ascii_lowercase + string.digits, 16))

        COMMON_ACCOUNT = ran_strx("0123456789", 8)
        APPLY_USER_NAME = '肖英贤'
        APPLY_USER_CARD_ID = '652801195101015216'
        MEDICAL_CARD = ran_strx("0123456789", 10)
        CURRENT_YEAR_PAY = 100
        ALL_YEAR_PAY = 200
        PLAN_PAY = 300
        ADDITIONAL_PAY = 400
        OTHER_PAY = 500

        CURRENT_YEAR_PAY_cx = -100
        ALL_YEAR_PAY_cx = -200
        PLAN_PAY_cx = -300
        ADDITIONAL_PAY_cx = -400
        OTHER_PAY_cx = -500

        REFUND_AMOUNT = round((CURRENT_YEAR_PAY + ALL_YEAR_PAY + PLAN_PAY + ADDITIONAL_PAY + OTHER_PAY), 2)
        REFUND_AMOUNT_cx = round((CURRENT_YEAR_PAY_cx + ALL_YEAR_PAY_cx + PLAN_PAY_cx + ADDITIONAL_PAY_cx + OTHER_PAY_cx), 2)

        BUSSINESS_TYPE = cl_bussniss_type
        if BUSSINESS_TYPE == '03' or BUSSINESS_TYPE=='13':
            MAIL_ADDRESS = '北京市海淀区用友路1号'
            MAIL_ADDRESS_CODE = ran_strx("0123456789", 6)
        else:
            MAIL_ADDRESS = ''
            MAIL_ADDRESS_CODE =''

        if BUSSINESS_TYPE == '10':
            REFUND_AMOUNT = OTHER_PAY
            CURRENT_YEAR_PAY = 0
            ALL_YEAR_PAY = 0
            PLAN_PAY = 0
            ADDITIONAL_PAY = 0
            # 撤销
            REFUND_AMOUNT_cx = OTHER_PAY_cx
            CURRENT_YEAR_PAY_cx = 0
            ALL_YEAR_PAY_cx = 0
            PLAN_PAY_cx = 0
            ADDITIONAL_PAY_cx = 0

        banktype = int(random.uniform(0, cl_banktype.__len__()))
        BANK_TYPE = cl_banktype[banktype]
        if BANK_TYPE=='00':
            # 代办
            BANK_CODE = '313290000017'
            BANK_CARD_ACCOUNT = '622468000106695774'
            # AGENT_USER_NAME = '委托待办人''测试李'
            AGENT_USER_NAME = '肖英贤'

        else:
            BANK_CODE = ran_strx("0123456789", 12)
            BANK_CARD_ACCOUNT = ran_strx("0123456789", 20)
            AGENT_USER_NAME = ''

        #支付类型为单位集中时单位编码才有值
        if BUSSINESS_TYPE == '04':
            # UNIT_CODE = '206003001'
            UNIT_CODE = '00127046'
            UNIT_NAME = '百联集团有限公司'
        else:
            UNIT_CODE = ''
            UNIT_NAME = ''
        ACCEPT_ACCOUNT_NAME = ''
        ACCEPT_ACCOUNT = ''
        AEECPT_BANK_NAME = ''
        BILL_CREATER = ''
        BILL_CREATE_TIME = ''
        BILL_CREATE_AREA = ''
        VOUCHER_TYPE = ''
        VOUCHER_STATUS = ''
        VOUVHER_CREATE_TIME = ''
        BILL_STATUS = ''
        RES1 = ''
        RES2 = ''
        RES3 = ''
        RES4 = ''
        COUNTRY_CODE = country_code
        REFUND_CATEGORY = ''
        ACCOUNT_STATE = '00'
        BILL_STATE = '00'
        BILL_DATE = ''
        HANDWORK_FLAG = ''
        NOTE_NUM = ''
        FAIL_REASON = ''
        FUND_BATCH_NUM = ''
        EXCHANGE_NUM = '123456'
        REFUND_STATE = ''
        WORK_FLOW_STATE = '1'
        TASK_ID = ''
        NODE_ID = ''
        PROC_DEF_ID = ''
        PROC_INST_ID = ''
        CHANGE_STATUS = ''
        VOU_GUID = ''
        VOU_NO = ''
        RG_NAME = '上海市松江区'
        SERVICE_NODE_NAME = ''
        SERVICE_NODE_CODE = ''

        PAY_TYPE = ''
        # bussniss_type 与 pay_type 对应关系
        if (BUSSINESS_TYPE == '01' or BUSSINESS_TYPE == '16') :
            PAY_TYPE = 1
        if (BUSSINESS_TYPE == '02' or BUSSINESS_TYPE == '10' or BUSSINESS_TYPE == '12' or BUSSINESS_TYPE == '15') :
            PAY_TYPE = 2
        if (BUSSINESS_TYPE == '03' or BUSSINESS_TYPE == '13'):
            PAY_TYPE = 3
        if (BUSSINESS_TYPE == '04'):
            PAY_TYPE = 4
        # 业务单据类型为10 转移接续支付时，以下三个字段才有值
        ORI_ACCEPT_ACCOUNT_NAME = ''
        ORI_ACCEPT_ACCOUNT = ''
        ORI_ACCEPT_BANK_NAME = ''
        bank_name=['上海银行','邮储银行','招商银行']
        if BUSSINESS_TYPE == '10':
            ORI_ACCEPT_ACCOUNT_NAME = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤",
                                           2)
            ORI_ACCEPT_ACCOUNT = ran_strx("0123456789", 32)
            ORI_ACCEPT_BANK_NAME = bank_name[int(random.uniform(0,2))]
            ACCEPT_ACCOUNT_NAME = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤",
                                           2)
            ACCEPT_ACCOUNT = ran_strx("0123456789", 32)
            AEECPT_BANK_NAME =  bank_name[int(random.uniform(0,2))]

        INSURANCE_TYPE = '000'
        INSURANCE_NAME = '零星报销'
        COMMIT_DATE = ''
        PAY_TIME = ''
        ADD_PAGE_NO = ''
        CENTER_NAME = rg_name
        CENTER_CODE = country_code
        AREA_CODE=''
        area_code = ['28', '30', '33', '34', '37', '39','31','43','35','38','36','40','41','42','32']
        if BUSSINESS_TYPE=='12':
            BILL_STATUS=''
            WORK_FLOW_STATE='1'
            BILL_DATE=''
            BILL_CREATE_TIME=''
            if  COUNTRY_CODE=='00':
                AREA_CODE= area_code[int(random.uniform(0,1))]
            elif  COUNTRY_CODE=='06':
                AREA_CODE= area_code[int(random.uniform(2,5))]
            elif COUNTRY_CODE=='01':
                AREA_CODE= area_code[int(random.uniform(6,6))]
            elif COUNTRY_CODE=='12':
                AREA_CODE= area_code[int(random.uniform(7,7))]
            elif COUNTRY_CODE=='14':
                AREA_CODE= area_code[int(random.uniform(8,8))]
            elif COUNTRY_CODE=='17':
                AREA_CODE= area_code[int(random.uniform(9,9))]
            elif COUNTRY_CODE=='10':
                AREA_CODE= area_code[int(random.uniform(10,10))]
            elif COUNTRY_CODE=='22':
                AREA_CODE= area_code[int(random.uniform(11,13))]
            else:
                AREA_CODE= area_code[int(random.uniform(14,14))]#虹口
        elif BUSSINESS_TYPE=='15' or BUSSINESS_TYPE=='16' :
            BILL_STATUS=''
            WORK_FLOW_STATE='1'
            BILL_DATE='201122'
            BILL_CREATE_TIME=otherStyleTime
        FAIL_TIMES = '0'
        EXCHANGE_PLAN_STATUS = ''
        EXCHANGE_PLAN_ID =  ''
        AUDIT_STATUS = '00'
        NEW_DATE = ''
        SEQ_NO = ''
        APPLY_NO = 'QX'+country_code + BUSSINESS_TYPE + otherStyleTime3 + str(n)
        # APPLY_NO = country_code + BUSSINESS_TYPE +'0717'+ str(n)
        # APPLY_NO = 'QX'+country_code + BUSSINESS_TYPE + str(int(time.time()))

        BILL_NO = APPLY_NO + APPLY_SUB_NO
        # 撤销凭证
        BILL_NO_cx = APPLY_NO + APPLY_SUB_NO_cx

        BILL_CREATE_NAME = ''
        BILL_CREATE_DATE = ''
        AUDITOR = ''
        AUDIT_DATE = ''


        # 明细表数据
        MESSAGE_TYPE1 = '2'
        SERAL_NO = ran_strx("0123456789", 13)
        # bill_no与主表保持一致
        BILL_NO1 = BILL_NO
        # 撤销
        BILL_NO1_cx = BILL_NO_cx
        PAY_TARGET = cl_pay_target[int(random.uniform(0, 7))]
        HOSPITAL_LV = cl_hospital_lv[int(random.uniform(0, 7))]
        MEDICAL_TYPE = cl_medical_type[int(random.uniform(0, 6))]
        if BUSSINESS_TYPE == '10':
            SETTLE_TYPE = '10801'
        elif BUSSINESS_TYPE == '04':
            SETTLE_TYPE = '70101'
        elif BUSSINESS_TYPE == '15':
            SETTLE_TYPE = '50001'
        elif BUSSINESS_TYPE == '16':
            SETTLE_TYPE = '52114'
        else:
            SETTLE_TYPE = BUSSINESS_TYPE

        CURRENT_YEAR_AMOUNT1 = CURRENT_YEAR_PAY
        ALL_YEAR_AMOUNT1 = ALL_YEAR_PAY
        PLAN_PAY1 = PLAN_PAY
        ADDITIONAL_PAY1 = ADDITIONAL_PAY
        OTHER_PAY1 = OTHER_PAY
        SELF_AMOUNT = round(random.uniform(100, 10), 2)
        REFUND_AMOUNT1 = REFUND_AMOUNT
        TOTAL_AMOUNT = round((SELF_AMOUNT + REFUND_AMOUNT1), 2)

        # 撤销凭证
        CURRENT_YEAR_AMOUNT1_cx = CURRENT_YEAR_PAY_cx
        ALL_YEAR_AMOUNT1_cx = ALL_YEAR_PAY_cx
        PLAN_PAY1_cx = PLAN_PAY_cx
        ADDITIONAL_PAY1_cx = ADDITIONAL_PAY_cx
        OTHER_PAY1_cx = OTHER_PAY_cx
        SELF_AMOUNT_cx = round(random.uniform(100, 10), 2)
        REFUND_AMOUNT1_cx = REFUND_AMOUNT_cx
        TOTAL_AMOUNT_cx = round((SELF_AMOUNT_cx + REFUND_AMOUNT1_cx), 2)

        HAND_WORK_DATE = ''
        CHANGE_DATE = ''
        BACKOUT_STATE = ''
        CONFIRM_VOU_DATE = ''
        CONFIRM_VOU_NO = ''
        CONFIRM_VOU_GUID = ''
        COMMIT_VOU_DATE = ''
        COMMIT_VOU_NO = ''
        COMMIT_VOU_GUID = ''
        PAY_VOU_DATE = ''
        PAY_VOU_NO = ''
        PAY_VOU_GUID = ''
        EXPORT_DATE = ''
        NOTE_TYPE = ''
        # FAIL_VOU_DATE = ''
        # FAIL_VOU_NO = ''
        # FAIL_VOU_GUID = ''
        IMPORT_DATE = ''


        line = str_head_zhu + '"' + ID + '", "' + CREATE_BY + '", ' + 'TO_TIMESTAMP(\'' + CREATE_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + LAST_MODIFIED_BY + '", TO_TIMESTAMP(\'' + LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), "' + \
               LAST_MODIFIED_VERSION + '", "' + MESSAGE_TYPE + '", "' + APPLY_NO + '", "' + APPLY_SUB_NO + '", "' + BILL_NO + '", "' + COMMON_ACCOUNT + '", "' + \
               APPLY_USER_NAME + '", "' + APPLY_USER_CARD_ID + '", "' + MEDICAL_CARD + '", "' + str(REFUND_AMOUNT) + '", "' + str(CURRENT_YEAR_PAY) + '", "' + str(ALL_YEAR_PAY) + '", "' + \
               str(PLAN_PAY) + '", "' + str(ADDITIONAL_PAY) + '", "' + str(OTHER_PAY) + '", "' + str(PAY_TYPE) + '", "' + MAIL_ADDRESS + '", "' + MAIL_ADDRESS_CODE + '", "' + BANK_TYPE + '", "' + \
               BANK_CODE + '", "' + BANK_CARD_ACCOUNT + '", "' + AGENT_USER_NAME + '", "' + UNIT_CODE + '", "' + UNIT_NAME + '", "' + ACCEPT_ACCOUNT_NAME + '", "' + \
               ACCEPT_ACCOUNT + '", "' + AEECPT_BANK_NAME + '", "' + BILL_CREATER + '", '+ 'TO_TIMESTAMP(\'' + BILL_CREATE_TIME + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'),"' +  BILL_CREATE_AREA + '", "' + VOUCHER_TYPE + '", "' + \
               VOUCHER_STATUS + '", "' + VOUVHER_CREATE_TIME + '", "' + BILL_STATUS + '", "' + RES1 + '", "' + RES2 + '", "' + RES3 + '", "' + RES4 + '", "' + COUNTRY_CODE + '", "' + \
               REFUND_CATEGORY + '", "' + ACCOUNT_STATE + '", "' + BILL_STATE + '", "' + BILL_DATE + '", "' + HANDWORK_FLAG + '", "' + NOTE_NUM + '", "' + FAIL_REASON + '", "' + \
               FUND_BATCH_NUM + '", "' + ORI_ACCEPT_ACCOUNT_NAME + '", "' + ORI_ACCEPT_ACCOUNT + '", "' + ORI_ACCEPT_BANK_NAME + '", "' + EXCHANGE_NUM + '", "' + \
               REFUND_STATE + '", "' + WORK_FLOW_STATE + '", "' + TASK_ID + '", "' + NODE_ID + '", "' + PROC_DEF_ID + '", "' + PROC_INST_ID + '", "' + CHANGE_STATUS + '", "' + \
               VOU_GUID + '", "' + VOU_NO + '", "' + RG_NAME + '", "' + SERVICE_NODE_NAME + '", "' + SERVICE_NODE_CODE + '", "' + BUSSINESS_TYPE + '", "' + INSURANCE_TYPE + '", "' + \
               INSURANCE_NAME + '", "' + COMMIT_DATE + '", "' + PAY_TIME + '", "' + ADD_PAGE_NO + '", "' + CENTER_NAME + '", "' + CENTER_CODE + '", "' + AREA_CODE + '", "' + \
               FAIL_TIMES + '", "' + EXCHANGE_PLAN_STATUS + '", "' + EXCHANGE_PLAN_ID + '", "' + AUDIT_STATUS + '", "' + NEW_DATE + '", "' + SEQ_NO +'", "'+HAND_WORK_DATE +'", "'+\
               CHANGE_DATE+'", "'+BACKOUT_STATE + '", "' + CONFIRM_VOU_DATE + '", "' + CONFIRM_VOU_NO + '", "' + CONFIRM_VOU_GUID + '", "' + COMMIT_VOU_DATE + '", "' + COMMIT_VOU_NO + '", "' + \
               COMMIT_VOU_GUID + '", "' + PAY_VOU_DATE + '", "' + PAY_VOU_NO + '", "' + PAY_VOU_GUID + '", "' + EXPORT_DATE + '", "' + NOTE_TYPE + '", "' + IMPORT_DATE + '", "' + BILL_CREATE_NAME + '", "' + BILL_CREATE_DATE + '", "' + AUDITOR + '", "' + AUDIT_DATE +'");'

        line_cx = str_head_zhu + '"' + ID + '1' + '", "' + CREATE_BY + '", ' + 'TO_TIMESTAMP(\'' + CREATE_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + LAST_MODIFIED_BY + '", TO_TIMESTAMP(\'' + LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), "' + \
               LAST_MODIFIED_VERSION + '", "' + MESSAGE_TYPE + '", "' + APPLY_NO + '", "' + APPLY_SUB_NO_cx + '", "' + BILL_NO_cx + '", "' + COMMON_ACCOUNT + '", "' + \
               APPLY_USER_NAME + '", "' + APPLY_USER_CARD_ID + '", "' + MEDICAL_CARD + '", "' + str(REFUND_AMOUNT_cx) + '", "' + str(CURRENT_YEAR_PAY_cx) + '", "' + str(ALL_YEAR_PAY_cx) + '", "' + \
               str(PLAN_PAY_cx) + '", "' + str(ADDITIONAL_PAY_cx) + '", "' + str(OTHER_PAY_cx) + '", "' + str(PAY_TYPE) + '", "' + MAIL_ADDRESS + '", "' + MAIL_ADDRESS_CODE + '", "' + BANK_TYPE + '", "' + \
               BANK_CODE + '", "' + BANK_CARD_ACCOUNT + '", "' + AGENT_USER_NAME + '", "' + UNIT_CODE + '", "' + UNIT_NAME + '", "' + ACCEPT_ACCOUNT_NAME + '", "' + \
               ACCEPT_ACCOUNT + '", "' + AEECPT_BANK_NAME + '", "' + BILL_CREATER + '", '+ 'TO_TIMESTAMP(\'' + BILL_CREATE_TIME + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'),"' +  BILL_CREATE_AREA + '", "' + VOUCHER_TYPE + '", "' + \
               VOUCHER_STATUS + '", "' + VOUVHER_CREATE_TIME + '", "' + BILL_STATUS + '", "' + RES1 + '", "' + RES2 + '", "' + RES3 + '", "' + RES4 + '", "' + COUNTRY_CODE + '", "' + \
               REFUND_CATEGORY + '", "' + ACCOUNT_STATE + '", "' + BILL_STATE + '", "' + BILL_DATE + '", "' + HANDWORK_FLAG + '", "' + NOTE_NUM + '", "' + FAIL_REASON + '", "' + \
               FUND_BATCH_NUM + '", "' + ORI_ACCEPT_ACCOUNT_NAME + '", "' + ORI_ACCEPT_ACCOUNT + '", "' + ORI_ACCEPT_BANK_NAME + '", "' + EXCHANGE_NUM + '", "' + \
               REFUND_STATE + '", "' + WORK_FLOW_STATE + '", "' + TASK_ID + '", "' + NODE_ID + '", "' + PROC_DEF_ID + '", "' + PROC_INST_ID + '", "' + CHANGE_STATUS + '", "' + \
               VOU_GUID + '", "' + VOU_NO + '", "' + RG_NAME + '", "' + SERVICE_NODE_NAME + '", "' + SERVICE_NODE_CODE + '", "' + BUSSINESS_TYPE + '", "' + INSURANCE_TYPE + '", "' + \
               INSURANCE_NAME + '", "' + COMMIT_DATE + '", "' + PAY_TIME + '", "' + ADD_PAGE_NO + '", "' + CENTER_NAME + '", "' + CENTER_CODE + '", "' + AREA_CODE + '", "' + \
               FAIL_TIMES + '", "' + EXCHANGE_PLAN_STATUS + '", "' + EXCHANGE_PLAN_ID + '", "' + AUDIT_STATUS + '", "' + NEW_DATE + '", "' + SEQ_NO +'", "'+HAND_WORK_DATE +'", "'+\
               CHANGE_DATE+'", "'+BACKOUT_STATE + '", "' + CONFIRM_VOU_DATE + '", "' + CONFIRM_VOU_NO + '", "' + CONFIRM_VOU_GUID + '", "' + COMMIT_VOU_DATE + '", "' + COMMIT_VOU_NO + '", "' + \
               COMMIT_VOU_GUID + '", "' + PAY_VOU_DATE + '", "' + PAY_VOU_NO + '", "' + PAY_VOU_GUID + '", "' + EXPORT_DATE + '", "' + NOTE_TYPE + '", "' + IMPORT_DATE + '", "' + BILL_CREATE_NAME + '", "' + BILL_CREATE_DATE + '", "' + AUDITOR + '", "' + AUDIT_DATE +'");'


        line1 = str_head_mingxi + '"' + ID +  '", "' + CREATE_BY + '", ' + 'TO_TIMESTAMP(\'' + CREATE_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'),' + ' "' + LAST_MODIFIED_BY + '"' + \
                ', TO_TIMESTAMP(\'' + LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + LAST_MODIFIED_VERSION + '", "' + MESSAGE_TYPE1 + '", "' + SERAL_NO + '", "' + \
                BILL_NO1 + '", "' + PAY_TARGET + '", "' + HOSPITAL_LV + '", "' + MEDICAL_TYPE + '", "' + SETTLE_TYPE + '", "' + \
                str(TOTAL_AMOUNT) + '", "' + str(SELF_AMOUNT) + '", "' + str(REFUND_AMOUNT1) + '", "' + str(CURRENT_YEAR_AMOUNT1) + '", "' + \
                str(ALL_YEAR_AMOUNT1) + '", "' + str(PLAN_PAY1) + '", "' + str(ADDITIONAL_PAY1) + '", "' + str(OTHER_PAY1) + '", "' + EXCHANGE_PLAN_ID + \
                '", "' + EXCHANGE_PLAN_STATUS + '");'

        line1_cx = str_head_mingxi + '"' + ID + '1' +  '", "' + CREATE_BY + '", ' + 'TO_TIMESTAMP(\'' + CREATE_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'),' + ' "' + LAST_MODIFIED_BY + '"' + \
                ', TO_TIMESTAMP(\'' + LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + LAST_MODIFIED_VERSION + '", "' + MESSAGE_TYPE1 + '", "' + SERAL_NO + '", "' + \
                BILL_NO1_cx + '", "' + PAY_TARGET + '", "' + HOSPITAL_LV + '", "' + MEDICAL_TYPE + '", "' + SETTLE_TYPE + '", "' + \
                str(TOTAL_AMOUNT_cx) + '", "' + str(SELF_AMOUNT_cx) + '", "' + str(REFUND_AMOUNT1_cx) + '", "' + str(CURRENT_YEAR_AMOUNT1_cx) + '", "' + \
                str(ALL_YEAR_AMOUNT1_cx) + '", "' + str(PLAN_PAY1_cx) + '", "' + str(ADDITIONAL_PAY1_cx) + '", "' + str(OTHER_PAY1_cx) + '", "' + EXCHANGE_PLAN_ID + \
                '", "' + EXCHANGE_PLAN_STATUS + '");'

        #AREA_CODE = '101'
        # CENTER_CODE = '黄浦区'
        SERVER_NODE_CODE = ''
        if BANK_TYPE == '00':
            ACCOUNT_NO=ran_strx("0123456789", 32)
            BANK_CODE1 = ran_strx("0123456789", 12)
        else:
            ACCOUNT_NO = BANK_CARD_ACCOUNT
            BANK_CODE1=BANK_CODE
        # BANK_CODE = '5042'
        ACCOUNT_NAME = APPLY_USER_NAME
        BANK_NODE_NAME = '昌平回龙观支行'
        IMPORT_DATE = otherStyleTime2
        USER_CARD_NO = APPLY_USER_CARD_ID
        BANK_NAME = '上海银行'
        EXCHANGE_PLAN_STATUS = ''
        EXCHANGE_PLAN_ID = ''
        RES1 = ''
        RES2 = ''
        USER_CARD_TYPE = '1'

        line2 = str_head_bankaccount + '"' + ID + '", "' + CREATE_BY + '", ' + 'TO_TIMESTAMP(\'' + CREATE_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'),' + ' "' + LAST_MODIFIED_BY + '"' + \
                ', TO_TIMESTAMP(\'' + LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + LAST_MODIFIED_VERSION + '", "' + AREA_CODE + '", "' + CENTER_CODE + '", "' + \
                SERVER_NODE_CODE + '", "' + ACCOUNT_NO + '", "' + BANK_CODE1 + '", "' + ACCOUNT_NAME + '", "' + BANK_NODE_NAME + '", "' + \
                IMPORT_DATE + '", "' + USER_CARD_NO + '", "' + BANK_NAME + '", "' + EXCHANGE_PLAN_STATUS + '", "' + EXCHANGE_PLAN_ID + '", "' + RES1 + '", "' + RES2 + '", "' + USER_CARD_TYPE + '");'

        line = line.replace('\"', '\'')
        line1 = line1.replace('\"', '\'')
        line_cx = line_cx.replace('\"', '\'')
        line1_cx = line1_cx.replace('\"', '\'')

        line2 = line2.replace('\"', '\'')
        no += 1
        n -= 1

        smcs_cash_file.write(line + '\n')
        smcs_cash_file.write(line1 + '\n')
        # 同步生成撤销凭证
        # smcs_cash_file.write(line_cx + '\n')
        # smcs_cash_file.write(line1_cx + '\n')

        # smcs_cash_file.write(line2 + '\n')
        if n%2 != 0:
            smcs_cash_file.write('commit;' + '\n')
    smcs_cash_file.write('commit;' + '\n')


if __name__ == '__main__':
    # 传参： country_code, rg_name, cl_bussniss_type, n
    # 现金结算
    # make_sql('17', '松江区医保中心', '01', 1)
    # 银行卡支付
    make_sql('17', '松江区医保中心', '02', 5)
    # 异地银行卡支付
    # make_sql('17', '松江区医保中心', '12', 2)
    # 税务隔日退费
    # make_sql('17', '松江区医保中心', '15', 1)
    # 单位集中
    # make_sql('17', '松江区医保中心', '04', 1)
    # 转移接续
    # make_sql('17', '松江区医保中心', '10', 1)
    # 邮汇
    # make_sql('17', '松江区医保中心', '03', 1)


