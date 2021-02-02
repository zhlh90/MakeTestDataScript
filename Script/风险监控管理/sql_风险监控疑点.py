# -*- coding: utf-8 -*
import datetime

# import pandas as pd
import random
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
otherStyleTime4 = now.strftime("%m%d%H%M")

def make_sql(country_code, n):

    path = '../../Data_sql/风险监控疑点/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'TEST_01'+str(otherStyleTime3)+'.sql'
    smcs_cash_file = open(file_name, 'w', encoding='utf-8')

    # 主表sql
    str_head_zhu = "insert into TEST001 values ("

    no = 1
    while (n > 0):

        ID = 'aa' + str(n)
        LAST_MODIFIED_DATE = otherStyleTime
        FIELD1 = ran_strx("0123456789", 1)
        FIELD2 = ran_strx("0123456789", 1)
        FIELD3 = ran_strx("0123456789", 1)
        AAE140 = '310'


        line = str_head_zhu + '"' + FIELD1 + '", "' + FIELD2 + '", "' + FIELD3 + '", "' + ID + '", TO_TIMESTAMP(\'' + LAST_MODIFIED_DATE + '\',\'SYYYY-MM-DD HH24:MI:SS:FF6\'), "' + AAE140 + '");'

        line = line.replace('\"', '\'')
        no += 1
        n -= 1

        smcs_cash_file.write(line + '\n')


if __name__ == '__main__':
    # 传参： country_code, n
    make_sql('00', 2)


