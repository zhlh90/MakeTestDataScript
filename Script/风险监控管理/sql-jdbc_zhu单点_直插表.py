# -*- coding: utf-8 -*
import datetime
import cx_Oracle
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

def make_sql(n):

    starttime = datetime.datetime.now()
    db = cx_Oracle.connect('ybjjdb/test1@10.10.66.159:1521/orcl')
    # db = cx_Oracle.connect('ptmifc/1@10.10.66.159:1521/orcl')
    cr = db.cursor() #创建游标

    no = 1
    while (n > 0):

        ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))
        #LAST_MODIFIED_DATE = datetime.datetime.now()
        LAST_MODIFIED_DATE = datetime.datetime.fromisoformat('2020-11-05 19:00:00')
        # FUND_BATCH_NO = '1'
        FUND_BATCH_NO = '2'
        AGENCY_CODE = '00'
        INSURANCE_CODE = '310'
        INSURANCE_NAME = '城镇职工基本医疗保险'
        AGENCY_NAME = '上海市医疗保障局'

        sqlG = " insert into zhu_smrw_rule_002(ID, LAST_MODIFIED_DATE, FUND_BATCH_NO, AGENCY_CODE, INSURANCE_CODE, INSURANCE_NAME, AGENCY_NAME)  " \
               " values (:1,:2,:3,:4,:5,:6,:7) "

        cr.execute(sqlG, (ID, LAST_MODIFIED_DATE, FUND_BATCH_NO, AGENCY_CODE, INSURANCE_CODE, INSURANCE_NAME, AGENCY_NAME))

        no += 1
        n -= 1
        if( n%200 == 0):
            print(n)
            db.commit()

    cr.close()
    db.commit()
    db.close()
    endtime = datetime.datetime.now()
    print("耗时H：" + str(round((endtime - starttime).seconds / 3600, 2)))
    print(str(starttime))
    print(str(endtime))


if __name__ == '__main__':
    # 传参： aab034, n
    # 第一参数：0-上海 1-黄埔，2-河北省
    # 第二参数：0-310 1-390
    make_sql(50000)


