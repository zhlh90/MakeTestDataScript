# -*- coding: utf-8 -*
import datetime
import cx_Oracle
import random
from faker import Faker, Factory

# 业务类型
from Script import shenfenzhenghao

cl_bussnisstype_code = ['DYZFZZS']
cl_bussnisstype_name = ['待遇支付主子孙']
# 统筹区
cl_country_code = ['00','130000','34000001','34000001']
cl_country_name = ['上海市统筹','河北省统筹','安徽省统筹','安徽省统筹']
# 经办机构
cl_agency_code = ['00','1300','34000001','34010001']
cl_agency_name = ['上海保险事业管理局','河北省','安徽省事业保险局','合肥市事业保险局']
# 行政区划
cl_org_code = ['310000','130000','34000001','34000001']
cl_org_name = ['上海市','河北省','安徽省','安徽省']
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
otherStyleTime6 = now.strftime("%Y%m")
# 年结后日期
# tim = datetime.datetime.fromisoformat('2021-01-01 01:01:11')
# #转换为指定的格式:
# otherStyleTime = tim.strftime("%Y-%m-%d %H:%M:%S")
# otherStyleTime1 = tim.strftime("%Y%m%d%H")
# otherStyleTime2 = tim.strftime("%Y-%m-%d")
# otherStyleTime3 = tim.strftime("%Y%m%d%H%M%S")
# otherStyleTime4 = tim.strftime("%Y%m%d%H%M")
# otherStyleTime5 = tim.strftime("%Y-%m")
# otherStyleTime6 = tim.strftime("%Y%m")

