# -*- coding: utf-8 -*
import datetime
import cx_Oracle
import random

# 业务类型
cl_bussnisstype_code = ['DYZF',]
cl_bussnisstype_name = ['待遇支付']
# 统筹区
cl_country_code = ['00','130000','34000001']
cl_country_name = ['上海市统筹','河北省统筹','安徽省统筹']
# 经办机构
cl_agency_code = ['00','130002','34000001']
cl_agency_name = ['上海保险事业管理局','河北省','安徽省事业保险局']
# 行政区划
cl_org_code = ['310000','130000','34000001']
cl_org_name = ['上海市','河北省','安徽省']
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
    starttime = datetime.datetime.now()
    db = cx_Oracle.connect('smifcmiddledb/1@10.10.66.159:1521/orcl')
    cr = db.cursor() #创建游标

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
        AAB001 = '1122331'
        AAD027 = '33.33'
        AAD076 = '2'
        AAD145 = '1'
        AAF200 = '313'
        AAB012 = '上海银行'

        if cl_agency_code[country_code] == '130102':
            AAE009 = '上海市待遇支付往来单位001'
            AAE010 = '12345678901234567001'
        elif cl_agency_code[country_code] == '130102':
            AAE009 = '长安区待遇支付往来单位001'
            AAE010 = '1301020011234567890'
        else:
            AAE009 = '安徽待遇支付往来单位001'
            AAE010 = '1301020011234567890'

        AAD051 = cl_org_name[country_code]
        AAD052 = cl_org_name[country_code]
        AAD050 = '123456123456'
        AAD030 = '摘要1'
        AAD023 = '1'
        AAD026 = '1'
        AAB191 = otherStyleTime3
        BAZ002 = '1'
        BZE011 = '创建人1'
        BZE036 = otherStyleTime3
        BZE034 = cl_agency_code[country_code]
        AAE011 = '经办人1'
        AAE036 = otherStyleTime3
        AAB034 = cl_agency_code[country_code]
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
        AAD094 = cl_agency_code[country_code]
        STATUS = '0'
        P14 = '000'
        P23 = '325624'

        sqlG = " insert into AD61(AAZ802, AAE140, AAE002, AAD015, AAD020, AAD021, AAD022, AAA033, AAZ010, AAZ999, AAE069, AAB001, AAD027, AAD076, AAD145, AAF200, AAB012, AAE009, AAE010, AAD051, AAD052, AAD050, AAD030, AAD023, AAD026, AAB191, BAZ002, BZE011, BZE036, BZE034, AAE011, AAE036, AAB034, AAA027, AAD032, AAD033, AAD028, AAD029, BZE300, AAD825, AAD081, AAD082, AAD083, AAE100, AAD087, AAD089, AAD090, AAD086, AAD091, AAD092, AAD094, STATUS, P14, P23)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49,:50,:51,:52,:53,:54) "

        cr.execute(sqlG, (AAZ802, AAE140, AAE002, AAD015, AAD020, AAD021, AAD022, AAA033, AAZ010, AAZ999, AAE069, AAB001, AAD027, AAD076, AAD145, AAF200, AAB012, AAE009, AAE010, AAD051, AAD052, AAD050, AAD030, AAD023, AAD026, AAB191, BAZ002, BZE011, BZE036, BZE034, AAE011, AAE036, AAB034, AAA027, AAD032, AAD033, AAD028, AAD029, BZE300, AAD825, AAD081, AAD082, AAD083, AAE100, AAD087, AAD089, AAD090, AAD086, AAD091, AAD092, AAD094, STATUS, P14, P23))
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
        o_AAB001 = '1122331'
        o_AAD027 = '11.11'
        o_AAC058 = '1'
        o_AAC147 = ran_strx("0123456789", 20)
        o_AAD145 = '1'
        o_AAF200 = '313'
        o_AAB012 = '上海银行'

        if cl_agency_code[country_code] == '00':
            o_AAE009 = '上海市待遇支付往来单位001'
            o_AAE010 = '12345678901234567001'
        elif cl_agency_code[country_code] == '130102':
            o_AAE009 = '长安区待遇支付往来单位001'
            o_AAE010 = '1301020011234567890'
        else:
            o_AAE009 = '安徽待遇支付往来单位001'
            o_AAE010 = '1301020011234567890'


        o_AAD051 = cl_org_name[country_code]
        o_AAD052 = cl_org_name[country_code]
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
        o_S81 = ran_strx("0123456789", 15)
        o_S82 = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        o_S83 = '313'
        o_S84 = '上海银行'
        o_S85 = '00'
        o_S86 = '上海区县'
        o_S87 = '123456123456'
        o_S88 = '325462'
        sqlG1 = " insert into AD41(AAZ807, AAE140, AAE002, AAD015, AAD020, AAD048, AAD021, AAD022, AAA033, AAZ010, AAE069, AAB001, AAD027, AAC058, AAC147, AAD145, AAF200, AAB012, AAE009, AAE010, AAD051, AAD052, AAD050, AAD030, AAD059, AAZ802, BAZ002, BZE011, BZE036, BZE034, AAE011, AAE036, AAB034, AAA027, BZE300, AAD023, AAZ999, AAZ001, AAD825, AAD094, AAB019, S81, S82, S83, S84, S85, S86, S87, S88)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49) "
        cr.execute(sqlG1, (o_AAZ807, o_AAE140, o_AAE002, o_AAD015, o_AAD020, o_AAD048, o_AAD021, o_AAD022, o_AAA033, o_AAZ010, o_AAE069, o_AAB001, o_AAD027, o_AAC058, o_AAC147, o_AAD145, o_AAF200, o_AAB012, o_AAE009, o_AAE010, o_AAD051, o_AAD052, o_AAD050, o_AAD030, o_AAD059, o_AAZ802, o_BAZ002, o_BZE011, o_BZE036, o_BZE034, o_AAE011, o_AAE036, o_AAB034, o_AAA027, o_BZE300, o_AAD023, o_AAZ999, o_AAZ001, o_AAD825, o_AAD094, o_AAB019, o_S81, o_S82, o_S83, o_S84, o_S85, o_S86, o_S87, o_S88))

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
        t_AAB001 = '1122332'
        t_AAD027 = '22.22'
        t_AAC058 = '1'
        t_AAC147 = ran_strx("0123456789", 20)
        t_AAD145 = '1'
        t_AAF200 = '313'
        t_AAB012 = '上海银行'

        if cl_agency_code[country_code] == '00':
            t_AAE009 = '上海市待遇支付往来单位001'
            t_AAE010 = '12345678901234567001'
        elif cl_agency_code[country_code] == '130102':
            t_AAE009 = '长安区待遇支付往来单位001'
            t_AAE010 = '1301020011234567890'
        else:
            t_AAE009 = '安徽待遇支付往来单位001'
            t_AAE010 = '1301020011234567890'

        t_AAD051 = cl_org_name[country_code]
        t_AAD052 = cl_org_name[country_code]
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
        t_S81 = ran_strx("0123456789", 15)
        t_S82 = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        t_S83 = '313'
        t_S84 = '上海银行'
        t_S85 = '00'
        t_S86 = '上海区县'
        t_S87 = '123456123456'
        t_S88 = '34235243'

        sqlG2 = " insert into AD41(AAZ807, AAE140, AAE002, AAD015, AAD020, AAD048, AAD021, AAD022, AAA033, AAZ010, AAE069, AAB001, AAD027, AAC058, AAC147, AAD145, AAF200, AAB012, AAE009, AAE010, AAD051, AAD052, AAD050, AAD030, AAD059, AAZ802, BAZ002, BZE011, BZE036, BZE034, AAE011, AAE036, AAB034, AAA027, BZE300, AAD023, AAZ999, AAZ001, AAD825, AAD094, AAB019, S81, S82, S83, S84, S85, S86, S87, S88)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49) "
        cr.execute(sqlG2, (t_AAZ807, t_AAE140, t_AAE002, t_AAD015, t_AAD020, t_AAD048, t_AAD021, t_AAD022, t_AAA033, t_AAZ010, t_AAE069, t_AAB001, t_AAD027, t_AAC058, t_AAC147, t_AAD145, t_AAF200, t_AAB012, t_AAE009, t_AAE010, t_AAD051, t_AAD052, t_AAD050, t_AAD030, t_AAD059, t_AAZ802, t_BAZ002, t_BZE011, t_BZE036, t_BZE034, t_AAE011, t_AAE036, t_AAB034, t_AAA027, t_BZE300, t_AAD023, t_AAZ999, t_AAZ001, t_AAD825, t_AAD094, t_AAB019, t_S81, t_S82, t_S83, t_S84, t_S85, t_S86, t_S87, t_S88))

        no += 1
        n -= 1

    cr.close()
    db.commit()
    db.close()
    endtime = datetime.datetime.now()
    print("耗时H：" + str(round((endtime - starttime).seconds / 3600, 2)))



if __name__ == '__main__':
    # 传参： country_code, n
    # 0-上海
    # 1-河北
    # 2-安徽
    make_sql(0, 1)


