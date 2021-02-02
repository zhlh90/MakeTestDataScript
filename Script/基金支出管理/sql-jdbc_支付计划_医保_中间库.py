# -*- coding: utf-8 -*
import datetime
import cx_Oracle
import random


# 业务类型
# cl_bussnisstype_code = ['K10025','K1002501','K1002502','K1002503','K1002504','K1002505','K1002506','K1002507','K1002508','K1002509','K1002510','K1002511','K1002512','K1002513','K1002514','K1002515']
# cl_bussnisstype_name = ['两定机构月结支付','地税回盘实收到帐','地税回盘失败','统筹范围外医保基金转移','跨省异地清算','大额医疗保险费','中心报销','中心报销大额','异地清算扣款','月结算','跨省大额预付金','省内异地清算','跨省大额预付金上解','省内大额预付金','账户返还','年结算']

# 经办机构
cl_agency_code = ['00','01','1300']
cl_agency_name = ['上海保险事业管理局','黄浦区保险事业管理局','河北省']
# 业务类型
cl_bussnisstype_code = ['K10025','K10026','K10025NJ']
cl_bussnisstype_name = ['两定机构月结支付','大额医疗保险费拨付','两定机构年结']
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
otherStyleTime6 = now.strftime("%Y%m")

def make_sql(agency_no,bus_no, n):

    starttime = datetime.datetime.now()
    db = cx_Oracle.connect('smifcmiddledb/1@10.10.66.159:1521/orcl')
    cr = db.cursor() #创建游标

    # 主子表sql
    str_head_zhu = "insert into MID_PAY_PLAN values ("
    str_head_item = "insert into MID_PAY_PLAN_ITEM values ("

    no = 1
    while (n > 0):
        # 主表
        P1 = otherStyleTime6
        P2 = '310'
        P3 = '城镇企业职工基本医疗保险'
        P4 = 'YW' + otherStyleTime3 + str(n)
        P5 = ''
        P6 = '00'
        P7 = '上海市统筹'
        P8 = cl_agency_code[agency_no]
        P9 = cl_agency_name[agency_no]
        # num = int(random.uniform(0, 2))
        P10 = cl_bussnisstype_code[bus_no]
        P11 = cl_bussnisstype_name[bus_no]

        P12 = '3'
        P13 = '6666.66'
        STATUS = '0'
        AAD404 = ''
        AAD405 = ''
        AAD406 = ''
        AAD407 = ''
        AAD408 =''
        AAD409 =''
        AAD410 =''
        AAD411 =''
        AAD412 =''
        AAD413 =''
        AAD414 =''
        AAD415 =''
        P23 = '325624'

        sqlG = " insert into MID_PAY_PLAN(P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, STATUS, AAD404, AAD405, AAD406, AAD407, AAD408, AAD409, AAD410, AAD411, AAD412, AAD413, AAD414, AAD415, P23)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27) "

        cr.execute(sqlG, (P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, STATUS, AAD404, AAD405, AAD406, AAD407, AAD408, AAD409, AAD410, AAD411, AAD412, AAD413, AAD414, AAD415, P23))

         # 子表
        S1 = '310'
        S2 = '城镇企业职工基本医疗保险'
        S3 = otherStyleTime6
        S100 = P4
        S4 = '00400001'
        S5 = '上海市支付计划往来单位001'

        S4_2 = '00400002'
        S5_2 = '上海市支付计划往来单位002'

        S4_3 = '00400003'
        S5_3 = '上海市支付计划往来单位003'

        S6 = '20310'
        S7 = '10310'
        S8 = '900'
        S9 = '18000'
        S10 = '1111.11'

        S10_2 = '2222.22'

        S10_3 = '3333.33'

        if P10 == 'K10025' or P10 == 'K10025NJ':
            S11 = '12'
            S12 = '13'
            S13 = '14'
            S14 = '15'
            S15 = '16'
            S16 = '17'
            S17 = '18'
        elif P10 == 'K10026':
            S11 = otherStyleTime2
            S12 = '1'
            S13 = '1'
            S14 = otherStyleTime5
            S15 = '张财务'
            S16 = '李业务'
            S17 = otherStyleTime5
        elif P10 == 'YS1':
            S11 = otherStyleTime2
            S12 = '1'
            S13 = '1'
            S14 = otherStyleTime5
            S15 = '张财务'
            S16 = '李业务'
            S17 = otherStyleTime5

        S18 = '19'
        S19 = '20'
        S20 = '21'
        S21 = '22'
        S22 = '23'
        S23 = '24'
        S24 = '25'
        S25 = '26'
        S26 = '27'
        S27 = '28'
        S28 = '29'
        S29 = '30'
        S30 = '31'
        S31 = '32'
        S32 = '33'
        S33 = '34'
        S34 = '35'
        S35 = '36'
        S36 = '37'
        S37 = '38'
        S38 = '39'
        S39 = '40'
        S40 = '41'
        S41 = '42'
        S42 = '43'
        S43 = '44'
        S44 = '45'
        if P10 == 'K10025' or P10 == 'K10025NJ':
            S45 = '事业'
            S46 = '测试1'
        elif P10 == 'K10026':
            S45 = otherStyleTime5
            S46 = '王复核'
        elif P10 == 'YS1':
            S45 = otherStyleTime5
            S46 = '王复核'

        STATUS = '0'
        S81 = ''
        S82 = ''
        S83 = ''
        S84 = ''
        S85 = ''
        S86 = ''
        S87 = ''
        S88 = ''
        AGENCY_CODE =cl_agency_code[agency_no]
        AGENCY_NAME =cl_agency_name[agency_no]


        sqlZ1 = " insert into MID_PAY_PLAN_ITEM(S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, S36, S37, S38, S39, S40, S41, S42, S43, S44, S45, S46, S100, STATUS, S81, S82, S83, S84, S85, S86, S87, S88, AGENCY_CODE, AGENCY_NAME)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49,:50,:51,:52,:53,:54,:55,:56,:57,:58) "

        cr.execute(sqlZ1, (S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, S36, S37, S38, S39, S40, S41, S42, S43, S44, S45, S46, S100, STATUS, S81, S82, S83, S84, S85, S86, S87, S88, AGENCY_CODE, AGENCY_NAME))

        cr.execute(sqlZ1, (S1, S2, S3, S4_2, S5_2, S6, S7, S8, S9, S10_2, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, S36, S37, S38, S39, S40, S41, S42, S43, S44, S45, S46, S100, STATUS, S81, S82, S83, S84, S85, S86, S87, S88, AGENCY_CODE, AGENCY_NAME))

        cr.execute(sqlZ1, (S1, S2, S3, S4_3, S5_3, S6, S7, S8, S9, S10_3, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, S36, S37, S38, S39, S40, S41, S42, S43, S44, S45, S46, S100, STATUS, S81, S82, S83, S84, S85, S86, S87, S88, AGENCY_CODE, AGENCY_NAME))

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
    # 传参： country_code, n
    # 第一参数：0-上海 1-黄埔，2-河北省
    # 第二参数：0-K10025 1-K10026 2-K10025NJ
    make_sql(0,0, 5)


