import datetime
# import cx_Oracle
import pymysql
import random

# 险种
cl_insurance_code = ['310','390']
cl_insurance_name = ['城镇职工基本医疗保险','城乡居民基本医疗保险']
# 经办机构
cl_agency_code = ['00','01']
cl_agency_name = ['上海市医保局局','黄浦区医保局']
# 行政区划
cl_org_code = ['310000','310100']
cl_org_name = ['上海市','黄浦区']
# 业务类型 401-非现金，402-现金,现金-1、非现金-2子表pay_type需要更改
cl_businesstype_code = ['K1002401','K1002402']
cl_businesstype_name = ['零星报销-银行卡支付','零星报销-现金支付']
pay_type = ['2','1']

# 从字符串中随机取n个字符组成字符串
def ran_strx(strx, n):
    items = list(strx)
    str2 = ''
    for i in range(0, n):
        str1 = items[random.randint(0, len(items)-1)]
        str2 += str1
    return str2

#随机生成一串长度为n的数字形式字符串
def ran_intstr(n):
    int_str = ''
    for i in range (0,n):
        items = random.randint(1,9)
        int_str += str(items)
    return (int_str)

#获得当前时间
now = datetime.datetime.now()
#转换为制定格式
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
otherStyleTime1 = now.strftime("%Y%m%d%H")
otherStyleTime2 = now.strftime("%Y-%m-%d")
otherStyleTime3 = now.strftime("%Y%m%d%H%M%S")
otherStyleTime4 = now.strftime("%Y%m%d%H%M")
otherStyleTime5 = now.strftime("%Y-%m")
otherStyleTime6 = now.strftime("%Y%m")

