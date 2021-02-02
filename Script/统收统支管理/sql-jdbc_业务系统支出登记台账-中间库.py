# -*- coding: utf-8 -*
import datetime
import cx_Oracle
import random
import os

# 从字符串中随机取n个字符组成字符串
def ran_strx(strx, n):
    items = list(strx)
    str2= ''
    for i in range(0, n):
        random.randint(0, len(items)-1)
        str1 = items[random.randint(0, len(items)-1)]
        str2 += str(str1)
    return str2

# 经办机构
cl_agency_code = ['00','1300','34000301']
cl_agency_name = ['上海保险事业管理局','河北省','合肥市本级保险事业管理局']
# 支出项目
cl_EXP_PROJECT_CODE = ['50010101','5001010201','5001010202','50010103','50010104','50010105','50010106','50010107']
cl_EXP_PROJECT_NAME = ['基础养老金','个人账户养老金-按月支出','个人账户养老金-一次性支出','过渡性养老金','离休金','退休金','退职金','补贴']
###############
# 取字段：
# 业务表（SURP_EXP_ACCOUNT）：经办单位：agency_code; 支出项目:EXP_PROJECT_CODE
# 会计表（问黄伟）：单位：agency_code，会计科目：**，借贷方向=借
###############
#获得当前时间
now = datetime.datetime.now()
#转换为指定的格式:
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
otherStyleTime1 = now.strftime("%Y%m%d%H")
otherStyleTime2 = now.strftime("%Y-%m-%d")
otherStyleTime3 = now.strftime("%Y%m%d%H%M%S")
otherStyleTime4 = now.strftime("%Y%m%d%H%M")
otherStyleTime5 = now.strftime("%Y-%m")

def make_sql(agency_code, n):

    starttime = datetime.datetime.now()
    db = cx_Oracle.connect('smifcmiddledb/1@10.10.66.159:1521/orcl')
    cr = db.cursor() #创建游标

    # 主表sql
    str_head_zhu = "insert into SURP_MID_EXP_ACCOUNT values ("

    no = 1
    while (n > 0):

        INSURANCE_CODE = '110'
        INSURANCE_NAME = '城镇企业职工基本养老保险'
        AGENCY_CODE = cl_agency_code[agency_code]
        Y_MONTH = otherStyleTime5
        num = int(random.uniform(0, 8))
        EXP_PROJECT_CODE = cl_EXP_PROJECT_CODE[num]
        EXP_PROJECT_NAME = cl_EXP_PROJECT_NAME[num]
        EXP_AMOUNT = str(round(random.uniform(10000, 10), 2))
        CREATE_USER = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
        # CREATE_TIME = "TO_TIMESTAMP("+otherStyleTime+",'SYYYY-MM-DD HH24:MI:SS:FF6')"
        CREATE_TIME = datetime.datetime.now()
        STATE = '0'
        AGENCY_NAME = cl_agency_name[agency_code]

        sqlG = " insert into SURP_MID_EXP_ACCOUNT(INSURANCE_CODE, INSURANCE_NAME, AGENCY_CODE, Y_MONTH, EXP_PROJECT_CODE, EXP_PROJECT_NAME, EXP_AMOUNT, CREATE_USER, CREATE_TIME, STATE, AGENCY_NAME)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11) "

        cr.execute(sqlG, (INSURANCE_CODE, INSURANCE_NAME, AGENCY_CODE, Y_MONTH, EXP_PROJECT_CODE, EXP_PROJECT_NAME, EXP_AMOUNT, CREATE_USER, CREATE_TIME, STATE, AGENCY_NAME))

        no += 1
        n -= 1

    cr.close()
    db.commit()
    db.close()
    endtime = datetime.datetime.now()
    print("耗时H：" + str(round((endtime - starttime).seconds / 3600, 2)))

if __name__ == '__main__':
    # 传参： agency_code, n
    # 0-00-上海市
    # 1-1300-河北省
    # 2-34000301-安徽省合肥市
    make_sql(0, 1)


