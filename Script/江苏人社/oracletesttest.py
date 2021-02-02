import datetime

import cx_Oracle
import random
import time

def mkdata(n,m,l,dd,ddd):
    starttime = datetime.datetime.now()
    nowdatekey = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    db = cx_Oracle.connect('smifcmiddledb/1@10.10.66.159:1521/orcl')
    cr = db.cursor() #创建游标
    num = 0
    for i in range(n):
        num +=1
        P4 = 'YW'+nowdatekey+str(i)
        P13S10D13 = random.uniform(100000, 20)
        P13S10D13 = round(P13S10D13, 2)
        P1 = dd
        P2 = '310'
        P3 = '城镇企业职工基本医疗保险'
        P4 = P4
        P5 = P4
        P6  = '00'
        P7  = '上海市统筹'
        P8  = '00'
        P9 = '上海市医保中心'
        P10  = 'K10025'
        P11  = '两定机构月结支付'
        P12 = '3'
        P13  = str(P13S10D13)
        STATUS = ''
        AAD404 = ''
        AAD405 = ''
        AAD406 = ''
        # sqlG = " insert into MID_PAY_PLAN(P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,STATUS,AAD404,AAD405,AAD406)  " \
        #  " values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') "

        sqlG = " insert into MID_PAY_PLAN(P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,STATUS,AAD404,AAD405,AAD406)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17) "
        # print(str(i) + " : " + sqlG)
        cr.execute(sqlG, (P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, STATUS, AAD404, AAD405, AAD406))
        for j in range(m):
            num += 1
            S1 = '310'
            S2 = '城镇企业职工基本医疗保险'
            S3 = dd
            S4 = '00400001'
            S5 =  'YWP'+nowdatekey+str(j)
            S6 = '20310'
            S7 = '10310'
            S8='900'
            S9='18000'
            S10 = random.uniform(100000, 20)
            S10 = round(S10, 2)
            S10 = S10
            S11 = '11'
            S12 = '12'
            S13 = '13'
            S14 = '14'
            S15 = '14'
            S16 = '14'
            S17 = '14'
            S18 = '14'
            S19 = '14'
            S20 = '14'
            S21 = '14'
            S22 = '14'
            S23 = '14'
            S24 = '14'
            S25 = '14'
            S26 = '14'
            S27 = '14'
            S28 = '14'
            S29 = '14'
            S30 = '14'
            S31 = '14'
            S32 = '14'
            S33 = '14'
            S34 = '14'
            S35 = '14'
            S36 = '14'
            S37 = '14'
            S38 = '14'
            S39 = '14'
            S40 = '14'
            S41 = '14'
            S42 = '14'
            S43 = '14'
            S44 = '14'
            S45 = '14'
            S46 = '测试1'
            S100 = P4
            STATUS = ''

            sqlF = "insert into MID_PAY_PLAN_ITEM(S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17,S18,S19,S20,S21,S22,S23,S24,S25,S26,S27,S28,S29,S30,S31,S32,S33,S34,S35,S36,S37,S38,S39,S40,S41,S42,S43,S44,S45,S46,S100,STATUS) " \
         " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48)"
            # print(str(j) + " : " + sqlG)
            cr.execute(sqlF,(S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17,S18,S19,S20,S21,S22,S23,S24,S25,S26,S27,S28,S29,S30,S31,S32,S33,S34,S35,S36,S37,S38,S39,S40,S41,S42,S43,S44,S45,S46,S100,STATUS))
            for k in range(l):
                num += 1
                D1 = ddd
                D2 = '310'
                D3 = '城镇职工基本医疗保险'
                D4 = '4'
                D5 = '5'
                D6 = '00'
                D7 = '上海市统筹'
                D8 = '00'
                D9 = '上海市医保中心'
                D10 = 'K10025'
                D11 = '两定机构月结支付'
                D12 = '3'
                D13 = random.uniform(100000, 20)
                D13 = round(D13, 2)
                D13 = D13
                D14 = '1'
                D15 = S5
                STATUS = ''
                sqlS =  " insert into MID_PAY_PLAN_ITEM_DETAIL(D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,STATUS)  " \
                  " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16) "
                # print(str(k)+" : " + sqlS)
                cr.execute(sqlS,(D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,STATUS))
                while(num>=100):
                    print(num)
                    db.commit()
                    num=0
    # res = cr.fetchall()
    # print(res)
    cr.close()
    db.commit()
    db.close()
    endtime = datetime.datetime.now()
    print("耗时H：" + str(round((endtime - starttime).seconds / 3600, 2)))


if __name__ == '__main__':
    mkdata(1,1,4,'2020-09','2020-09-24')

