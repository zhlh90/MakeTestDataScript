# -*- coding: utf-8 -*
import datetime
# import cx_Oracle
import pymysql
import random
import string

# 统筹区
from Script import shenfenzhenghao

cl_country_code = ['00','130000','34000001','630101','630101']
cl_country_name = ['上海市统筹','河北省统筹','安徽省统筹','西宁市医疗保障局本级','西宁市医疗保障局本级']
# 经办机构
cl_agency_code = ['00','130002','34000001','630101','630102']
# cl_agency_name = ['上海保险事业管理局','河北省','西宁市医疗保障局本级']
cl_agency_name = ['','河北省','安徽省事业保险局','西宁市医疗保障局本级','西宁市城东区医疗保障局']
# 行政区划
cl_org_code = ['310000','130000','34000001','630101','630102']
cl_org_name = ['上海市','河北省','安徽省','西宁市','西宁市城东区']
# 业务类型
cl_bussnisstype_code = ['QHK10025','QHK10026','QHK10027','QHK10028','QHK10029','QHK10030','QHK10031','QHK9903','QHK9902','QHK10032','QHK10033']
cl_bussnisstype_name = ['青海支付计划两定结算','青海支付计划医院预付','青海支付计划转移支出','青海支付计划生育津贴支出','青海支付计划零星报销','青海支付计划征缴退费','青海支付计划个账结算','测试青海支付计划主子孙','测试青海支付计划主子','异地就医两定结算','异地就医拨款']

# 险种
cl_ins_code = ['310','320','330','390']
cl_ins_name = ['城镇职工基本医疗保险','公务员医疗补助','大额医疗费用补助','城乡居民基本医疗保险']

# 青海-医疗类别
cl_QH_MEDICAL_CATEGORY=['11','12','13','14','21','22','23','24','41','51','52','53']
# 青海-人员类别
cl_QH_PERSONNEL_CATEGORY=['11','12','13','14','15','16','17','18','20']

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
otherStyleTime5 = now.strftime("%Y-%m")
otherStyleTime6 = now.strftime("%Y%m")

