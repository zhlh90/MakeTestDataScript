# -*- coding: utf-8 -*
import datetime

# import pandas as pd
import random
from Script import shenfenzhenghao
import os

# 业务类型
cl_BUSINESS_TYPE = ['K1002401', 'K1002402']
cl_PAY_TYPE = ['2', '1']

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

    path = '../../Data_sql/零星报销/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'MID_CASH'+str(otherStyleTime3)+'.sql'
    # file_name_item = path + 'MID_PAY_PLAN_ITEM'+str(otherStyleTime3)+'.sql'
    SMCS_CASH_file = open(file_name, 'w', encoding='utf-8')
    # SMRTS_PAY_PLAN_ITEM_file = open(file_name_item, 'w', encoding='utf-8')

    # 主子表sql
    str_head_zhu = "insert into MID_CASH values ("
    str_head_item = "insert into MID_CASH_ITEM values ("

    no = 1
    while (n > 0):
        # 主表
        BILL_NO = otherStyleTime4 + str(n)
        BATCH_NO = 'YW' + otherStyleTime4 + str(n)
        APPLY_USER_NAME = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
        APPLY_USER_CARD_ID = shenfenzhenghao.outIDcard()
        REFUND_AMOUNT = '100.00'
        MEDICAL_CARD = ran_strx("0123456789", 10)
        BANK_CODE = '001'
        BANK_TYPE = '001'
        BANK_ACCOUNT_NAME = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        BANK_CARD_ACCOUNT = ran_strx("0123456789", 16)
        AREA_CODE = '310000'
        AREA_NAME = '上海市'
        CENTER_CODE = '00'
        CENTER_NAME = '上海市社会保险管理局'
        PAY_PERIOD = '202008'
        # 现金-1  银行卡-0
        num = int(random.uniform(0, 2))
        # num = 0
        BUSINESS_TYPE = cl_BUSINESS_TYPE[num]
        PAY_TYPE = cl_PAY_TYPE[num]

        STATUS = '0'
        INSURANCE_CODE = '110'
        INSURANCE_NAME = '城镇职工基本医疗保险'
        PAY_STATUS = '0'

        # 子表
        aa = ''
        BATCH_NO_1 = BATCH_NO
        BILL_NO_1 = BILL_NO
        TOTAL_AMOUNT_1 = '110'
        SETTLE_TYPE_1 = '1'
        SELF_AMOUNT_1 = '160'
        REFUND_AMOUNT_1 = '156'
        MEDICAL_TYPE_1 = '2'
        PAY_TARGET_1 = '2'
        HOSPITAL_LV_1 = '2'
        SETTLE_TYPE_NAME_1 = '费款项001'

        bb = ''
        BATCH_NO_2 = BATCH_NO
        BILL_NO_2 = BILL_NO
        TOTAL_AMOUNT_2 = '115'
        SETTLE_TYPE_2 = '2'
        SELF_AMOUNT_2 = '410'
        REFUND_AMOUNT_2 = '137'
        MEDICAL_TYPE_2 = '2'
        PAY_TARGET_2 = '2'
        HOSPITAL_LV_2 = '2'
        SETTLE_TYPE_NAME_2 = '费款项002'

        line = str_head_zhu + '"' + BILL_NO + '", "' + BATCH_NO + '", "' + APPLY_USER_NAME + '", "' + APPLY_USER_CARD_ID\
               + '", "' + REFUND_AMOUNT + '", "' + MEDICAL_CARD + '", "' + BANK_CODE + '", "' + BANK_TYPE + '", "' + \
               BANK_ACCOUNT_NAME + '", "' + BANK_CARD_ACCOUNT + '", "' + AREA_CODE + '", "' + AREA_NAME + '", "' + \
               CENTER_CODE + '", "' + CENTER_NAME + '", "' + PAY_PERIOD + '", "' + BUSINESS_TYPE + '", "' + PAY_TYPE\
               + '", "' + STATUS + '", "' + INSURANCE_CODE + '", "' + INSURANCE_NAME + '", "' + PAY_STATUS + '");'

        line_item1 = str_head_item + '"' + aa + '", "' + BATCH_NO_1 + '", "' + BILL_NO_1 + '", "' + TOTAL_AMOUNT_1 + '", "' + SETTLE_TYPE_1 + '", "' + SELF_AMOUNT_1 + '", "' + REFUND_AMOUNT_1 + '", "' + MEDICAL_TYPE_1 + '", "' + PAY_TARGET_1 + '", "' + HOSPITAL_LV_1 + '", "' + SETTLE_TYPE_NAME_1 + '");'
        line_item2 = str_head_item + '"' + bb + '", "' + BATCH_NO_2 + '", "' + BILL_NO_2 + '", "' + TOTAL_AMOUNT_2 + '", "' + SETTLE_TYPE_2 + '", "' + SELF_AMOUNT_2 + '", "' + REFUND_AMOUNT_2 + '", "' + MEDICAL_TYPE_2 + '", "' + PAY_TARGET_2 + '", "' + HOSPITAL_LV_2 + '", "' + SETTLE_TYPE_NAME_2 + '");'

        line = line.replace('\"', '\'')
        line_item1 = line_item1.replace('\"', '\'')
        line_item2 = line_item2.replace('\"', '\'')
        no += 1
        n -= 1

        SMCS_CASH_file.write(line + '\n')
        SMCS_CASH_file.write(line_item1 + '\n')
        SMCS_CASH_file.write(line_item2 + '\n')



if __name__ == '__main__':
    # 传参： country_code, n
    make_sql('00', 20000)


