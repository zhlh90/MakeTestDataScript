# -*- coding: utf-8 -*
import datetime
import time

# import pandas as pd
import random
import string
from Script import shenfenzhenghao
from enum import Enum
import os

# 业务类型
# cl_bussnisstype_code = ['K10025','K1002501','K1002502','K1002503','K1002504','K1002505','K1002506','K1002507','K1002508','K1002509','K1002510','K1002511','K1002512','K1002513','K1002514','K1002515']
# cl_bussnisstype_name = ['两定机构月结支付','地税回盘实收到帐','地税回盘失败','统筹范围外医保基金转移','跨省异地清算','大额医疗保险费','中心报销','中心报销大额','异地清算扣款','月结算','跨省大额预付金','省内异地清算','跨省大额预付金上解','省内大额预付金','账户返还','年结算']


#cl_bussnisstype_code = ['KB0301']
#cl_bussnisstype_name = ['月结算-医院']

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

    path = '../Data_sql/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'MID_PAY_PLAN_KC0302'+str(otherStyleTime3)+'.sql'
    # file_name_item = path + 'MID_PAY_PLAN_ITEM'+str(otherStyleTime3)+'.sql'
    SMRTS_PAY_PLAN_file = open(file_name, 'w', encoding='utf-8')
    # SMRTS_PAY_PLAN_ITEM_file = open(file_name_item, 'w', encoding='utf-8')

    # 主子表sql
    str_head_zhu = "insert into MID_PAY_PLAN values ("
    str_head_item = "insert into MID_PAY_PLAN_ITEM values ("

    no = 1
    while (n > 0):
        # 主表
        p1 = '2020-07'
        p2 = '310'
        p3 = '城镇职工基本医疗保险'
        p4 = 'YW' + otherStyleTime4 + str(n)
        p5 = ''
        p6 = country_code
        p7 = '上海市统筹'
        p8 = country_code
        p9 = '上海市医保中心'
        #num = int(random.uniform(0, 2))
        p10 = 'KB0302'
        p11 = '月结算-药店'

        p12 = '2'
        p13 = '526.00'
        status = '0'

        # 子表
        s1 = '310'
        s2 = '城镇职工基本医疗保险'
        s3 = '2020-07'
        s100 = p4   #业务单号
        s4 = '001'
        s5 = '上海市第一医院'

        s4_2 = '002'
        s5_2 = '上海市第二医院'

        #s4_3 = '00400003'
        #s5_3 = '上海市支付计划往来单位003'

        s6 = '6'
        s7 = '7'
        s8 = '8'
        s9 = '9'
        s10 = '123.01'

        s10_2 = '402.99'

        #s10_3 = '3333.33'

        s11 = '100.02'
        s12 = '50.00'
        s13 = '60.66'
        s14 = '80.12'
        s15 = '16.88'
        s16 = '1111111111111221'
        s17 = '1111111111111220'
        s18 = '320.56'
        s19 = '20'
        s20 = '21'
        s21 = '22'
        s22 = '23'
        s23 = '11.11'
        s24 = '123.01'
        s25 = '263.12'
        s26 = '27'
        s27 = '28'
        s28 = '29'
        s29 = '30'
        s30 = '31'
        s31 = '32'
        s32 = '33'
        s33 = '34'
        s34 = '35'
        s35 = '36'
        s36 = '37'
        s37 = '38'
        s38 = '39'
        s39 = '40'
        s40 = '41'
        s41 = '42'
        s42 = '43'
        s43 = '44'
        s44 = '45'
        s45 = '事业'
        s46 = '测试1'




        line = str_head_zhu + '"' + p1 + '", "' + p2 + '", "' + p3 + '", "' + p4 + '", "' + p5 + '", "' + p6 + '", "' + p7 + '", "' + p8 + '", "' + p9 + '", "' + p10 + '", "' + p11 + '", "' + p12 + '", "' + p13 + '", "' + status + '");'

        line_item1 = str_head_item + '"' + s1 + '", "' + s2 + '", "' + s3 + '", "' + s4 + '", "' + s5 + '", "' + s6 + '", "' + s7 + '", "' + s8 + '", "' + s9 + '", "' + s10 + '", "' + s11 + '", "' + s12 + '", "' + s13 + '", "' + s14 + '", "' + s15 \
                     + '", "' + s16 + '", "' + s17 + '", "' + s18 + '", "' + s19 + '", "' + s20 + '", "' + s21 + '", "' + s22 + '", "' + s23 + '", "' + s24 + '", "' + s25 + '", "' + s26 + '", "' + s27 + '", "' + s28 + '", "' + s29 + '", "' + s30 + '", "' + s31\
                     + '", "' + s32 + '", "' + s33 + '", "' + s34 + '", "' + s35 + '", "' + s36 + '", "' + s37 + '", "' + s38 + '", "' + s39 + '", "' + s40 + '", "' + s41 + '", "' + s42 + '", "' + s43 + '", "' + s44 + '", "' + s45 + '", "' + s46 + '", "' + s100 + '");'
        line_item2 = str_head_item + '"' + s1 + '", "' + s2 + '", "' + s3 + '", "' + s4_2 + '", "' + s5_2 + '", "' + s6 + '", "' + s7 + '", "' + s8 + '", "' + s9 + '", "' + s10_2 + '", "' + s11 + '", "' + s12 + '", "' + s13 + '", "' + s14 + '", "' + s15 \
                     + '", "' + s16 + '", "' + s17 + '", "' + s18 + '", "' + s19 + '", "' + s20 + '", "' + s21 + '", "' + s22 + '", "' + s23 + '", "' + s24 + '", "' + s25 + '", "' + s26 + '", "' + s27 + '", "' + s28 + '", "' + s29 + '", "' + s30 + '", "' + s31\
                     + '", "' + s32 + '", "' + s33 + '", "' + s34 + '", "' + s35 + '", "' + s36 + '", "' + s37 + '", "' + s38 + '", "' + s39 + '", "' + s40 + '", "' + s41 + '", "' + s42 + '", "' + s43 + '", "' + s44 + '", "' + s45 + '", "' + s46 + '", "' + s100 + '");'
        #line_item3 = str_head_item + '"' + s1 + '", "' + s2 + '", "' + s3 + '", "' + s4_3 + '", "' + s5_3 + '", "' + s6 + '", "' + s7 + '", "' + s8 + '", "' + s9 + '", "' + s10_3 + '", "' + s11 + '", "' + s12 + '", "' + s13 + '", "' + s14 + '", "' + s15 \
                     #+ '", "' + s16 + '", "' + s17 + '", "' + s18 + '", "' + s19 + '", "' + s20 + '", "' + s21 + '", "' + s22 + '", "' + s23 + '", "' + s24 + '", "' + s25 + '", "' + s26 + '", "' + s27 + '", "' + s28 + '", "' + s29 + '", "' + s30 + '", "' + s31\
                     #+ '", "' + s32 + '", "' + s33 + '", "' + s34 + '", "' + s35 + '", "' + s36 + '", "' + s37 + '", "' + s38 + '", "' + s39 + '", "' + s40 + '", "' + s41 + '", "' + s42 + '", "' + s43 + '", "' + s44 + '", "' + s45 + '", "' + s46 + '", "' + s100 + '");'


        line = line.replace('\"', '\'')
        line_item1 = line_item1.replace('\"', '\'')
        line_item2 = line_item2.replace('\"', '\'')
        #line_item3 = line_item3.replace('\"', '\'')
        no += 1
        n -= 1

        SMRTS_PAY_PLAN_file.write(line + '\n')
        SMRTS_PAY_PLAN_file.write(line_item1 + '\n')
        SMRTS_PAY_PLAN_file.write(line_item2 + '\n')
        #SMRTS_PAY_PLAN_file.write(line_item3 + '\n')



if __name__ == '__main__':
    # 传参： country_code, n
    make_sql('00', 5)


