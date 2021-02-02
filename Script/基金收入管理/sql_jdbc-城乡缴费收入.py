# -*- coding: utf-8 -*
import datetime
import cx_Oracle
import random
import string
from faker import Faker, Factory

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

# 统筹区
cl_country_code = ['00','130000','34000001','34000001']
cl_country_name = ['上海市统筹','河北省统筹','安徽省统筹','安徽省统筹']

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

def make_sql(agency_no, insurance_code, n):

    starttime = datetime.datetime.now()
    db = cx_Oracle.connect('smifcmiddledb/1@10.10.66.159:1521/orcl')
    cr = db.cursor() #创建游标
    # 通过工厂函数来创建
    fake1 = Factory.create()
    # 通过构造函数来创建
    fake2 = Faker()
    fake_cn = Faker("zh_CN")

    no = 1
    while (n > 0):

        UUID  = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        AGENCY_CODE = cl_agency_code[agency_no]
        AGENCY_NAME = cl_agency_name[agency_no]
        INSURANCE_CODE = '390'
        INSURANCE_NAME = '城乡居民基本医疗保险'
        AAA027 = cl_country_code[agency_no]
        AAA041 = round(random.uniform(1000, 10), 2)
        AAA042 = round(random.uniform(1000, 10), 2)
        AAA115 = '10'
        AAA321 = ran_strx("12345690",1)
        AAA322 = otherStyleTime3 + ran_strx("0123456789", 10)
        AAB001 = 'DWBH' + ran_strx("1234567890", 8)
        AAB084 = round(random.uniform(100000, 10), 2)
        AAB119 = ran_strx("123456789", 4)
        AAB120 = round(random.uniform(100000, 10), 2)
        AAB121 = round(random.uniform(100000, 10), 2)
        AAB165 = '10'
        AAD009 = ran_strx("1234567890", 8)
        AAE003 = '202008'
        AAE056 = round(random.uniform(1000, 10), 2)
        AAE080 = round(random.uniform(100000, 10), 2)
        AAE082 = round(random.uniform(10000, 10), 2)
        AAE239 = '1'
        AAE418 = '202008041220'
        AAE530 = otherStyleTime
        AAE531 = otherStyleTime
        AAF020 = otherStyleTime
        AAZ288 = ran_strx("1234567890", 8)
        AAZ400 = '8836'
        STATUS = '0'

        sqlZ = " insert into MID_UNIT_PAYMENT_DETAIL_CHX(UUID, AGENCY_CODE, AGENCY_NAME, INSURANCE_CODE, INSURANCE_NAME, AAA027, AAA041, AAA042, AAA115, AAA321, AAA322, AAB001, AAB084, AAB119, AAB120, AAB121, AAB165, AAD009, AAE003, AAE056, AAE080, AAE082, AAE239, AAE418, AAE530, AAE531, AAF020, AAZ288, AAZ400, STATUS)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30) "

        cr.execute(sqlZ, (UUID, AGENCY_CODE, AGENCY_NAME, INSURANCE_CODE, INSURANCE_NAME, AAA027, AAA041, AAA042, AAA115, AAA321, AAA322, AAB001, AAB084, AAB119, AAB120, AAB121, AAB165, AAD009, AAE003, AAE056, AAE080, AAE082, AAE239, AAE418, AAE530, AAE531, AAF020, AAZ288, AAZ400, STATUS))


        no += 1
        n -= 1
        if( n%100 == 0):
            print(n)
            db.commit()

    cr.close()
    db.commit()
    db.close()
    endtime = datetime.datetime.now()
    print("耗时H：" + str(round((endtime - starttime).seconds / 3600, 2)))


if __name__ == '__main__':
    # 传参： agency_code, insurance_code, n
    make_sql(0, '390', 4)


