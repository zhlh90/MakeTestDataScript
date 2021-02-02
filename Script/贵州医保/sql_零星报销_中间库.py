# -*- coding: utf-8 -*
import datetime

# import pandas as pd
import random
from Script import shenfenzhenghao
import os


# 经办机构
cl_agency_code = ['00','01','1300','520201']
cl_agency_name = ['上海保险事业管理局','黄浦区保险事业管理局','河北省','六盘水市本级']

# 险种
cl_ins_code = ['310','390']
cl_ins_name = ['城镇职工基本医疗保险','城乡居民基本医疗保险']

# 业务类型
cl_BUSINESS_TYPE = ['K1002401', 'K1002402']
# 统筹区
cl_country_code = ['00','00','130000','520200']
cl_country_name = ['上海市统筹','上海市统筹','河北省统筹','六盘水市']

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
otherStyleTime5 = now.strftime("%Y%m")

def make_sql(agency_no,ins_no, n):

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
    str_head_zhu = "insert into mid.MID_CASH values ("
    str_head_item = "insert into mid.MID_CASH_ITEM values ("

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
        AREA_CODE = cl_country_code[agency_no]
        AREA_NAME = cl_country_name[agency_no]
        CENTER_CODE = cl_agency_code[agency_no]
        CENTER_NAME = cl_agency_name[agency_no]
        PAY_PERIOD = otherStyleTime5
        # 现金-1  银行卡-0
        num = int(random.uniform(0, 2))
        # num = 0
        BUSINESS_TYPE = cl_BUSINESS_TYPE[num]
        PAY_TYPE = cl_PAY_TYPE[num]

        STATUS = '0'
        INSURANCE_CODE = cl_ins_code[ins_no]
        INSURANCE_NAME = cl_ins_name[ins_no]
        # PAY_STATUS = '0'

        # 子表
        # aa = ''
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

        # line = str_head_zhu + '"' + BILL_NO + '", "' + BATCH_NO + '", "' + APPLY_USER_NAME + '", "' + APPLY_USER_CARD_ID\
        #        + '", "' + REFUND_AMOUNT + '", "' + MEDICAL_CARD + '", "' + BANK_CODE + '", "' + BANK_TYPE + '", "' + \
        #        BANK_ACCOUNT_NAME + '", "' + BANK_CARD_ACCOUNT + '", "' + AREA_CODE + '", "' + AREA_NAME + '", "' + \
        #        CENTER_CODE + '", "' + CENTER_NAME + '", "' + PAY_PERIOD + '", "' + BUSINESS_TYPE + '", "' + PAY_TYPE\
        #        + '", "' + STATUS + '", "' + INSURANCE_CODE + '", "' + INSURANCE_NAME + '", "' + PAY_STATUS + '");'

        # line_item1 = str_head_item + '"' + aa + '", "' + BATCH_NO_1 + '", "' + BILL_NO_1 + '", "' + TOTAL_AMOUNT_1 + '", "' + SETTLE_TYPE_1 + '", "' + SELF_AMOUNT_1 + '", "' + REFUND_AMOUNT_1 + '", "' + MEDICAL_TYPE_1 + '", "' + PAY_TARGET_1 + '", "' + HOSPITAL_LV_1 + '", "' + SETTLE_TYPE_NAME_1 + '");'
        # line_item2 = str_head_item + '"' + bb + '", "' + BATCH_NO_2 + '", "' + BILL_NO_2 + '", "' + TOTAL_AMOUNT_2 + '", "' + SETTLE_TYPE_2 + '", "' + SELF_AMOUNT_2 + '", "' + REFUND_AMOUNT_2 + '", "' + MEDICAL_TYPE_2 + '", "' + PAY_TARGET_2 + '", "' + HOSPITAL_LV_2 + '", "' + SETTLE_TYPE_NAME_2 + '");'
        line = str_head_zhu + '"' + BILL_NO + '", "' + BATCH_NO + '", "' + APPLY_USER_NAME + '", "' + APPLY_USER_CARD_ID\
               + '", "' + REFUND_AMOUNT + '", "' + MEDICAL_CARD + '", "' + BANK_CODE + '", "' + BANK_TYPE + '", "' + \
               BANK_ACCOUNT_NAME + '", "' + BANK_CARD_ACCOUNT + '", "' + AREA_CODE + '", "' + AREA_NAME + '", "' + \
               CENTER_CODE + '", "' + CENTER_NAME + '", "' + PAY_PERIOD + '", "' + BUSINESS_TYPE + '", "' + PAY_TYPE\
               + '", "' + STATUS + '", "' + INSURANCE_CODE + '", "' + INSURANCE_NAME + '");'

        line_item1 = str_head_item + '"' + BATCH_NO_1 + '", "' + BILL_NO_1 + '", "' + TOTAL_AMOUNT_1 + '", "' + SETTLE_TYPE_1 + '", "' + SELF_AMOUNT_1 + '", "' + REFUND_AMOUNT_1 + '", "' + MEDICAL_TYPE_1 + '", "' + PAY_TARGET_1 + '", "' + HOSPITAL_LV_1 + '", "' + SETTLE_TYPE_NAME_1 + '");'
        line_item2 = str_head_item + '"' + BATCH_NO_2 + '", "' + BILL_NO_2 + '", "' + TOTAL_AMOUNT_2 + '", "' + SETTLE_TYPE_2 + '", "' + SELF_AMOUNT_2 + '", "' + REFUND_AMOUNT_2 + '", "' + MEDICAL_TYPE_2 + '", "' + PAY_TARGET_2 + '", "' + HOSPITAL_LV_2 + '", "' + SETTLE_TYPE_NAME_2 + '");'


        line = line.replace('\"', '\'')
        line_item1 = line_item1.replace('\"', '\'')
        line_item2 = line_item2.replace('\"', '\'')
        no += 1
        n -= 1

        SMCS_CASH_file.write(line + '\n')
        SMCS_CASH_file.write(line_item1 + '\n')
        SMCS_CASH_file.write(line_item2 + '\n')



if __name__ == '__main__':
    # 第一参数：0-上海 1-黄埔，2-河北省，3-六盘水市本级
    # 第二参数：0-310 1-390
    # 第三参数：数据条数
    make_sql(3,0,10)


