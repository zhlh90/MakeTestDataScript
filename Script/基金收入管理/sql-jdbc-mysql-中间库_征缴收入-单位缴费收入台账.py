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
        db='sifcmiddledb',##数据库名
        charset='utf8'##连接编码
    )
    #创建游标
    cr = db.cursor()

    no = 1
    while (n > 0):

        ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        AAA027 = '00'
        AAA041 = round(random.uniform(1000, 10), 2)
        AAA042 = round(random.uniform(1000, 10), 2)
        AAA115 = '10'
        AAA321 = ran_strx("12345690",1)
        AAA322 = otherStyleTime3 + ran_strx("0123456789", 10)
        AAB001 = 'DWBH' + ran_strx("1234567890", 8)
        AAB034 = cl_agency_code[agency_code_num]
        AAB084 = round(random.uniform(100000, 10), 2)
        AAB119 = ran_strx("123456789", 4)
        AAB120 = round(random.uniform(100000, 10), 2)
        AAB121 = round(random.uniform(100000, 10), 2)
        AAB165 = '10'
        AAD009 = ran_strx("1234567890", 8)
        AAE003 = '202011'
        AAE056 = round(random.uniform(1000, 10), 2)
        AAE080 = round(random.uniform(100000, 10), 2)
        AAE082 = round(random.uniform(10000, 10), 2)
        AAE140 = cl_ins_code[ins_no]
        AAE239 = '1'
        AAE418 = '202011031220'
        AAE530 = otherStyleTime2
        AAE531 = otherStyleTime
        AAF020 = otherStyleTime
        AAZ288 = ran_strx("1234567890", 8)
        AAZ400 = '8836'
        PLAN_ID = ''
        REC_STATUS = ''
        REC_NO = ''
        REC_TIME = now
        EXCHANGE_PLAN_ID = 'ec0642fc1ea54c97a151b604ce9ad7b1'
        EXCHANGE_PLAN_STATUS = '1'
        VOU_GUID = ''
        VOU_NO = ''
        VOU_DATE = ''
        VOU_STATUS = ''
        FIELD01 = ''
        FIELD02 = ''
        FIELD03 = ''
        FIELD04 = ''
        FIELD05 = ''
        FIELD06 = ''
        FIELD07 = ''
        FIELD08 = ''
        FIELD09 = ''
        FIELD10 = ''
        FIELD11 = ''
        FIELD12 = ''
        FIELD13 = ''
        FIELD14 = ''
        FIELD15 = ''
        FIELD16 = ''
        FIELD17 = ''
        FIELD18 = ''
        FIELD19 = ''
        FIELD20 = ''
        AMT01 = 0
        AMT02 = 0
        AMT03 = 0
        AMT04 = 0
        AMT05 = 0
        AMT06 = 0
        AMT07 = 0
        AMT08 = 0
        AMT09 = 0
        AMT10 = 0
        UUID = ID


        sqlG = "insert into SMR_UNIT_PAYMENT_DETAIL values (%(ID)s, %(AAA027)s, %(AAA041)s, %(AAA042)s, %(AAA115)s, %(AAA321)s, %(AAA322)s, %(AAB001)s, %(AAB034)s, %(AAB084)s, %(AAB119)s, %(AAB120)s, %(AAB121)s, %(AAB165)s, %(AAD009)s, %(AAE003)s, %(AAE056)s, %(AAE080)s, %(AAE082)s, %(AAE140)s, %(AAE239)s, %(AAE418)s, %(AAE530)s, %(AAE531)s, %(AAF020)s, %(AAZ288)s, %(AAZ400)s, %(PLAN_ID)s, %(REC_STATUS)s, %(REC_NO)s, %(REC_TIME)s, %(EXCHANGE_PLAN_ID)s, %(EXCHANGE_PLAN_STATUS)s, %(VOU_GUID)s, %(VOU_NO)s, %(VOU_DATE)s, %(VOU_STATUS)s, %(FIELD01)s, %(FIELD02)s, %(FIELD03)s, %(FIELD04)s, %(FIELD05)s, %(FIELD06)s, %(FIELD07)s, %(FIELD08)s, %(FIELD09)s, %(FIELD10)s, %(FIELD11)s, %(FIELD12)s, %(FIELD13)s, %(FIELD14)s, %(FIELD15)s, %(FIELD16)s, %(FIELD17)s, %(FIELD18)s, %(FIELD19)s, %(FIELD20)s, %(AMT01)s, %(AMT02)s, %(AMT03)s, %(AMT04)s, %(AMT05)s, %(AMT06)s, %(AMT07)s, %(AMT08)s, %(AMT09)s, %(AMT10)s, %(UUID)s)"
        value = {
        "ID": ID,
        "AAA027": AAA027,
        "AAA041": AAA041,
        "AAA042": AAA042,
        "AAA115": AAA115,
        "AAA321": AAA321,
        "AAA322": AAA322,
        "AAB001": AAB001,
        "AAB034": AAB034,
        "AAB084": AAB084,
        "AAB119": AAB119,
        "AAB120": AAB120,
        "AAB121": AAB121,
        "AAB165": AAB165,
        "AAD009": AAD009,
        "AAE003": AAE003,
        "AAE056": AAE056,
        "AAE080": AAE080,
        "AAE082": AAE082,
        "AAE140": AAE140,
        "AAE239": AAE239,
        "AAE418": AAE418,
        "AAE530": AAE530,
        "AAE531": AAE531,
        "AAF020": AAF020,
        "AAZ288": AAZ288,
        "AAZ400": AAZ400,
        "PLAN_ID": PLAN_ID,
        "REC_STATUS": REC_STATUS,
        "REC_NO": REC_NO,
        "REC_TIME": REC_TIME,
        "EXCHANGE_PLAN_ID": EXCHANGE_PLAN_ID,
        "EXCHANGE_PLAN_STATUS": EXCHANGE_PLAN_STATUS,
        "VOU_GUID": VOU_GUID,
        "VOU_NO": VOU_NO,
        "VOU_DATE": VOU_DATE,
        "VOU_STATUS": VOU_STATUS,
        "FIELD01": FIELD01,
        "FIELD02": FIELD02,
        "FIELD03": FIELD03,
        "FIELD04": FIELD04,
        "FIELD05": FIELD05,
        "FIELD06": FIELD06,
        "FIELD07": FIELD07,
        "FIELD08": FIELD08,
        "FIELD09": FIELD09,
        "FIELD10": FIELD10,
        "FIELD11": FIELD11,
        "FIELD12": FIELD12,
        "FIELD13": FIELD13,
        "FIELD14": FIELD14,
        "FIELD15": FIELD15,
        "FIELD16": FIELD16,
        "FIELD17": FIELD17,
        "FIELD18": FIELD18,
        "FIELD19": FIELD19,
        "FIELD20": FIELD20,
        "AMT01": AMT01,
        "AMT02": AMT02,
        "AMT03": AMT03,
        "AMT04": AMT04,
        "AMT05": AMT05,
        "AMT06": AMT06,
        "AMT07": AMT07,
        "AMT08": AMT08,
        "AMT09": AMT09,
        "AMT10": AMT10,
        "UUID": UUID
        }

        cr.execute(sqlG,value)

        sqlU = "update SMR_UNIT_PAYMENT_DETAIL set PLAN_ID=null,REC_STATUS=null,REC_NO=null,REC_TIME=null,VOU_GUID=null,VOU_NO=null,VOU_DATE=null,VOU_STATUS=null,FIELD01=null,FIELD02=null,FIELD03=null,FIELD04=null,FIELD05=null,FIELD06=null,FIELD07=null,FIELD08=null,FIELD09=null,FIELD10=null,FIELD11=null,FIELD12=null,FIELD13=null,FIELD14=null,FIELD15=null,FIELD16=null,FIELD17=null,FIELD18=null,FIELD19=null,FIELD20=null,AMT01=null,AMT02=null,AMT03=null,AMT04=null,AMT05=null,AMT06=null,AMT07=null,AMT08=null,AMT09=null,AMT10=null "
        cr.execute(sqlU)

        if n % 10000 == 0:
            db.commit()

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
    make_sql(0,0,1)



