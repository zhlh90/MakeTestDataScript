# -*- coding: utf-8 -*
import datetime

import pandas as pd
import random
import os

#业务类型
bussnisstype = ['K1002401', 'K1002402', 'K1002403', 'K1002404',
                'K10025', 'K10026', 'K90004', 'K90005', 'K90006',
                'K90007', 'K90008', 'K90009', 'K90010', 'K90011',
                'K90012', 'K90013', 'K90014', 'K90015', 'K90016', 'K90017', 'K90018']
bussnisstype_in = ['K90004', 'K90008', 'K90009', 'K90010', 'K90011', 'K90012', 'K90013', 'K90014', 'K90015']

# 从字符串中随机取n个字符组成字符串
def ran_strx(strx, n):
    items = list(strx)
    str2 = ''
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

def make_excel(agency_code, insurance_code, n):

    headers = ['PAYMENT_UNIT', 'RECEIVE_UNIT', 'RECEIPT_ACCOUNT_NAME', 'RECEIPT_ACCOUNT_NO', 'RECEIPT_ACCOUNT_TYPE', 'BANK_CODE', 'SUBSIDY_AMOUNT', 'INSURANCE_CODE', 'AGENCY_CODE', 'REGION_CODE']

    rows = []

    no = 1
    while (n > 0):
        #下拨付款往来单位名称（根据实际数据变更）
        PAYMENT_UNIT = '测试付款单位' + ran_strx("0123456789", 8)
        #下拨收款经办机构单位（根据实际数据变更）
        RECEIVE_UNIT = '测试收款经办机构'
        #下拨经办机构银行账户名称（根据实际数据变更）
        RECEIPT_ACCOUNT_NAME = '测试收款经办机构账户'
        #下拨经办机构银行账号（根据实际数据变更）
        RECEIPT_ACCOUNT_NO = ran_strx("0123456789", 16)
        RECEIPT_ACCOUNT_TYPE = '0'+ran_strx("1234", 1)
        BANK_CODE = '313'
        SUBSIDY_AMOUNT = round(random.uniform(100000, 10), 2)
        INSURANCE_CODE = insurance_code
        AGENCY_CODE = agency_code
        REGION_CODE = '310000'

        row =[PAYMENT_UNIT, RECEIVE_UNIT, RECEIPT_ACCOUNT_NAME, RECEIPT_ACCOUNT_NO, RECEIPT_ACCOUNT_TYPE, BANK_CODE, SUBSIDY_AMOUNT, INSURANCE_CODE, AGENCY_CODE, REGION_CODE]
        rows.append(row)
        no += 1
        n -= 1

    path = '../../Data_excel/基金收入/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + '上级补助收入数据接入表'+str(otherStyleTime3)+'.xlsx'
    dt = pd.DataFrame(rows, columns=headers)
    dt.to_excel(file_name, index=0)


if __name__ == '__main__':
    # 传参： agency_code, insurance_code, n
    make_excel('00', '310', 10)


