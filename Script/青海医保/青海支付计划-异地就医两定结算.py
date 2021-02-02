# -*- coding: utf-8 -*
import datetime


# import pandas as pd
import random
import string
import os



# 从字符串中随机取n个字符组成字符串
def ran_strx(strx, n):
    items = list(strx)
    str2 = ''
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


def make_sql(BUSINESS_TYPE_CODE, BUSINESS_TYPE_NAME, n):

    path = '../../Data_sql/基金支出/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'QH_SMRTS_PAY_PLAN_MI'+str(otherStyleTime3)+'.sql'
    smcs_cash_file = open(file_name, 'w', encoding='utf-8')

    # sql
    str_head_zhu = "insert into QH_SMRTS_PAY_PLAN_MI values ("
    str_head_item = "insert into QH_SMRTS_PAY_PLAN_DETAIL_MI values ("

    no = 1
    while (n > 0):
        field04 = ''
        field041 = '1'
        UNION_CODE = '630102'
        UNION_NAME = '城东区'
        BATCH_NO = 'QH' + ran_strx("0123456789", 5)
        YE_MONTH = '202101'
        INSURANCE_CODE = '310'
        INSURANCE_NAME = '城镇职工基本医疗保险'

        AGENCY_CODE = '630101'
        AGENCY_NAME = '西宁市医疗保障局本级'
        TOTAL_COUNT = ''
        TOTAL_AMOUNT = ran_strx("0123456789", 5)
        SUMMARY_TYPE = '1'  #汇总类型1-支付计划管理,2-统支,3-商保',
        status = ''  #状态
        rollback_reason = ''
        rollback_time = ''
        CWZS_TIME = ''
        CWZS_PEOPLE = ''
        ope_type = ''
        JZ_STATUS = ''
        vou_no = ''
        vou_status = ''
        vou_date = ''
        MEDICAL_CODE = '2200001'
        MEDICAL_NAME = '测试数据'
        DETAIL_UNIT_NO = 'QH' + otherStyleTime3 + str(n) + ran_strx("0123456789", 3)
        advance_amount = ''
        FIELD06 = ''
        SUMMARY = '摘要'
        CHARGE_AMOUNT = ''
        VOU_NO = ''
        JZ_STATUS= ''
        FAIL_REASON = ''
        BANK_DATA_STATUS = ''
        BANK_OFFER_TIME= ''
        DATA_DEAL_STAS = ''
        ISSUED_TO_TYPE = ''
        RECEIVE_BANK_USER_CODE = ''
        RECEIVE_BANK_USER_NAME = ''
        RECEIVE_BANK_CODE = ''
        RECEIVE_BANK_NAME = ''
        RECEIVE_BANK_BRANCK_CODE = '123456123456'
        RECEIVE_BANK_BRANCK_NAME = '工商银行青海支行'
        end_time = ''
        start_time = ''
        RECEIVE_UNIT_name = ''
        Settlement_count = ''
        user_account_surplus = ''
        MEDICAL_type = '1'

        line = str_head_zhu  +  '"' + field04 + '", "' + UNION_CODE + '", "' + UNION_NAME + '", "' + BATCH_NO + '", "' + YE_MONTH + '", "' + INSURANCE_CODE + '", "' + INSURANCE_NAME + '", "' + BUSINESS_TYPE_CODE + '", "' + BUSINESS_TYPE_NAME + '", "' + AGENCY_CODE + '" ,"' + AGENCY_NAME + '", "' + TOTAL_COUNT + '", "' + TOTAL_AMOUNT +'", "' + SUMMARY_TYPE +'", "' + status +'", "' + rollback_reason +'", "' + rollback_time +'", "' + CWZS_TIME +'", "' + CWZS_PEOPLE +'", "' + ope_type +'", "' + JZ_STATUS +'", "' + vou_no +'", "' + vou_status +'", "' + vou_date +'");'
        line_item = str_head_item  +  '"' + field041 + '", "' + BATCH_NO + '", "' + YE_MONTH + '", "' + INSURANCE_CODE + '",  "' + INSURANCE_NAME + '", "' + BUSINESS_TYPE_CODE + '", "' + BUSINESS_TYPE_NAME + '", "' + AGENCY_CODE + '", "' + AGENCY_NAME + '", "' + MEDICAL_CODE + '" , "' + MEDICAL_type + '" ,"' + MEDICAL_NAME + '", "' + TOTAL_AMOUNT +'", "' + status +'", "' + DETAIL_UNIT_NO +'", "' + rollback_reason +'", "' + user_account_surplus +'", "' + Settlement_count +'", "' + RECEIVE_UNIT_name +'", "' + start_time +'", "' + end_time +'", "' + RECEIVE_BANK_BRANCK_NAME +'", "' + RECEIVE_BANK_BRANCK_CODE +'", "' + RECEIVE_BANK_NAME +'", "' + RECEIVE_BANK_CODE +'", "' + RECEIVE_BANK_CODE +'", "' + RECEIVE_BANK_USER_NAME +'", "' + RECEIVE_BANK_USER_CODE +'", "' + rollback_time +'", "' + ISSUED_TO_TYPE +'", "' + DATA_DEAL_STAS +'", "' + BANK_OFFER_TIME +'", "' + BANK_DATA_STATUS +'", "' + FAIL_REASON +'", "' + VOU_NO +'", "' + CHARGE_AMOUNT +'", "' + FIELD06 +'", "' + SUMMARY +'", "' + advance_amount +'");'

        line = line.replace('\"', '\'')
        line_item = line_item.replace('\"', '\'')
        no += 1
        n -= 1

        smcs_cash_file.write(line + '\n')
        smcs_cash_file.write(line_item + '\n')


if __name__ == '__main__':
    # 传参： BUSINESS_TYPE_CODE, BUSINESS_TYPE_NAME, n
    make_sql('QHK10032', '青海支付计划-异地就医两定结算', 1)


