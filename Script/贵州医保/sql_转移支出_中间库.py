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
# 经办机构
cl_agency_code = ['00','01','1300','520201']
cl_agency_name = ['上海保险事业管理局','黄浦区保险事业管理局','河北省','六盘水市本级']
# 统筹区
cl_country_code = ['00','00','130000','520200']
cl_country_name = ['上海市统筹','上海市统筹','河北省统筹','六盘水市']
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

def make_sql(agency_no,ins_no, n):

    path = '../../Data_sql/转移支出/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'MID_TRANSFER_PAY'+str(otherStyleTime3)+'.sql'
    smcs_cash_file = open(file_name, 'w', encoding='utf-8')

    # 主表sql
    str_head_zhu = "insert into mid.MID_TRANSFER_PAY values ("

    no = 1
    while (n > 0):

        t1='ZYZF'+otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 5))
        t2=cl_country_code[agency_no]
        t3=cl_country_name[agency_no]
        insurance_code=cl_ins_code[ins_no]
        insurance_name=cl_ins_name[ins_no]
        t6='张三'
        t7='230128199909143832'
        agency_code=cl_agency_code[agency_no]
        agency_name=cl_agency_name[agency_no]
        t10='1111000.00'
        t11='110000.00'
        t12=cl_agency_name[agency_no]
        t13=cl_agency_name[agency_no]
        t14='99999994'
        t15=cl_agency_name[agency_no]
        t16='313'
        t17='上海银行'
        t18='测试'
        t19=otherStyleTime2
        status='0'


        line = str_head_zhu + '"' + t1  + '", "' + t2  + '", "' + t3  + '", "' + insurance_code  + '", "' + insurance_name  + '", "' + t6  + '", "' + t7  + '", "' + agency_code     + '", "' + agency_name     + '", "' + t10 + '", "' + t11 + '", "' + t12 + '", "' + t13 + '", "' + t14 + '", "' + t15 + '", "' + t16 + '", "' + t17 + '", "' + t18 + '", "' + t19 + '", "' + status + '");'

        line = line.replace('\"', '\'')
        no += 1
        n -= 1

        smcs_cash_file.write(line + '\n')


if __name__ == '__main__':
    # 第一参数：0-上海 1-黄埔，2-河北省，3-六盘水市本级
    # 第二参数：0-310 1-390
    # 第三参数：数据条数
    make_sql(3,0,2)