def make_sql(country_code, n):
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
        # 主表

        P1 = otherStyleTime5
        INSURANCE_CODE = '110'
        INSURANCE_NAME = '城镇企业职工基本养老保险'
        P4 = 'YW' + otherStyleTime3 + str(n)
        P5 = ''
        P6 = cl_country_code[country_code]
        P7 = cl_country_name[country_code]
        AGENCY_CODE = cl_agency_code[country_code]
        AGENCY_NAME = cl_agency_name[country_code]
        P10 = cl_bussnisstype_code[0]
        P11 = cl_bussnisstype_name[0]
        P12 = '2'
        P13 = '2000.00'
        # 代发户银行编码
        P14 = '000'
        P15 = otherStyleTime
        P16 = '1'
        P17 = cl_org_code[country_code]
        # P18 = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        P18 = fake_cn.name()
        P19 = otherStyleTime
        status = ''
        P23 = P4

        sqlG = " insert into MID_PAY_PLAN_OLD(P1, INSURANCE_CODE, INSURANCE_NAME, P4, P5, P6, P7, AGENCY_CODE, AGENCY_NAME, P10, P11, P12, P13, P14, P15,  P16, P17, P18, P19, status, P23)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21) "
        cr.execute(sqlG, (P1, INSURANCE_CODE, INSURANCE_NAME, P4, P5, P6, P7, AGENCY_CODE, AGENCY_NAME, P10, P11, P12, P13, P14, P15,  P16, P17, P18, P19, status, P23))

        # 子表-one
        o_INSURANCE_CODE = '110'
        o_INSURANCE_NAME = '城镇企业职工基本养老保险'
        o_S3 = otherStyleTime6
        o_S4 = fake2.random_number(4)
        o_S5 = fake_cn.company()
        o_S6 = otherStyleTime6
        o_S7 = '01'
        # 身份证
        o_S8 = fake_cn.ssn(min_age=16, max_age=90)
        o_S9 = '2'
        o_S10 = '1200.00'
        o_S11 = ran_strx("0123456789", 10)
        o_S12 = ran_strx("0123456789", 15)
        o_S13 = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        o_S14 = otherStyleTime
        o_S15 = otherStyleTime2
        o_S16 = '银行返回结果失败'
        o_S17 = '银行附言：收到款项'
        o_S18 = '1'
        o_S19 = otherStyleTime3 + str(n)+'01'
        o_S100 = P4
        o_status = ''
        o_S81 = ran_strx("0123456789", 15)
        o_S82 = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        o_S83 = '313'
        o_S84 = '上海银行'
        o_S85 = '00'
        o_S86 = '上海区县'
        o_S87 = '123456123456'
        o_S88 = '01'+P4
        AGENCY_CODE =cl_agency_code[country_code]
        AGENCY_NAME =cl_agency_name[country_code]

        sqlo = " insert into MID_PAY_PLAN_DETAIL_OLD(INSURANCE_CODE, INSURANCE_NAME, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S100, status, S81, S82, S83, S84, S85, S86, S87, S88, AGENCY_CODE, AGENCY_NAME)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31) "
        cr.execute(sqlo, (o_INSURANCE_CODE, o_INSURANCE_NAME, o_S3, o_S4, o_S5, o_S6, o_S7, o_S8, o_S9, o_S10, o_S11, o_S12, o_S13, o_S14, o_S15, o_S16, o_S17, o_S18, o_S19, o_S100, o_status, o_S81, o_S82, o_S83, o_S84, o_S85, o_S86, o_S87, o_S88, AGENCY_CODE, AGENCY_NAME))

        t_INSURANCE_CODE = '110'
        t_INSURANCE_NAME = '城镇企业职工基本养老保险'
        t_S3 = otherStyleTime6
        t_S4 = fake2.random_number(4)
        t_S5 = fake_cn.company()
        t_S6 = otherStyleTime6
        t_S7 = '01'
        t_S8 = fake_cn.ssn(min_age=16, max_age=90)
        t_S9 = '2'
        t_S10 = '800.00'
        t_S11 = ran_strx("0123456789", 10)
        t_S12 = ran_strx("0123456789", 15)
        t_S13 = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        t_S14 = otherStyleTime
        t_S15 = otherStyleTime2
        t_S16 = '银行返回结果失败'
        t_S17 = '银行附言：收到款项'
        t_S18 = '1'
        t_S19 = otherStyleTime3 + str(n)+'02'
        t_S100 = P4
        t_status = ''
        t_S81 = ran_strx("0123456789", 15)
        t_S82 = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        t_S83 = '313'
        t_S84 = '上海银行'
        t_S85 = '00'
        t_S86 = '上海区县'
        t_S87 = '123456123456'
        t_S88 = '02'+P4
        AGENCY_CODE =cl_agency_code[country_code]
        AGENCY_NAME =cl_agency_name[country_code]

        sqlt = " insert into MID_PAY_PLAN_DETAIL_OLD(INSURANCE_CODE, INSURANCE_NAME, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S100, status, S81, S82, S83, S84, S85, S86, S87, S88, AGENCY_CODE, AGENCY_NAME)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31) "
        cr.execute(sqlt, (t_INSURANCE_CODE, t_INSURANCE_NAME, t_S3, t_S4, t_S5, t_S6, t_S7, t_S8, t_S9, t_S10, t_S11, t_S12, t_S13, t_S14, t_S15, t_S16, t_S17, t_S18, t_S19, t_S100, t_status, t_S81, t_S82, t_S83, t_S84, t_S85, t_S86, t_S87, t_S88, AGENCY_CODE, AGENCY_NAME))

        # 孙表-one
        oo_AAZ220 = o_S19
        oo_AAA036 = '1002133'
        oo_AAA037 = '养老金'
        oo_AAA085 = '1'
        oo_AAA088 = '1'
        oo_AAE002 = otherStyleTime2
        oo_AAE003 = otherStyleTime2
        oo_AAE019 = '600.00'
        oo_BIE505 = '1'
        oo_BIE504 = otherStyleTime
        oo_BIE506 = 'CX'+otherStyleTime4+str(n)
        oo_YW001 = ''
        oo_YW002 = ''
        oo_YW003 = ''
        oo_YW004 = ''
        oo_YW005 = ''
        oo_status = ''
        sqloo = " insert into MID_PAY_PLAN_ITEM_OLD(AAZ220, AAA036, AAA037, AAA085, AAA088, AAE002, AAE003, AAE019, BIE505, BIE504, BIE506, YW001, YW002, YW003, YW004, YW005, status)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17) "
        cr.execute(sqloo, (oo_AAZ220, oo_AAA036, oo_AAA037, oo_AAA085, oo_AAA088, oo_AAE002, oo_AAE003, oo_AAE019, oo_BIE505, oo_BIE504, oo_BIE506, oo_YW001, oo_YW002, oo_YW003, oo_YW004, oo_YW005, oo_status))

        ot_AAZ220 = o_S19
        ot_AAA036 = '1002134'
        ot_AAA037 = '离休金'
        ot_AAA085 = '1'
        ot_AAA088 = '1'
        ot_AAE002 = otherStyleTime2
        ot_AAE003 = otherStyleTime2
        ot_AAE019 = '600.00'
        ot_BIE505 = '1'
        ot_BIE504 = otherStyleTime
        ot_BIE506 = 'CX'+otherStyleTime4+str(n)
        ot_YW001 = ''
        ot_YW002 = ''
        ot_YW003 = ''
        ot_YW004 = ''
        ot_YW005 = ''
        ot_status = ''
        sqlot = " insert into MID_PAY_PLAN_ITEM_OLD(AAZ220, AAA036, AAA037, AAA085, AAA088, AAE002, AAE003, AAE019, BIE505, BIE504, BIE506, YW001, YW002, YW003, YW004, YW005, status)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17) "
        cr.execute(sqlot, (ot_AAZ220, ot_AAA036, ot_AAA037, ot_AAA085, ot_AAA088, ot_AAE002, ot_AAE003, ot_AAE019, ot_BIE505, ot_BIE504, ot_BIE506, ot_YW001, ot_YW002, ot_YW003, ot_YW004, ot_YW005, ot_status))


        to_AAZ220 = t_S19
        to_AAA036 = '1002133'
        to_AAA037 = '养老金'
        to_AAA085 = '1'
        to_AAA088 = '1'
        to_AAE002 = otherStyleTime2
        to_AAE003 = otherStyleTime2
        to_AAE019 = '400.00'
        to_BIE505 = '1'
        to_BIE504 = otherStyleTime
        to_BIE506 = 'CX'+otherStyleTime4+str(n)
        to_YW001 = ''
        to_YW002 = ''
        to_YW003 = ''
        to_YW004 = ''
        to_YW005 = ''
        to_status = ''
        sqlto = " insert into MID_PAY_PLAN_ITEM_OLD(AAZ220, AAA036, AAA037, AAA085, AAA088, AAE002, AAE003, AAE019, BIE505, BIE504, BIE506, YW001, YW002, YW003, YW004, YW005, status)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17) "
        cr.execute(sqlto, (to_AAZ220, to_AAA036, to_AAA037, to_AAA085, to_AAA088, to_AAE002, to_AAE003, to_AAE019, to_BIE505, to_BIE504, to_BIE506, to_YW001, to_YW002, to_YW003, to_YW004, to_YW005, to_status))


        tt_AAZ220 = t_S19
        tt_AAA036 = '1002134'
        tt_AAA037 = '离休金'
        tt_AAA085 = '1'
        tt_AAA088 = '1'
        tt_AAE002 = otherStyleTime2
        tt_AAE003 = otherStyleTime2
        tt_AAE019 = '400.00'
        tt_BIE505 = '1'
        tt_BIE504 = otherStyleTime
        tt_BIE506 = 'CX'+otherStyleTime4+str(n)
        tt_YW001 = ''
        tt_YW002 = ''
        tt_YW003 = ''
        tt_YW004 = ''
        tt_YW005 = ''
        tt_status = ''
        sqltt = " insert into MID_PAY_PLAN_ITEM_OLD(AAZ220, AAA036, AAA037, AAA085, AAA088, AAE002, AAE003, AAE019, BIE505, BIE504, BIE506, YW001, YW002, YW003, YW004, YW005, status)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17) "
        cr.execute(sqltt, (tt_AAZ220, tt_AAA036, tt_AAA037, tt_AAA085, tt_AAA088, tt_AAE002, tt_AAE003, tt_AAE019, tt_BIE505, tt_BIE504, tt_BIE506, tt_YW001, tt_YW002, tt_YW003, tt_YW004, tt_YW005, tt_status))

        no += 1
        n -= 1
    cr.close()
    db.commit()
    db.close()
    endtime = datetime.datetime.now()
    print("耗时H：" + str(round((endtime - starttime).seconds / 3600, 2)))

if __name__ == '__main__':
    # 传参： country_code, n
    #长安区
    # make_sql('130102', 10)
    #上海市中心
    # cl_agency_code = ['00','1300','34000001','34010001']
    # cl_agency_name = ['上海保险事业管理局','河北省','安徽省事业保险局','合肥市事业保险局']
    make_sql(3, 1)


