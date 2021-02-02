# -*- coding: utf-8 -*
import datetime

# import pandas as pd
import random
import os

# 业务类型
cl_bussnisstype_code = ['DYZF',]
cl_bussnisstype_name = ['待遇支付']

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

def make_sql(country_code, n):

    path = '../../Data_sql/支付计划/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + '待遇支付中间表'+str(otherStyleTime3)+'.sql'
    # file_name_item = path + 'MID_PAY_PLAN_ITEM'+str(otherStyleTime3)+'.sql'
    SMRTS_PAY_PLAN_file = open(file_name, 'w', encoding='utf-8')
    # SMRTS_PAY_PLAN_ITEM_file = open(file_name_item, 'w', encoding='utf-8')

    # 主子表sql
    str_head_zhu = "insert into AD61 values ("
    str_head_item = "insert into AD41 values ("

    no = 1
    while (n > 0):
        # 主表

        AAZ802 = otherStyleTime4 + str(n)
        AAE140 = '110'
        AAE002 = otherStyleTime5
        AAD015 = '1'
        num = 0
        AAD020 = cl_bussnisstype_code[num]
        AAD021 = AAZ802
        AAD022 = AAZ802
        AAA033 = '1'
        AAZ010 = '1'
        AAZ999 = '1'
        AAE069 = '1'
        AAB001 = '999'
        AAD027 = '33.33'
        AAD076 = '2'
        AAD145 = '1'
        AAF200 = '313'
        AAB012 = '上海银行'

        AAE009 = '上海市待遇支付往来单位001'
        AAE010 = '12345678901234567001'
        if country_code == '130102':
            AAE009 = '长安区待遇支付往来单位001'
            AAE010 = '1301020011234567890'

        AAD051 = '合肥市'
        AAD052 = '合肥市'
        AAD050 = '123456123456'
        AAD030 = '摘要1'
        AAD023 = '1'
        AAD026 = '1'
        AAB191 = otherStyleTime3
        BAZ002 = '1'
        BZE011 = '创建人1'
        BZE036 = otherStyleTime3
        BZE034 = country_code
        AAE011 = '经办人1'
        AAE036 = otherStyleTime3
        AAB034 = country_code
        AAA027 = '13'
        AAD032 = 'qweqwe'
        AAD033 = '11'
        AAD028 = '123456789'
        AAD029 = '1234567890'
        BZE300 = '123141242'
        AAD825 = '11'
        AAD081 = '123'
        AAD082 = '123'
        AAD083 = '123'
        AAE100 = '1'
        AAD087 = ''
        AAD089 = '11'
        AAD090 = '1'
        AAD086 = '1'
        AAD091 = '1'
        AAD092 = '1'
        AAD094 = country_code
        STATUS = '0'

        # 子表-one
        o_AAZ807 = AAZ802
        o_AAE140 = '110'
        o_AAE002 = AAE002
        o_AAD015 = '1'
        o_AAD020 = 'DYZF'
        o_AAD048 = 'DYZF01'
        o_AAD021 = AAZ802
        o_AAD022 = AAZ802
        o_AAA033 = '1'
        o_AAZ010 = ran_strx("0123456789", 8)
        o_AAE069 = 'sdyfsu'
        o_AAB001 = '999'
        o_AAD027 = '11.11'
        o_AAC058 = '1'
        o_AAC147 = ran_strx("0123456789", 20)
        o_AAD145 = '1'
        o_AAF200 = '313'
        o_AAB012 = '上海银行'

        o_AAE009 = '上海市待遇支付往来单位001'
        o_AAE010 = '12345678901234567001'
        if country_code == '130102':
            o_AAE009 = '长安区待遇支付往来单位001'
            o_AAE010 = '1301020011234567890'

        o_AAD051 = '合肥市'
        o_AAD052 = '合肥市'
        o_AAD050 = '123456124356'
        o_AAD030 = '摘要1'
        o_AAD059 = ran_strx("0123456789", 11)
        o_AAZ802 = '113421'
        o_BAZ002 = '132'
        o_BZE011 = '创建人1'
        o_BZE036 = otherStyleTime3
        o_BZE034 = '00'
        o_AAE011 = '经办人1'
        o_AAE036 = otherStyleTime3
        o_AAB034 = '00'
        o_AAA027 = '00'
        o_BZE300 = ran_strx("0123456789", 8)
        o_AAD023 = '1'
        o_AAZ999 = '1'
        o_AAZ001 = ran_strx("0123456789", 16)
        o_AAD825 = '1'
        o_AAD094 = '01'
        o_AAB019 = '10'

        t_AAZ807 = AAZ802
        t_AAE140 = '110'
        t_AAE002 = AAE002
        t_AAD015 = '1'
        t_AAD020 = 'DYZF'
        t_AAD048 = 'DYZF02'
        t_AAD021 = AAZ802
        t_AAD022 = AAZ802
        t_AAA033 = '1'
        t_AAZ010 = ran_strx("0123456789", 8)
        t_AAE069 = 'sdyfsu'
        t_AAB001 = '998'
        t_AAD027 = '22.22'
        t_AAC058 = '1'
        t_AAC147 = ran_strx("0123456789", 20)
        t_AAD145 = '1'
        t_AAF200 = '313'
        t_AAB012 = '上海银行'

        t_AAE009 = '上海市待遇支付往来单位002'
        t_AAE010 = '12345678901234567002'
        if country_code == '130102':
            t_AAE009 = '长安区待遇支付往来单位002'
            t_AAE010 = '13010202123456789002'

        t_AAD051 = '安徽省'
        t_AAD052 = '安徽省'
        t_AAD050 = '123456124356'
        t_AAD030 = '摘要1'
        t_AAD059 = ran_strx("0123456789", 11)
        t_AAZ802 = '113421'
        t_BAZ002 = '132'
        t_BZE011 = '创建人2'
        t_BZE036 = otherStyleTime3
        t_BZE034 = '00'
        t_AAE011 = '经办人2'
        t_AAE036 = otherStyleTime3
        t_AAB034 = '00'
        t_AAA027 = '00'
        t_BZE300 = ran_strx("0123456789", 8)
        t_AAD023 = '1'
        t_AAZ999 = '1'
        t_AAZ001 = ran_strx("0123456789", 16)
        t_AAD825 = '1'
        t_AAD094 = '01'
        t_AAB019 = '10'




        line = str_head_zhu + '"' + AAZ802 + '", "' + AAE140 + '", "' + AAE002 + '", "' + AAD015 + '", "' + AAD020 + '", "' + AAD021 + '", "' + AAD022 + '", "' + AAA033 + '", "' + AAZ010 + '", "' + AAZ999 + '", "' + AAE069 + '", "' + AAB001 + '", "' + AAD027 + '", "' + AAD076 + '", "' + AAD145 + '", "' + AAF200 + '", "' + AAB012 + '", "' + AAE009 + '", "' + AAE010 + '", "' + AAD051 + '", "' + AAD052 + '", "' + AAD050 + '", "' + AAD030 + '", "' + AAD023 + '", "' + AAD026 + '", "' + AAB191 + '", "' + BAZ002 + '", "' + BZE011 + '", "' + BZE036 + '", "' + BZE034 + '", "' + AAE011 + '", "' + AAE036 + '", "' + AAB034 + '", "' + AAA027 + '", "' + AAD032 + '", "' + AAD033 + '", "' + AAD028 + '", "' + AAD029 + '", "' + BZE300 + '", "' + AAD825 + '", "' + AAD081 + '", "' + AAD082 + '", "' + AAD083 + '", "' + AAE100 + '", "' + AAD087 + '", "' + AAD089 + '", "' + AAD090 + '", "' + AAD086 + '", "' + AAD091 + '", "' + AAD092 + '", "' + AAD094 + '", "' + STATUS + '");'

        line_item1 = str_head_item + '"' + o_AAZ807 + '", "' + o_AAE140 + '", "' + o_AAE002 + '", "' + o_AAD015 + '", "' + o_AAD020 + '", "' + o_AAD048 + '", "' + o_AAD021 + '", "' + o_AAD022 + '", "' + o_AAA033 + '", "' + o_AAZ010 + '", "' + o_AAE069 + '", "' + o_AAB001 + '", "' + o_AAD027 + '", "' + o_AAC058 + '", "' + o_AAC147 + '", "' + o_AAD145 + '", "' + o_AAF200 + '", "' + o_AAB012 + '", "' + o_AAE009 + '", "' + o_AAE010 + '", "' + o_AAD051 + '", "' + o_AAD052 + '", "' + o_AAD050 + '", "' + o_AAD030 + '", "' + o_AAD059 + '", "' + o_AAZ802 + '", "' + o_BAZ002 + '", "' + o_BZE011 + '", "' + o_BZE036 + '", "' + o_BZE034 + '", "' + o_AAE011 + '", "' + o_AAE036 + '", "' + o_AAB034 + '", "' + o_AAA027 + '", "' + o_BZE300 + '", "' + o_AAD023 + '", "' + o_AAZ999 + '", "' + o_AAZ001 + '", "' + o_AAD825 + '", "' + o_AAD094 + '", "' + o_AAB019 + '");'
        line_item2 = str_head_item + '"' + t_AAZ807 + '", "' + t_AAE140 + '", "' + t_AAE002 + '", "' + t_AAD015 + '", "' + t_AAD020 + '", "' + t_AAD048 + '", "' + t_AAD021 + '", "' + t_AAD022 + '", "' + t_AAA033 + '", "' + t_AAZ010 + '", "' + t_AAE069 + '", "' + t_AAB001 + '", "' + t_AAD027 + '", "' + t_AAC058 + '", "' + t_AAC147 + '", "' + t_AAD145 + '", "' + t_AAF200 + '", "' + t_AAB012 + '", "' + t_AAE009 + '", "' + t_AAE010 + '", "' + t_AAD051 + '", "' + t_AAD052 + '", "' + t_AAD050 + '", "' + t_AAD030 + '", "' + t_AAD059 + '", "' + t_AAZ802 + '", "' + t_BAZ002 + '", "' + t_BZE011 + '", "' + t_BZE036 + '", "' + t_BZE034 + '", "' + t_AAE011 + '", "' + t_AAE036 + '", "' + t_AAB034 + '", "' + t_AAA027 + '", "' + t_BZE300 + '", "' + t_AAD023 + '", "' + t_AAZ999 + '", "' + t_AAZ001 + '", "' + t_AAD825 + '", "' + t_AAD094 + '", "' + t_AAB019 + '");'

        line = line.replace('\"', '\'')
        line_item1 = line_item1.replace('\"', '\'')
        line_item2 = line_item2.replace('\"', '\'')

        no += 1
        n -= 1

        SMRTS_PAY_PLAN_file.write(line + '\n')
        SMRTS_PAY_PLAN_file.write(line_item1 + '\n')
        SMRTS_PAY_PLAN_file.write(line_item2 + '\n')



if __name__ == '__main__':
    # 传参： country_code, n
    #长安区
    # make_sql('130102', 10)
    #上海市中心
    make_sql('34010001', 1)