def make_sql(agency_code,insur_num,bus_type,n):
    starttime = datetime.datetime.now()
    db = pymysql.connect(
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

    while(n>0):
        #主表信息
        BILL_NO = 'SMCS'+ otherStyleTime3 + str(n)
        BATCH_NO = 'SMCS'+ otherStyleTime3 +'00'+ str(n)
        APPLY_USER_NAME = ran_strx( "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤",3)
        APPLY_USER_CARD_ID = ran_intstr(10)
        REFUND_AMOUNT = str(100 + n)
        MEDICAL_CARD = ran_intstr(10)
        BANK_CODE = random.choice(['313','000'])
        BANK_TYPE = BANK_CODE
        BANK_ACCOUNT_NAME = APPLY_USER_NAME
        BANK_CARD_ACCOUNT = ran_intstr(16)
        AREA_CODE = cl_org_code[agency_code]
        AREA_NAME = cl_org_name[agency_code]
        CENTER_CODE = cl_agency_code[agency_code]
        CENTER_NAME = cl_agency_name[agency_code]
        PAY_PERIOD = otherStyleTime6
        BUSINESS_TYPE = cl_businesstype_code[bus_type]
        PAY_TYPE = pay_type[bus_type]
        STATUS = '0'
        INSURANCE_CODE = cl_insurance_code[insur_num]
        INSURANCE_NAME = cl_insurance_name[insur_num]
        ROLLBACK_REASON = None
        ROLLBACK_TIME = None

        sqlG = "insert into MID_CASH values (%(BILL_NO)s,%(BATCH_NO)s,%(APPLY_USER_NAME)s,%(APPLY_USER_CARD_ID)s,%(REFUND_AMOUNT)s,%(MEDICAL_CARD)s,%(BANK_CODE)s,%(BANK_TYPE)s,%(BANK_ACCOUNT_NAME)s,%(BANK_CARD_ACCOUNT)s,%(AREA_CODE)s,%(AREA_NAME)s,%(CENTER_CODE)s,%(CENTER_NAME)s,%(PAY_PERIOD)s,%(BUSINESS_TYPE)s,%(PAY_TYPE)s,%(STATUS)s,%(INSURANCE_CODE)s,%(INSURANCE_NAME)s,%(ROLLBACK_REASON)s,%(ROLLBACK_TIME)s)"
        # sqlG = "insert into MID_CASH values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        valueG = {
            "BILL_NO":BILL_NO,
            "BATCH_NO":BATCH_NO,
            "APPLY_USER_NAME":APPLY_USER_NAME,
            "APPLY_USER_CARD_ID":APPLY_USER_CARD_ID,
            "REFUND_AMOUNT":REFUND_AMOUNT,
            "MEDICAL_CARD":MEDICAL_CARD,
            "BANK_CODE":BANK_CODE,
            "BANK_TYPE":BANK_TYPE,
            "BANK_ACCOUNT_NAME":BANK_ACCOUNT_NAME,
            "BANK_CARD_ACCOUNT":BANK_CARD_ACCOUNT,
            "AREA_CODE":AREA_CODE,
            "AREA_NAME":AREA_NAME,
            "CENTER_CODE":CENTER_CODE,
            "CENTER_NAME":CENTER_NAME,
            "PAY_PERIOD":PAY_PERIOD,
            "BUSINESS_TYPE":BUSINESS_TYPE,
            "PAY_TYPE":PAY_TYPE,
            "STATUS":STATUS,
            "INSURANCE_CODE":INSURANCE_CODE,
            "INSURANCE_NAME":INSURANCE_NAME,
            "ROLLBACK_REASON":ROLLBACK_REASON,
            "ROLLBACK_TIME":ROLLBACK_TIME
        }

        cr.execute(sqlG,valueG)
        print('insert into MID_CASH values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' %(BILL_NO,BATCH_NO,APPLY_USER_NAME,APPLY_USER_CARD_ID,REFUND_AMOUNT,MEDICAL_CARD,BANK_CODE,BANK_TYPE,BANK_ACCOUNT_NAME,BANK_CARD_ACCOUNT,AREA_CODE,AREA_NAME,CENTER_CODE,CENTER_NAME,PAY_PERIOD,BUSINESS_TYPE,PAY_TYPE,STATUS,INSURANCE_CODE,INSURANCE_NAME,ROLLBACK_REASON,ROLLBACK_TIME))

        #子表信息,生成款项01，款项02
        m=0;
        for m in (0,1):
            firstNull = None
            BATCH_NO_det = BATCH_NO
            BILL_NO_det = BILL_NO
            MEDICAL_TYPE = '1'
            PAY_TARGET ='1'
            HOSPITAL_LV = '1'
            if m == 0:
                TOTAL_AMOUNT = '50'
                SELF_AMOUNT = '0'
                REFUND_AMOUNT = '50'
                SETTLE_TYPE = '1'
                SETTLE_TYPE_NAME = '费款项001'
            if m == 1:
                TOTAL_AMOUNT = str(50+n)
                SELF_AMOUNT = '0'
                REFUND_AMOUNT = str(50+n)
                SETTLE_TYPE = '2'
                SETTLE_TYPE_NAME = '费款项002'

            sqlZ = "insert into MID_CASH_ITEM values (%(firstNull)s,%(BATCH_NO_det)s,%(BILL_NO_det)s,%(TOTAL_AMOUNT)s,%(SETTLE_TYPE)s,%(SELF_AMOUNT)s,%(REFUND_AMOUNT)s,%(MEDICAL_TYPE)s,%(PAY_TARGET)s,%(HOSPITAL_LV)s,%(SETTLE_TYPE_NAME)s);"
            valueZ = {
                "firstNull":firstNull,
                "BATCH_NO_det":BATCH_NO_det,
                "BILL_NO_det":BILL_NO_det,
                "TOTAL_AMOUNT":TOTAL_AMOUNT,
                "SETTLE_TYPE":SETTLE_TYPE,
                "SELF_AMOUNT":SELF_AMOUNT,
                "REFUND_AMOUNT":REFUND_AMOUNT,
                "MEDICAL_TYPE":MEDICAL_TYPE,
                "PAY_TARGET":PAY_TARGET,
                "HOSPITAL_LV":HOSPITAL_LV,
                "SETTLE_TYPE_NAME":SETTLE_TYPE_NAME
            }
            cr.execute(sqlZ,valueZ)
            print ('insert into MID_CASH_ITEM values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' %(firstNull,BATCH_NO_det,BILL_NO_det,TOTAL_AMOUNT,SETTLE_TYPE,SELF_AMOUNT,REFUND_AMOUNT,MEDICAL_TYPE,PAY_TARGET,HOSPITAL_LV,SETTLE_TYPE_NAME))
            m += 1
        n -=1

    cr.close()
    db.commit()
    db.close()
    endtime = datetime.datetime.now()
    print("耗时H：" + str(round((endtime - starttime).seconds / 3600, 2)))

if __name__ == '__main__':
    # def make_sql(agency_code,insur_num,bus_type,n):
    # 第一参数：0-上海 1-黄埔
    # 第二参数：0-310 1-390
    # 第三参数：数据类型，0-银行卡，1-现金
    # 第四参数：数据条数
    make_sql(0,0,0,15)










