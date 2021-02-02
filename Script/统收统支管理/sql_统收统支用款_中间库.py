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
otherStyleTime4 = now.strftime("%Y%m%d%H%M")
otherStyleTime5 = now.strftime("%Y-%m")

def make_sql(a_agency_code, b_agency_code, c_agency_code, d_agency_code, e_agency_code, f_agency_code, g_agency_code, n, s):

    path = 'E:/医保产品/基金收入/统收统支SQL/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'SURP_COUNTY_FORM_APPLY_TEST'+str(otherStyleTime3)+'.sql'
    smcs_cash_file = open(file_name, 'w', encoding='utf-8')

    # 区县级sql
    str_head_zhu = "insert into SURP_COUNTY_FORM_APPLY_TEST values ("
    #省市级sql
    str_head_zhu1= "insert into SURP_COLLECTED_FORM_APPLY_TEST values("

    while (n > 0):
    #省市级
        a_ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        a_YEAR_MONTH = otherStyleTime5
        a_YEAR = '2020'
        a_MONTH = '08'
        a_QUARTER = '3'
        a_INSURANCE_CODE = '110'
        a_INSURANCE_NAME = '城镇企业职工基本养老保险'
        a_AGENCY_CODE = a_agency_code
        a_AGENCY_NAME = '河北省保险事业管理局'
        a_APPLY_PAY_MONEY = str(round(random.uniform(10000, 10), 2))
        a_REC_ACCOUNT_NO = '130100123456789001-001'
        a_REC_ACCOUNT_NAME = '河北省本级保险事业管理局支出户001-001'
        a_REC_BANK_NODE_NAME = '上海银行石家庄市支行1号'
        a_REC_BANK_NODE_SEQ = '130100123456'
        a_REC_BANK_TYPE_CODE = '313'
        a_REC_BANK_TYPE_NAME = '上海银行'
        a_REGION_CODE = '130000'
        a_REGION_NAME = '河北省'
        a_COLLECTED_FORM_NO = 'YK' + ran_strx('0123456789', 17)
        a_IF_COLLECTED = '1'
        a_CITY_OR_PROVINCE = 'P'
        a_OPERATE_STATE = '0'
        a_OPERATE_TIME = otherStyleTime
        a_OPERATOR_ID = 'hbzd1'
        a_CREATE_USER_NAME = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
        a_PARENT_COLLECTED_FORM_NO = ''
        a_BUSINESS_DATE = otherStyleTime2
        a_CHECK_STATUS = ''
        a_CHECK_AMOUNT = ''
        a_CHECK_DATE = ''
        a_CHECK_INFO = ''
        a_CHECK_PERSON = ''
        a_STATUS = '0'

        line_item3 = str_head_zhu1 + '"' + a_ID + '", "' + a_YEAR_MONTH + '", "' + a_YEAR + '", "' + a_MONTH + '", "' + a_QUARTER + '", "' + \
                     a_INSURANCE_CODE + '", "' + a_INSURANCE_NAME + '", "' + a_AGENCY_CODE + '", "' + a_AGENCY_NAME + '", "' + a_APPLY_PAY_MONEY + '", "' + \
                     a_REC_ACCOUNT_NO + '", "' + a_REC_ACCOUNT_NAME + '", "' + a_REC_BANK_NODE_NAME + '", "' + a_REC_BANK_NODE_SEQ + '", "' + \
                     a_REC_BANK_TYPE_CODE + '", "' + a_REC_BANK_TYPE_NAME + '", "' + a_REGION_CODE + '", "' + a_REGION_NAME + '", "' + \
                     a_COLLECTED_FORM_NO + '", "' + a_IF_COLLECTED + '", "' + a_CITY_OR_PROVINCE + '", "' + a_OPERATE_STATE + '", ' + 'TO_TIMESTAMP(\'' + a_OPERATE_TIME + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + a_OPERATOR_ID + '", "' + \
                     a_CREATE_USER_NAME + '", "' + a_PARENT_COLLECTED_FORM_NO + '", "' + a_CHECK_STATUS + '", "' + a_CHECK_AMOUNT + '", "' + \
                     a_CHECK_DATE + '", "' + a_CHECK_INFO + '", "' + a_CHECK_PERSON + '", "' + a_BUSINESS_DATE + '", "' +  a_STATUS + '");'

        line_item3 = line_item3.replace('\"', '\'')

        smcs_cash_file.write(line_item3 + '\n')




        m = s
        while (m > 0):
        # 市级制单
            b_ID = otherStyleTime3 + str(m) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
            b_YEAR_MONTH = otherStyleTime5
            b_YEAR = '2020'
            b_MONTH = '08'
            b_QUARTER = '3'
            b_INSURANCE_CODE = '110'
            b_INSURANCE_NAME = '城镇企业职工基本养老保险'
            b_AGENCY_CODE = b_agency_code
            b_AGENCY_NAME = '石家庄市本级保险事业管理局'
            if m == 1:
                b_AGENCY_CODE = e_agency_code
                b_AGENCY_NAME = '唐山市本级保险事业管理局'
            b_APPLY_PAY_MONEY = str(round(random.uniform(10000, 10), 2))
            b_REC_ACCOUNT_NO = '130100123456789001-001'
            b_REC_ACCOUNT_NAME = '石家庄市本级保险事业管理局支出户001-001'
            b_REC_BANK_NODE_NAME = '上海银行石家庄市支行1号'
            b_REC_BANK_NODE_SEQ = '130100123456'
            b_REC_BANK_TYPE_CODE = '313'
            b_REC_BANK_TYPE_NAME = '上海银行'
            b_REGION_CODE = '130000'
            b_REGION_NAME = '河北省'
            b_COLLECTED_FORM_NO = 'YK' + ran_strx('0123456789', 17)
            b_IF_COLLECTED = '1'
            b_CITY_OR_PROVINCE = 'C'
            b_OPERATE_STATE = '0'
            b_OPERATE_TIME = otherStyleTime
            b_OPERATOR_ID = 'sjzzd1'
            if m == 1:
                b_OPERATOR_ID = 'tszd1'
            b_CREATE_USER_NAME = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
            b_PARENT_COLLECTED_FORM_NO = a_COLLECTED_FORM_NO
            b_BUSINESS_DATE = otherStyleTime2
            b_CHECK_STATUS = ''
            b_CHECK_AMOUNT = ''
            b_CHECK_DATE = ''
            b_CHECK_INFO = ''
            b_CHECK_PERSON = ''
            b_STATUS = '0'

            line_item4 = str_head_zhu1 + '"' + b_ID + '", "' + b_YEAR_MONTH + '", "' + b_YEAR + '", "' + b_MONTH + '", "' + b_QUARTER + '", "' + \
                b_INSURANCE_CODE + '", "' + b_INSURANCE_NAME + '", "' + b_AGENCY_CODE + '", "' + b_AGENCY_NAME + '", "' + b_APPLY_PAY_MONEY + '", "' + \
                b_REC_ACCOUNT_NO + '", "' + b_REC_ACCOUNT_NAME + '", "' + b_REC_BANK_NODE_NAME + '", "' + b_REC_BANK_NODE_SEQ + '", "' + \
                b_REC_BANK_TYPE_CODE + '", "' + b_REC_BANK_TYPE_NAME + '", "' + b_REGION_CODE + '", "' + b_REGION_NAME + '", "' + \
                b_COLLECTED_FORM_NO + '", "' + b_IF_COLLECTED + '", "' + b_CITY_OR_PROVINCE + '", "' + b_OPERATE_STATE + '", ' + 'TO_TIMESTAMP(\'' + b_OPERATE_TIME + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + b_OPERATOR_ID + '", "' + \
                b_CREATE_USER_NAME + '", "' + b_PARENT_COLLECTED_FORM_NO + '", "' + b_CHECK_STATUS + '", "' + b_CHECK_AMOUNT + '", "' + \
                b_CHECK_DATE + '", "' + b_CHECK_INFO + '", "' + b_CHECK_PERSON + '", "' + b_BUSINESS_DATE + '", "' + b_STATUS + '");'
            line_item4 = line_item4.replace('\"', '\'')

            smcs_cash_file.write(line_item4 + '\n')



            # 区县级第一条
            ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
            YEAR_MONTH = otherStyleTime5
            YEAR = '2020'
            MONTH = '08'
            QUARTER = '3'
            INSURANCE_CODE = '110'
            INSURANCE_NAME = '城镇企业职工基本养老保险'
            AGENCY_CODE = c_agency_code
            AGENCY_NAME = '长安区保险事业管理局'
            if m == 1:
                AGENCY_CODE = f_agency_code
                AGENCY_NAME = '路南区保险事业管理局'
            APPLY_PAY_MONEY = str(round(random.uniform(10000, 10), 2))
            REC_ACCOUNT_NO = '130100123456789001-001'
            REC_ACCOUNT_NAME = '石家庄市本级保险事业管理局支出户001-001'
            REC_BANK_NODE_NAME = '上海银行石家庄市支行1号'
            REC_BANK_NODE_SEQ = '130100123456'
            REC_BANK_TYPE_CODE = '313'
            REC_BANK_TYPE_NAME = '上海银行'
            REGION_CODE = '130000'
            REGION_NAME = '河北省'
            APPLY_FORM_NO = 'YK' + ran_strx('0123456789', 17)
            IF_COLLECTED = '1'
            OPERATE_STATE = '0'
            OPERATE_TIME = otherStyleTime
            OPERATOR_ID = 'cazd1'
            if m == 1:
                OPERATOR_ID = 'lnzd1'
            CREATE_USER_NAME = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
            PARENT_COLLECTED_FORM_NO = b_COLLECTED_FORM_NO
            CHECK_STATUS = ''
            CHECK_AMOUNT = ''
            CHECK_DATE = ''
            CHECK_INFO = ''
            CHECK_PERSON = ''
            BUSINESS_DATE = otherStyleTime2
            PURPOSE = '测试-数据接入'
            APPLY_TIME = otherStyleTime
            STATUS = '0'

            # 区县级第二条

            t_ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
            t_YEAR_MONTH = otherStyleTime5
            t_YEAR = '2020'
            t_MONTH = '08'
            t_QUARTER = '3'
            t_INSURANCE_CODE = '110'
            t_INSURANCE_NAME = '城镇企业职工基本养老保险'
            t_AGENCY_CODE = d_agency_code
            t_AGENCY_NAME = '桥东区保险事业管理局'
            if m == 1:
                t_AGENCY_CODE = g_agency_code
                t_AGENCY_NAME = '路北区保险事业管理局'
            t_APPLY_PAY_MONEY = str(round(random.uniform(10000, 10), 2))
            t_REC_ACCOUNT_NO = '130100123456789001-001'
            t_REC_ACCOUNT_NAME = '石家庄市本级保险事业管理局支出户001-001'
            t_REC_BANK_NODE_NAME = '上海银行石家庄市支行1号'
            t_REC_BANK_NODE_SEQ = '130100123456'
            t_REC_BANK_TYPE_CODE = '313'
            t_REC_BANK_TYPE_NAME = '上海银行'
            t_REGION_CODE = '130000'
            t_REGION_NAME = '河北省'
            t_APPLY_FORM_NO = 'YK' + ran_strx('0123456789', 17)
            t_IF_COLLECTED = '1'
            t_OPERATE_STATE = '0'
            t_OPERATE_TIME = otherStyleTime
            t_OPERATOR_ID = 'qdzd1'
            if m == 1:
                t_OPERATOR_ID = 'lbzd1'

            t_CREATE_USER_NAME = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
            t_PARENT_COLLECTED_FORM_NO = b_COLLECTED_FORM_NO
            t_CHECK_STATUS = ''
            t_CHECK_AMOUNT = ''
            t_CHECK_DATE = ''
            t_CHECK_INFO = ''
            t_CHECK_PERSON = ''
            t_BUSINESS_DATE = otherStyleTime2
            t_PURPOSE = '测试-数据接入'
            t_APPLY_TIME = otherStyleTime
            t_STATUS = '0'

            line_item1 = str_head_zhu + '"' + ID + '", "' + YEAR_MONTH + '", "' + YEAR + '", "' + MONTH + '", "' + QUARTER + '", "' + \
                INSURANCE_CODE + '", "' + INSURANCE_NAME + '", "' + AGENCY_CODE + '", "' + AGENCY_NAME + '", "' + APPLY_PAY_MONEY + '", "' + \
                REC_ACCOUNT_NO + '", "' + REC_ACCOUNT_NAME + '", "' + REC_BANK_NODE_NAME + '", "' + REC_BANK_NODE_SEQ + '", "' + \
                REC_BANK_TYPE_CODE + '", "' + REC_BANK_TYPE_NAME + '", "' + REGION_CODE + '", "' + REGION_NAME + '", "' + \
                APPLY_FORM_NO + '", "' + IF_COLLECTED + '", "' + OPERATE_STATE + '", ' + 'TO_TIMESTAMP(\'' + OPERATE_TIME + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + OPERATOR_ID + '", "' + \
                CREATE_USER_NAME + '", "' + PARENT_COLLECTED_FORM_NO + '", "' + CHECK_STATUS + '", "' + CHECK_AMOUNT + '", "' + \
                CHECK_DATE + '", "' + CHECK_INFO + '", "' + CHECK_PERSON + '", "' + BUSINESS_DATE + '", "' + PURPOSE + '", ' + 'TO_TIMESTAMP(\'' + APPLY_TIME + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + STATUS + '");'

            line_item2 = str_head_zhu + '"' + t_ID + '", "' + t_YEAR_MONTH + '", "' + t_YEAR + '", "' + t_MONTH + '", "' + t_QUARTER + '", "' + \
                t_INSURANCE_CODE + '", "' + t_INSURANCE_NAME + '", "' + t_AGENCY_CODE + '", "' + t_AGENCY_NAME + '", "' + t_APPLY_PAY_MONEY + '", "' + \
                t_REC_ACCOUNT_NO + '", "' + t_REC_ACCOUNT_NAME + '", "' + t_REC_BANK_NODE_NAME + '", "' + t_REC_BANK_NODE_SEQ + '", "' + \
                t_REC_BANK_TYPE_CODE + '", "' + t_REC_BANK_TYPE_NAME + '", "' + t_REGION_CODE + '", "' + t_REGION_NAME + '", "' + \
                t_APPLY_FORM_NO + '", "' + t_IF_COLLECTED + '", "' + t_OPERATE_STATE + '", ' + 'TO_TIMESTAMP(\'' + t_OPERATE_TIME + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + t_OPERATOR_ID + '", "' + \
                t_CREATE_USER_NAME + '", "' + t_PARENT_COLLECTED_FORM_NO + '", "' + t_CHECK_STATUS + '", "' + t_CHECK_AMOUNT + '", "' + \
                t_CHECK_DATE + '", "' + t_CHECK_INFO + '", "' + t_CHECK_PERSON + '", "' + t_BUSINESS_DATE + '", "' + t_PURPOSE + '", ' + 'TO_TIMESTAMP(\'' + t_APPLY_TIME + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), ' + '"' + t_STATUS + '");'

            line_item1 = line_item1.replace('\"', '\'')
            line_item2 = line_item2.replace('\"', '\'')
            m -= 1
            smcs_cash_file.write(line_item1 + '\n')
            smcs_cash_file.write(line_item2 + '\n')
        n -= 1


if __name__ == '__main__':
    # 传参： agency_code, n（有几组，每组7条）,s(1省对2市)
    # 河北省，石家庄市，长安区，桥东区，唐山市，路南区，路北区
    make_sql('1300', '130100', '130102', '130103', '130201', '130202', '130203', 1, 2)


