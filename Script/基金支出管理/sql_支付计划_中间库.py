# -*- coding: utf-8 -*
import datetime

# import pandas as pd
import random
import os

# 业务类型
# cl_bussnisstype_code = ['K10025','K1002501','K1002502','K1002503','K1002504','K1002505','K1002506','K1002507','K1002508','K1002509','K1002510','K1002511','K1002512','K1002513','K1002514','K1002515']
# cl_bussnisstype_name = ['两定机构月结支付','地税回盘实收到帐','地税回盘失败','统筹范围外医保基金转移','跨省异地清算','大额医疗保险费','中心报销','中心报销大额','异地清算扣款','月结算','跨省大额预付金','省内异地清算','跨省大额预付金上解','省内大额预付金','账户返还','年结算']


cl_bussnisstype_code = ['K10025','K10026']
cl_bussnisstype_name = ['两定机构月结支付','大额医疗保险费拨付']
# cl_bussnisstype_name = ['中心报销','支付计划']
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
otherStyleTime5 = now.strftime("%Y-%m")

def make_sql(country_code, n, bus_code):

    path = '../../Data_sql/支付计划/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'MID_PAY_PLAN'+str(otherStyleTime3)+'.sql'
    # file_name_item = path + 'MID_PAY_PLAN_ITEM'+str(otherStyleTime3)+'.sql'
    SMRTS_PAY_PLAN_file = open(file_name, 'w', encoding='utf-8')
    # SMRTS_PAY_PLAN_ITEM_file = open(file_name_item, 'w', encoding='utf-8')

    # 主子表sql
    str_head_zhu = "insert into MID_PAY_PLAN values ("
    str_head_item = "insert into MID_PAY_PLAN_ITEM values ("

    no = 1
    while (n > 0):
        # 主表
        p1 = otherStyleTime5
        p2 = '310'
        p3 = '城镇企业职工基本医疗保险'
        p4 = 'YW' + otherStyleTime4 + str(n)
        p5 = ''
        p6 = '00'
        p7 = '上海市统筹'
        p8 = country_code
        p9 = '上海市医保中心'
        # num = int(random.uniform(0, 2))
        # num = 1
        if bus_code == 'K10025':
            num = 0
        elif bus_code == 'K10026':
            num = 1
        p10 = cl_bussnisstype_code[num]
        p11 = cl_bussnisstype_name[num]

        p12 = '3'
        p13 = '6666.66'
        status = '0'
        AAD404 = ''
        AAD405 = ''
        AAD406 = ''

        # 子表
        s1 = '310'
        s2 = '城镇企业职工基本医疗保险'
        s3 = otherStyleTime5
        s100 = p4
        s4 = '00400001'
        s5 = '上海市支付计划往来单位001'

        s4_2 = '00400002'
        s5_2 = '上海市支付计划往来单位002'

        s4_3 = '00400003'
        s5_3 = '上海市支付计划往来单位003'

        s6 = '20310'
        s7 = '10310'
        s8 = '900'
        s9 = '18000'
        s10 = '1111.11'

        s10_2 = '2222.22'

        s10_3 = '3333.33'

        if bus_code == 'K10025':
            s11 = '12'
            s12 = '13'
            s13 = '14'
            s14 = '15'
            s15 = '16'
            s16 = '17'
            s17 = '18'
        elif bus_code == 'K10026':
            s11 = otherStyleTime2
            s12 = '1'
            s13 = '1'
            s14 = otherStyleTime5
            s15 = '张财务'
            s16 = '李业务'
            s17 = otherStyleTime5

        s18 = '19'
        s19 = '20'
        s20 = '21'
        s21 = '22'
        s22 = '23'
        s23 = '24'
        s24 = '25'
        s25 = '26'
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
        if bus_code == 'K10025':
            s45 = '事业'
            s46 = '测试1'
        elif bus_code == 'K10026':
            s45 = otherStyleTime5
            s46 = '王复核'

        status = '0'


        line = str_head_zhu + '"' + p1 + '", "' + p2 + '", "' + p3 + '", "' + p4 + '", "' + p5 + '", "' + p6 + '", "' + p7 + '", "' + p8 + '", "' + p9 + '", "' + p10 + '", "' + p11 + '", "' + p12 + '", "' + p13 + '", "' + status + '", "' + AAD404 + '", "' + AAD405 + '", "' + AAD406 + '");'

        line_item1 = str_head_item + '"' + s1 + '", "' + s2 + '", "' + s3 + '", "' + s4 + '", "' + s5 + '", "' + s6 + '", "' + s7 + '", "' + s8 + '", "' + s9 + '", "' + s10 + '", "' + s11 + '", "' + s12 + '", "' + s13 + '", "' + s14 + '", "' + s15 \
                     + '", "' + s16 + '", "' + s17 + '", "' + s18 + '", "' + s19 + '", "' + s20 + '", "' + s21 + '", "' + s22 + '", "' + s23 + '", "' + s24 + '", "' + s25 + '", "' + s26 + '", "' + s27 + '", "' + s28 + '", "' + s29 + '", "' + s30 + '", "' + s31\
                     + '", "' + s32 + '", "' + s33 + '", "' + s34 + '", "' + s35 + '", "' + s36 + '", "' + s37 + '", "' + s38 + '", "' + s39 + '", "' + s40 + '", "' + s41 + '", "' + s42 + '", "' + s43 + '", "' + s44 + '", "' + s45 + '", "' + s46 + '", "' + s100 + '", "' + status + '");'
        line_item2 = str_head_item + '"' + s1 + '", "' + s2 + '", "' + s3 + '", "' + s4_2 + '", "' + s5_2 + '", "' + s6 + '", "' + s7 + '", "' + s8 + '", "' + s9 + '", "' + s10_2 + '", "' + s11 + '", "' + s12 + '", "' + s13 + '", "' + s14 + '", "' + s15 \
                     + '", "' + s16 + '", "' + s17 + '", "' + s18 + '", "' + s19 + '", "' + s20 + '", "' + s21 + '", "' + s22 + '", "' + s23 + '", "' + s24 + '", "' + s25 + '", "' + s26 + '", "' + s27 + '", "' + s28 + '", "' + s29 + '", "' + s30 + '", "' + s31\
                     + '", "' + s32 + '", "' + s33 + '", "' + s34 + '", "' + s35 + '", "' + s36 + '", "' + s37 + '", "' + s38 + '", "' + s39 + '", "' + s40 + '", "' + s41 + '", "' + s42 + '", "' + s43 + '", "' + s44 + '", "' + s45 + '", "' + s46 + '", "' + s100 + '", "' + status + '");'
        line_item3 = str_head_item + '"' + s1 + '", "' + s2 + '", "' + s3 + '", "' + s4_3 + '", "' + s5_3 + '", "' + s6 + '", "' + s7 + '", "' + s8 + '", "' + s9 + '", "' + s10_3 + '", "' + s11 + '", "' + s12 + '", "' + s13 + '", "' + s14 + '", "' + s15 \
                     + '", "' + s16 + '", "' + s17 + '", "' + s18 + '", "' + s19 + '", "' + s20 + '", "' + s21 + '", "' + s22 + '", "' + s23 + '", "' + s24 + '", "' + s25 + '", "' + s26 + '", "' + s27 + '", "' + s28 + '", "' + s29 + '", "' + s30 + '", "' + s31\
                     + '", "' + s32 + '", "' + s33 + '", "' + s34 + '", "' + s35 + '", "' + s36 + '", "' + s37 + '", "' + s38 + '", "' + s39 + '", "' + s40 + '", "' + s41 + '", "' + s42 + '", "' + s43 + '", "' + s44 + '", "' + s45 + '", "' + s46 + '", "' + s100 + '", "' + status + '");'


        line = line.replace('\"', '\'')
        line_item1 = line_item1.replace('\"', '\'')
        line_item2 = line_item2.replace('\"', '\'')
        line_item3 = line_item3.replace('\"', '\'')
        no += 1
        n -= 1

        SMRTS_PAY_PLAN_file.write(line + '\n')
        SMRTS_PAY_PLAN_file.write(line_item1 + '\n')
        SMRTS_PAY_PLAN_file.write(line_item2 + '\n')
        SMRTS_PAY_PLAN_file.write(line_item3 + '\n')



if __name__ == '__main__':
    # 传参： country_code, n
    make_sql('00', 10,'K10026')


