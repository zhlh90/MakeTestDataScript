# -*- coding: utf-8 -*
import datetime

import pandas as pd
import random
import os
import string


# 从字符串中随机取n个字符组成字符串
def ran_strx(strx, n):
    items = list(strx)
    str2 = ''
    for i in range(0, n):
        random.randint(0, len(items)-1)
        str1 = items[random.randint(0, len(items)-1)]
        str2 += str(str1)
    return str2

# 经办机构
cl_agency_code = ['00','1300','34000301']
cl_agency_name = ['上海保险事业管理局','河北省','合肥市本级保险事业管理局']
# 会计科目
cl_EXP_PROJECT_CODE = ['1003010101','1003010102','1003010103','1003010104','1003010105','1003010106']
cl_EXP_PROJECT_NAME = ['定期3个月','定期6个月','定期1年','定期2年','定期3年','定期5年']
#########################
# 取字段：
# 业务表（SURP_FINANCE_EXP_ACCOUNT）：经办单位：agency_code; 会计科目:EXP_PROJECT_CODE  收支类型：IN_EXP_TYPE
# 会计表（问黄伟）：单位：agency_code，会计科目：**，借贷方向：***

# 收支与借贷对照：
# 收入：收支类型=0；借贷方向=借
# 支出：收支类型=1；借贷方向=贷
###############################
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

def make_excel(agency_code, insurance_code, n):

    headers = ['险种代码', '险种名称', '经办机构代码', '经办机构名称', '年月', '收支类型', '会计科目代码', '会计科目代码', '金额', '登记人']

    rows = []

    no = 1
    while (n > 0):
        INSURANCE_CODE = insurance_code
        INSURANCE_NAME = '城镇职工基本养老保险'
        AGENCY_CODE = cl_agency_code[agency_code]
        AGENCY_NAME = cl_agency_name[agency_code]
        Y_MONTH = otherStyleTime5
        IN_EXP_TYPE = str(int(random.uniform(0, 2)))
        num = int(random.uniform(0, 6))
        EXP_PROJECT_CODE = cl_EXP_PROJECT_CODE[num]
        EXP_PROJECT_NAME = cl_EXP_PROJECT_NAME[num]
        EXP_AMOUNT = round(random.uniform(10000, 10), 2)
        CREATE_USER = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)

        row =[INSURANCE_CODE, INSURANCE_NAME, AGENCY_CODE, AGENCY_NAME, Y_MONTH, IN_EXP_TYPE, EXP_PROJECT_CODE, EXP_PROJECT_NAME, EXP_AMOUNT, CREATE_USER]
        rows.append(row)
        no += 1
        n -= 1

    path = '../../Data_excel/统收统支/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + '财政专户台账'+str(otherStyleTime3)+'.xlsx'
    dt = pd.DataFrame(rows, columns=headers)
    dt.to_excel(file_name, index=0)


if __name__ == '__main__':
    # 传参： agency_code, insurance_code, n
    # 0-00-上海市
    # 1-1300-河北省
    # 2-34000301-安徽省合肥市
    make_excel(0, '110', 99)