def make_sql(country_code,bus_no,summary_type,ins_no,n):

    starttime = datetime.datetime.now()
    # 建立数据库连接
    db = pymysql.Connect(
        host='10.10.66.158',##mysql服务器地址
        port=3306,##mysql服务器端口号
        user='rsyb',##用户名
        passwd='1',##密码
        db='sifcmiddledb',##数据库名
        charset='utf8'##连接编码
    )
    #创建游标
    cr = db.cursor()

    no = 1
    while (n > 0):
        # 主表
        UNION_CODE = cl_country_code[country_code]
        UNION_NAME = cl_country_name[country_code]
        BATCH_NO = 'QH' + otherStyleTime3 + str(n)
        YE_MONTH = otherStyleTime6
        INSURANCE_CODE = cl_ins_code[ins_no]
        INSURANCE_NAME = cl_ins_name[ins_no]
        BUSINESS_TYPE_CODE = cl_bussnisstype_code[bus_no]
        BUSINESS_TYPE_NAME = cl_bussnisstype_name[bus_no]
        AGENCY_CODE = cl_agency_code[country_code]
        AGENCY_NAME = cl_agency_name[country_code]
        TOTAL_AMOUNT = '3333.33'
        TOTAL_COUNT = '2'
        # 1-支付计划  2-统支结算单
        SUMMARY_TYPE = summary_type
        STATUS = '0'
        ROLLBACK_REASON = ''
        ROLLBACK_TIME = datetime.datetime.fromisoformat('1900-01-01 00:00:00').strftime("%Y-%m-%d %H:%M:%S")
        FIELD04 = '1'

        # 是否主子孙 0-是 1-否
        if (BUSINESS_TYPE_CODE == 'QHK10025' or BUSINESS_TYPE_CODE == 'QHK10029' or BUSINESS_TYPE_CODE == 'QHK9903'):
            FIELD04 = '0'
        #领导人终审时间
        CWZS_TIME = datetime.datetime.fromisoformat('1900-01-01 00:00:00').strftime("%Y-%m-%d %H:%M:%S")
        #领导终审人
        CWZS_PEOPLE = ''
        #预付金操作类型
        OPE_TYPE = ''
        JZ_STATUS = ''
        VOU_NO = ''
        VOU_STATUS = ''
        VOU_DATE = ''
        DATA_DEAL_STAS = '101'

        sqlG = "insert into qh_smrts_pay_plan_mi values (%(DATA_DEAL_STAS)s, %(FIELD04)s, %(UNION_CODE)s, %(UNION_NAME)s, %(BATCH_NO)s, %(YE_MONTH)s, %(INSURANCE_CODE)s, %(INSURANCE_NAME)s, %(BUSINESS_TYPE_CODE)s, %(BUSINESS_TYPE_NAME)s, %(AGENCY_CODE)s, %(AGENCY_NAME)s, %(TOTAL_COUNT)s, %(TOTAL_AMOUNT)s, %(SUMMARY_TYPE)s, %(STATUS)s, %(ROLLBACK_REASON)s, %(ROLLBACK_TIME)s, %(CWZS_TIME)s, %(CWZS_PEOPLE)s, %(OPE_TYPE)s, %(JZ_STATUS)s, %(VOU_NO)s, %(VOU_STATUS)s, %(VOU_DATE)s)"
        value = {
        "UNION_CODE":UNION_CODE,
        "UNION_NAME":UNION_NAME,
        "BATCH_NO":BATCH_NO,
        "YE_MONTH":YE_MONTH,
        "INSURANCE_CODE":INSURANCE_CODE,
        "INSURANCE_NAME":INSURANCE_NAME,
        "BUSINESS_TYPE_CODE":BUSINESS_TYPE_CODE,
        "BUSINESS_TYPE_NAME":BUSINESS_TYPE_NAME,
        "AGENCY_CODE":AGENCY_CODE,
        "AGENCY_NAME":AGENCY_NAME,
        "TOTAL_COUNT":TOTAL_COUNT,
        "TOTAL_AMOUNT":TOTAL_AMOUNT,
        "SUMMARY_TYPE":SUMMARY_TYPE,
        "STATUS":STATUS,
        "ROLLBACK_REASON":ROLLBACK_REASON,
        "ROLLBACK_TIME":ROLLBACK_TIME,
        "FIELD04":FIELD04,
        "CWZS_TIME":CWZS_TIME,
        "CWZS_PEOPLE":CWZS_PEOPLE,
        "OPE_TYPE":OPE_TYPE,
        "JZ_STATUS":JZ_STATUS,
        "VOU_NO":VOU_NO,
        "VOU_STATUS":VOU_STATUS,
        "VOU_DATE":VOU_DATE,
        "DATA_DEAL_STAS":DATA_DEAL_STAS
        }
        cr.execute(sqlG, value)

        #子表
        BATCH_NO = BATCH_NO
        YE_MONTH = otherStyleTime6
        INSURANCE_CODE = cl_ins_code[ins_no]
        INSURANCE_NAME = cl_ins_name[ins_no]
        BUSINESS_TYPE_CODE = cl_bussnisstype_code[bus_no]
        BUSINESS_TYPE_NAME = cl_bussnisstype_name[bus_no]
        AGENCY_CODE = cl_agency_code[country_code]
        AGENCY_NAME = cl_agency_name[country_code]

        # 往来单位1
        MEDICAL_CODE_1 = shenfenzhenghao.outIDcard()
        MEDICAL_TYPE_1 = '1'  # 1-医院 2-药店
        MEDICAL_NAME_1 = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
        TOTAL_AMOUNT_1 = '1111.11'
        # 往来单位2
        MEDICAL_CODE_2 = shenfenzhenghao.outIDcard()
        MEDICAL_TYPE_2 = '2'
        MEDICAL_NAME_2 = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        TOTAL_AMOUNT_2 = '2222.22'

        if (BUSINESS_TYPE_CODE == 'QHK10025' or BUSINESS_TYPE_CODE == 'QHK10029' or BUSINESS_TYPE_CODE == 'QHK9903' or BUSINESS_TYPE_CODE == 'QHK10033'):
            # 往来单位1
            MEDICAL_CODE_1 = '2200001'
            MEDICAL_TYPE_1 = '1'  # 1-医院 2-药店
            # MEDICAL_NAME_1 = '上海市支付计划往来单位001'
            MEDICAL_NAME_1 = ''
            TOTAL_AMOUNT_1 = '1111.11'
            # 往来单位2
            MEDICAL_CODE_2 = '2200002'
            MEDICAL_TYPE_2 = '2'
            MEDICAL_NAME_2 = '上海市支付计划往来单位002'
            TOTAL_AMOUNT_2 = '2222.22'

        STATUS = '0'

        DETAIL_UNIT_NO_1 = 'QHZS1' + otherStyleTime3 + str(n)
        DETAIL_UNIT_NO_2 = 'QHZS2' + otherStyleTime3 + str(n)

        ROLLBACK_REASON = ''
        USER_ACCOUNT_SURPLUS = ''
        SETTLEMENT_COUNT = ''
        RECEIVE_UNIT_NAME = '上海市支付计划往来单位001收款'
        RECEIVE_UNIT_NAME_2 = '上海市支付计划往来单位002收款'
        START_TIME = datetime.datetime.fromisoformat('1900-01-01 00:00:00').strftime("%Y-%m-%d %H:%M:%S")
        END_TIME = datetime.datetime.fromisoformat('1900-01-01 00:00:00').strftime("%Y-%m-%d %H:%M:%S")
        # 收款方网点信息
        RECEIVE_BANK_BRANCK_NAME = '工商银行青海支行'
        RECEIVE_BANK_BRANCK_CODE = '123456123456'
        # 收款方银行信息
        RECEIVE_BANK_NAME = ''
        RECEIVE_BANK_CODE = '102'
        # 收款方账户信息
        # RECEIVE_BANK_USER_NAME = '上海市支付计划往来单位001'
        # RECEIVE_BANK_USER_CODE = '656789987678001'
        RECEIVE_BANK_USER_NAME = ''
        RECEIVE_BANK_USER_CODE = ''


        # 收款方网点信息
        RECEIVE_BANK_BRANCK_NAME_2 = '中国银行青海支行'
        RECEIVE_BANK_BRANCK_CODE_2 = '123456123456'
        # 收款方银行信息
        RECEIVE_BANK_NAME_2 = ''
        RECEIVE_BANK_CODE_2 = '104'
        # 收款方账户信息
        RECEIVE_BANK_USER_NAME_2 = '上海市支付计划往来单位002'
        RECEIVE_BANK_USER_CODE_2 = '656789987678002'
        ROLLBACK_TIME = datetime.datetime.fromisoformat('1900-01-01 00:00:00').strftime("%Y-%m-%d %H:%M:%S")
        # 核发类型
        ISSUED_TO_TYPE = ''
        if BUSINESS_TYPE_CODE == 'QHK10028':
            # 个人收款
            ISSUED_TO_TYPE = '11'
            # 单位+机构
            ISSUED_TO_TYPE = '21'
            ISSUED_TO_TYPE = '31'

        # 收款方类型 1-单位 2-个人
        FIELD04 = '1'
        if ISSUED_TO_TYPE == '11':
            FIELD04 = '2'
        if (BUSINESS_TYPE_CODE == "QHK10027" or BUSINESS_TYPE_CODE == "QHK10029" or BUSINESS_TYPE_CODE == "QHK10031"):
            FIELD04 = '2'
        # 数据处理状态
        DATA_DEAL_STAS = ''
        # 银行支付时间
        BANK_OFFER_TIME = datetime.datetime.fromisoformat('1900-01-01 00:00:00').strftime("%Y-%m-%d %H:%M:%S")
        # 支付状态
        BANK_DATA_STATUS = ''
        # 失败原因
        FAIL_REASON = ''
        # 是否财务记账
        JZ_STATUS = ''
        # 凭证号
        VOU_NO = ''
        # 扣减金额
        CHARGE_AMOUNT = '12.12'
        # 辅助核算代码 名称
        FIELD06 = 'asd名称'
        # 摘要
        SUMMARY = BUSINESS_TYPE_NAME + '测试导入'
        # 预留金额
        ADVANCE_AMOUNT_1 = '111.11'
        ADVANCE_AMOUNT_2 = '222.22'


        sqlz = "insert into qh_smrts_pay_plan_detail_mi values (%(FIELD04)s, %(BATCH_NO)s, %(YE_MONTH)s, %(INSURANCE_CODE)s, %(INSURANCE_NAME)s, %(BUSINESS_TYPE_CODE)s, %(BUSINESS_TYPE_NAME)s, %(AGENCY_CODE)s, %(AGENCY_NAME)s, %(MEDICAL_CODE)s, %(MEDICAL_TYPE)s, %(MEDICAL_NAME)s, %(TOTAL_AMOUNT)s, %(STATUS)s, %(DETAIL_UNIT_NO)s, %(ROLLBACK_REASON)s, %(USER_ACCOUNT_SURPLUS)s, %(SETTLEMENT_COUNT)s, %(RECEIVE_UNIT_NAME)s, %(START_TIME)s, %(END_TIME)s, %(RECEIVE_BANK_BRANCK_NAME)s, %(RECEIVE_BANK_BRANCK_CODE)s, %(RECEIVE_BANK_NAME)s, %(RECEIVE_BANK_CODE)s, %(RECEIVE_BANK_USER_NAME)s, %(RECEIVE_BANK_USER_CODE)s, %(ROLLBACK_TIME)s, %(ISSUED_TO_TYPE)s, %(DATA_DEAL_STAS)s, %(BANK_OFFER_TIME)s, %(BANK_DATA_STATUS)s, %(FAIL_REASON)s, %(JZ_STATUS)s, %(VOU_NO)s, %(CHARGE_AMOUNT)s, %(FIELD06)s, %(SUMMARY)s, %(ADVANCE_AMOUNT)s)"
        valuez1 = {
        "BATCH_NO":BATCH_NO,
        "YE_MONTH":YE_MONTH,
        "INSURANCE_CODE":INSURANCE_CODE,
        "INSURANCE_NAME":INSURANCE_NAME,
        "BUSINESS_TYPE_CODE":BUSINESS_TYPE_CODE,
        "BUSINESS_TYPE_NAME":BUSINESS_TYPE_NAME,
        "AGENCY_CODE":AGENCY_CODE,
        "AGENCY_NAME":AGENCY_NAME,
        "MEDICAL_CODE":MEDICAL_CODE_1,
        "MEDICAL_TYPE":MEDICAL_TYPE_1,
        "MEDICAL_NAME":MEDICAL_NAME_1,
        "TOTAL_AMOUNT":TOTAL_AMOUNT_1,
        "STATUS":STATUS,
        "DETAIL_UNIT_NO":DETAIL_UNIT_NO_1,
        "ROLLBACK_REASON":ROLLBACK_REASON,
        "USER_ACCOUNT_SURPLUS":USER_ACCOUNT_SURPLUS,
        "SETTLEMENT_COUNT":SETTLEMENT_COUNT,
        "RECEIVE_UNIT_NAME":RECEIVE_UNIT_NAME,
        "START_TIME":START_TIME,
        "END_TIME":END_TIME,
        "RECEIVE_BANK_BRANCK_NAME":RECEIVE_BANK_BRANCK_NAME,
        "RECEIVE_BANK_BRANCK_CODE":RECEIVE_BANK_BRANCK_CODE,
        "RECEIVE_BANK_NAME":RECEIVE_BANK_NAME,
        "RECEIVE_BANK_CODE":RECEIVE_BANK_CODE,
        "RECEIVE_BANK_USER_NAME":RECEIVE_BANK_USER_NAME,
        "RECEIVE_BANK_USER_CODE":RECEIVE_BANK_USER_CODE,
        "ROLLBACK_TIME":ROLLBACK_TIME,
        "ISSUED_TO_TYPE":ISSUED_TO_TYPE,
        "FIELD04":FIELD04,
        "DATA_DEAL_STAS":DATA_DEAL_STAS,
        "BANK_OFFER_TIME":BANK_OFFER_TIME,
        "BANK_DATA_STATUS":BANK_DATA_STATUS,
        "FAIL_REASON":FAIL_REASON,
        "JZ_STATUS":JZ_STATUS,
        "VOU_NO":VOU_NO,
        "CHARGE_AMOUNT":CHARGE_AMOUNT,
        "FIELD06":FIELD06,
        "SUMMARY":SUMMARY,
        "ADVANCE_AMOUNT":ADVANCE_AMOUNT_1
        }
        valuez2 = {
        "BATCH_NO":BATCH_NO,
        "YE_MONTH":YE_MONTH,
        "INSURANCE_CODE":INSURANCE_CODE,
        "INSURANCE_NAME":INSURANCE_NAME,
        "BUSINESS_TYPE_CODE":BUSINESS_TYPE_CODE,
        "BUSINESS_TYPE_NAME":BUSINESS_TYPE_NAME,
        "AGENCY_CODE":AGENCY_CODE,
        "AGENCY_NAME":AGENCY_NAME,
        "MEDICAL_CODE":MEDICAL_CODE_2,
        "MEDICAL_TYPE":MEDICAL_TYPE_2,
        "MEDICAL_NAME":MEDICAL_NAME_2,
        "TOTAL_AMOUNT":TOTAL_AMOUNT_2,
        "STATUS":STATUS,
        "DETAIL_UNIT_NO":DETAIL_UNIT_NO_2,
        "ROLLBACK_REASON":ROLLBACK_REASON,
        "USER_ACCOUNT_SURPLUS":USER_ACCOUNT_SURPLUS,
        "SETTLEMENT_COUNT":SETTLEMENT_COUNT,
        "RECEIVE_UNIT_NAME":RECEIVE_UNIT_NAME_2,
        "START_TIME":START_TIME,
        "END_TIME":END_TIME,
        "RECEIVE_BANK_BRANCK_NAME":RECEIVE_BANK_BRANCK_NAME_2,
        "RECEIVE_BANK_BRANCK_CODE":RECEIVE_BANK_BRANCK_CODE_2,
        "RECEIVE_BANK_NAME":RECEIVE_BANK_NAME_2,
        "RECEIVE_BANK_CODE":RECEIVE_BANK_CODE_2,
        "RECEIVE_BANK_USER_NAME":RECEIVE_BANK_USER_NAME_2,
        "RECEIVE_BANK_USER_CODE":RECEIVE_BANK_USER_CODE_2,
        "ROLLBACK_TIME":ROLLBACK_TIME,
        "ISSUED_TO_TYPE":ISSUED_TO_TYPE,
        "FIELD04":FIELD04,
        "DATA_DEAL_STAS":DATA_DEAL_STAS,
        "BANK_OFFER_TIME":BANK_OFFER_TIME,
        "BANK_DATA_STATUS":BANK_DATA_STATUS,
        "FAIL_REASON":FAIL_REASON,
        "JZ_STATUS":JZ_STATUS,
        "VOU_NO":VOU_NO,
        "CHARGE_AMOUNT":CHARGE_AMOUNT,
        "FIELD06":FIELD06,
        "SUMMARY":SUMMARY,
        "ADVANCE_AMOUNT":ADVANCE_AMOUNT_2
        }
        cr.execute(sqlz, valuez1)
        cr.execute(sqlz, valuez2)

        # 只有两定机构、零星支付有孙表数据
        if (BUSINESS_TYPE_CODE == 'QHK10025' or BUSINESS_TYPE_CODE == 'QHK10029' or BUSINESS_TYPE_CODE == 'QHK9903'):
            # 孙表 除两定支付外，其他没有孙表数据
            DETAIL_UNIT_NO_11 = DETAIL_UNIT_NO_1
            MEDICAL_TYPE_CODE_11 = cl_QH_MEDICAL_CATEGORY[int(random.uniform(0,12))]

            DETAIL_UNIT_NO_12 = DETAIL_UNIT_NO_1
            MEDICAL_TYPE_CODE_12 = cl_QH_MEDICAL_CATEGORY[int(random.uniform(0,12))]

            DETAIL_UNIT_NO_21 = DETAIL_UNIT_NO_2
            MEDICAL_TYPE_CODE_21 = cl_QH_MEDICAL_CATEGORY[int(random.uniform(0,12))]

            DETAIL_UNIT_NO_22 = DETAIL_UNIT_NO_2
            MEDICAL_TYPE_CODE_22 = cl_QH_MEDICAL_CATEGORY[int(random.uniform(0,12))]

            PERSON_TYPE = cl_QH_PERSONNEL_CATEGORY[int(random.uniform(0,9))]
            PERSON_TIME = '3'
            TOTAL_AMOUNT = '2133'
            HIFP_PAY = '342'
            HIFMI_PAY = '22'
            CVLSERV_PAY = '33'
            RETIRE_PAY = '344'
            ACCT_PAY = '22'
            HIFDM_PAY = '23'
            THEIR_AGENCY_CODE = ''
            THEIR_AGENCY_NAME = ''
            SHIFP_PAY = '32'
            HIFOB_PAY = '4454'
            DMLC_PAY = '3654'
            HIFES_PAY = '4333'
            OTH_PAY = '5555'
            STATUS = '0'



            sqls = "insert into qh_smrts_pay_plan_item_mi values (%(DETAIL_UNIT_NO)s, %(MEDICAL_TYPE_CODE)s, %(PERSON_TYPE)s, %(PERSON_TIME)s, %(TOTAL_AMOUNT)s, %(HIFP_PAY)s, %(HIFMI_PAY)s, %(CVLSERV_PAY)s, %(RETIRE_PAY)s, %(ACCT_PAY)s, %(HIFDM_PAY)s, %(THEIR_AGENCY_CODE)s, %(THEIR_AGENCY_NAME)s, %(SHIFP_PAY)s, %(HIFOB_PAY)s, %(DMLC_PAY)s, %(HIFES_PAY)s, %(OTH_PAY)s, %(STATUS)s)"
            values1 = {
            "DETAIL_UNIT_NO":DETAIL_UNIT_NO_11,
            "MEDICAL_TYPE_CODE":MEDICAL_TYPE_CODE_11,
            "PERSON_TYPE":PERSON_TYPE,
            "PERSON_TIME":PERSON_TIME,
            "TOTAL_AMOUNT":TOTAL_AMOUNT,
            "HIFP_PAY":HIFP_PAY,
            "HIFMI_PAY":HIFMI_PAY,
            "CVLSERV_PAY":CVLSERV_PAY,
            "RETIRE_PAY":RETIRE_PAY,
            "ACCT_PAY":ACCT_PAY,
            "HIFDM_PAY":HIFDM_PAY,
            "THEIR_AGENCY_CODE":THEIR_AGENCY_CODE,
            "THEIR_AGENCY_NAME":THEIR_AGENCY_NAME,
            "SHIFP_PAY":SHIFP_PAY,
            "HIFOB_PAY":HIFOB_PAY,
            "DMLC_PAY":DMLC_PAY,
            "HIFES_PAY":HIFES_PAY,
            "OTH_PAY":OTH_PAY,
            "STATUS":STATUS

            }
            values2 = {
            "DETAIL_UNIT_NO":DETAIL_UNIT_NO_12,
            "MEDICAL_TYPE_CODE":MEDICAL_TYPE_CODE_12,
            "PERSON_TYPE":PERSON_TYPE,
            "PERSON_TIME":PERSON_TIME,
            "TOTAL_AMOUNT":TOTAL_AMOUNT,
            "HIFP_PAY":HIFP_PAY,
            "HIFMI_PAY":HIFMI_PAY,
            "CVLSERV_PAY":CVLSERV_PAY,
            "RETIRE_PAY":RETIRE_PAY,
            "ACCT_PAY":ACCT_PAY,
            "HIFDM_PAY":HIFDM_PAY,
            "THEIR_AGENCY_CODE":THEIR_AGENCY_CODE,
            "THEIR_AGENCY_NAME":THEIR_AGENCY_NAME,
            "SHIFP_PAY":SHIFP_PAY,
            "HIFOB_PAY":HIFOB_PAY,
            "DMLC_PAY":DMLC_PAY,
            "HIFES_PAY":HIFES_PAY,
            "OTH_PAY":OTH_PAY,
            "STATUS":STATUS
            }
            values11 = {
            "DETAIL_UNIT_NO":DETAIL_UNIT_NO_21,
            "MEDICAL_TYPE_CODE":MEDICAL_TYPE_CODE_21,
            "PERSON_TYPE":PERSON_TYPE,
            "PERSON_TIME":PERSON_TIME,
            "TOTAL_AMOUNT":TOTAL_AMOUNT,
            "HIFP_PAY":HIFP_PAY,
            "HIFMI_PAY":HIFMI_PAY,
            "CVLSERV_PAY":CVLSERV_PAY,
            "RETIRE_PAY":RETIRE_PAY,
            "ACCT_PAY":ACCT_PAY,
            "HIFDM_PAY":HIFDM_PAY,
            "THEIR_AGENCY_CODE":THEIR_AGENCY_CODE,
            "THEIR_AGENCY_NAME":THEIR_AGENCY_NAME,
            "SHIFP_PAY":SHIFP_PAY,
            "HIFOB_PAY":HIFOB_PAY,
            "DMLC_PAY":DMLC_PAY,
            "HIFES_PAY":HIFES_PAY,
            "OTH_PAY":OTH_PAY,
            "STATUS":STATUS

            }
            values22 = {
            "DETAIL_UNIT_NO":DETAIL_UNIT_NO_22,
            "MEDICAL_TYPE_CODE":MEDICAL_TYPE_CODE_22,
            "PERSON_TYPE":PERSON_TYPE,
            "PERSON_TIME":PERSON_TIME,
            "TOTAL_AMOUNT":TOTAL_AMOUNT,
            "HIFP_PAY":HIFP_PAY,
            "HIFMI_PAY":HIFMI_PAY,
            "CVLSERV_PAY":CVLSERV_PAY,
            "RETIRE_PAY":RETIRE_PAY,
            "ACCT_PAY":ACCT_PAY,
            "HIFDM_PAY":HIFDM_PAY,
            "THEIR_AGENCY_CODE":THEIR_AGENCY_CODE,
            "THEIR_AGENCY_NAME":THEIR_AGENCY_NAME,
            "SHIFP_PAY":SHIFP_PAY,
            "HIFOB_PAY":HIFOB_PAY,
            "DMLC_PAY":DMLC_PAY,
            "HIFES_PAY":HIFES_PAY,
            "OTH_PAY":OTH_PAY,
            "STATUS":STATUS
            }
            cr.execute(sqls, values1)
            cr.execute(sqls, values2)
            cr.execute(sqls, values11)
            cr.execute(sqls, values22)


        no += 1
        n -= 1

    cr.close()
    db.commit()
    db.close()
    endtime = datetime.datetime.now()
    print("生成时间：" + otherStyleTime)
    print("耗时H：" + str(round((endtime - starttime).seconds / 3600, 2)))


