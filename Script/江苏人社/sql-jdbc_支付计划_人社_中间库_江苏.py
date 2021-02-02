# -*- coding: utf-8 -*
import datetime
import cx_Oracle
import random


# 统筹区
cl_country_code = ['00','130000','34000001']
cl_country_name = ['上海市统筹','河北省统筹','安徽省统筹']
# 经办机构
cl_agency_code = ['00','130002','34000001']
cl_agency_name = ['上海保险事业管理局','河北省','安徽省事业保险局']
# 行政区划
cl_org_code = ['310000','130000','34000001']
cl_org_name = ['上海市','河北省','安徽省']
# 业务类型
cl_bussnisstype_code = ['DYZF']
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

def make_sql(country_code,bus_no, n):

    starttime = datetime.datetime.now()
    db = cx_Oracle.connect('smifcmiddledb/1@10.10.66.159:1521/orcl')
    cr = db.cursor() #创建游标

    # 主子表sql
    str_head_zhu = "insert into MID_PAY_PLAN values ("
    str_head_item = "insert into MID_PAY_PLAN_ITEM values ("

    no = 1
    while (n > 0):
        # 主表
        P1 = otherStyleTime5
        P2 = '110'
        P3 = '城镇企业职工基本养老保险'
        P4 = 'YW' + otherStyleTime4 + str(n)
        P5 = 'YW'+P4
        P6 = '00'
        P7 = '上海市统筹'
        P8 = cl_agency_code[country_code]
        P9 = cl_agency_name[country_code]
        # num = int(random.uniform(0, 2))
        P10 = cl_bussnisstype_code[bus_no]
        P11 = cl_bussnisstype_name[bus_no]

        P12 = '2'
        P13 = '3333.33'
        STATUS = '0'
        P23 = P4
        P14 = '000'
        P15 = '社保银行'
        PAY_MARK = ''
        PAY_TIME = ''
        RECIP_BANK_NO = ''
        RECIP_ACC = ''
        RECIP_NAME = ''
        FAIL_CONFIRM = ''
        FAIL_STATUS = '0'
        P20 = ''

        sqlG = " insert into MID_PAY_PLAN_JS(P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, STATUS, P23, P14, P15, PAY_MARK, PAY_TIME, RECIP_BANK_NO, RECIP_ACC, RECIP_NAME, FAIL_CONFIRM, FAIL_STATUS, P20)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25) "

        cr.execute(sqlG, (P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, STATUS, P23, P14, P15, PAY_MARK, PAY_TIME, RECIP_BANK_NO, RECIP_ACC, RECIP_NAME, FAIL_CONFIRM, FAIL_STATUS, P20))

         # 子表
        S1 = '110'
        S2 = '城镇企业职工基本养老保险'
        S3 = otherStyleTime5
        S100 = P4

        if cl_agency_code[country_code] == '00':
            S4 = '22999'
            S5 = '上海市待遇支付往来单位001'
            S4_2 = '22998'
            S5_2 = '上海市待遇支付往来单位002'
        elif cl_agency_code[country_code] == '130102':
            S4 = '22999'
            S5 = '长安区待遇支付往来单位001'
            S4_2 = '22998'
            S5_2 = '长安区待遇支付往来单位002'
        else:
            S4 = '22999'
            S5 = '安徽待遇支付往来单位001'
            S4_2 = '22998'
            S5_2 = '安徽待遇支付往来单位002'

        S6 = '20310'
        S7 = '10310'
        S8 = '900'
        S9 = '18000'
        S10 = '1111.11'

        S10_2 = '2222.22'

        S11 = '12'
        S12 = '13'
        S13 = '14'
        S14 = '15'
        S15 = '16'
        S16 = '17'
        S17 = '18'
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
        S45 = '事业'
        S46 = '测试1'
        STATUS = '0'

        S88 = '01'+P4
        S88_2 = '02'+P4
        S80 = P4
        S80_2 = P4
        AGENCY_CODE =cl_agency_code[country_code]
        AGENCY_NAME =cl_agency_name[country_code]
        FAIL_CONFIRM_z = ''


        sqlZ1 = " insert into MID_PAY_PLAN_ITEM_JS(S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, S36, S37, S38, S39, S40, S41, S42, S43, S44, S45, S46, S100, STATUS, S80, S88, AGENCY_CODE, AGENCY_NAME, FAIL_CONFIRM)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49,:50,:51,:52,:53) "

        cr.execute(sqlZ1, (S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, S36, S37, S38, S39, S40, S41, S42, S43, S44, S45, S46, S100, STATUS, S80, S88, AGENCY_CODE, AGENCY_NAME, FAIL_CONFIRM_z))

        cr.execute(sqlZ1, (S1, S2, S3, S4_2, S5_2, S6, S7, S8, S9, S10_2, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, S36, S37, S38, S39, S40, S41, S42, S43, S44, S45, S46, S100, STATUS, S80_2, S88_2, AGENCY_CODE, AGENCY_NAME, FAIL_CONFIRM_z))

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
    print(endtime)


if __name__ == '__main__':
    # 传参： country_code, n
    # 第一参数：0-上海 1-长安，2-安徽
    # 第二参数：0-DYZF
    make_sql(0,0, 2)