if __name__ == '__main__':
    # 第一参数：0-上海 1-黄埔，2-河北省 3-西宁本级 4-西宁市城东区
    # cl_bussnisstype_code = ['QHK10025','QHK10026','QHK10027','QHK10028','QHK10029','QHK10030','QHK10031','QHK9903','QHK9902','QHK10032','QHK10033']
    # cl_bussnisstype_name = ['青海支付计划两定结算','青海支付计划医院预付','青海支付计划转移支出','青海支付计划生育津贴支出','青海支付计划零星报销','青海支付计划征缴退费','青海支付计划个账结算']
    # 第二参数：0-QHK10025 青海支付计划两定结算
    # 第三参数：数据类型1-支付计划 2-统支
    # 第四参数：险种 0-310 1-320 2-330 3-390
    # 第五参数：数据条数
    #异地两定
    make_sql(4,10,1,0,10)
    # #异地拨款
    # make_sql(3,10,1,0,2)
    # #两定
    # make_sql(3,0,1,0,2)
    # 预付
    # make_sql(0,1,1,10)
    # 转移支出
    # make_sql(0,2,1,1)
    # 生育
    # make_sql(0,3,1,1)
    # 零星
    # make_sql(0,4,1,10)
    # 个账结算
    # make_sql(0,6,1,1)
    # 测试业务类型
    # make_sql(0,7,1,1)
    # make_sql(0,8,1,1)


