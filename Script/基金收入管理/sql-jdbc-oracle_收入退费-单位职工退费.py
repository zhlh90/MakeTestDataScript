# -*- coding: utf-8 -*
import datetime
import time
import cx_Oracle

# import pandas as pd
import random
import string
from enum import Enum
import os

# 业务类型
# cl_bussnisstype_code = ['K10025','K1002501','K1002502','K1002503','K1002504','K1002505','K1002506','K1002507','K1002508','K1002509','K1002510','K1002511','K1002512','K1002513','K1002514','K1002515']
# cl_bussnisstype_name = ['两定机构月结支付','地税回盘实收到帐','地税回盘失败','统筹范围外医保基金转移','跨省异地清算','大额医疗保险费','中心报销','中心报销大额','异地清算扣款','月结算','跨省大额预付金','省内异地清算','跨省大额预付金上解','省内大额预付金','账户返还','年结算']


# cl_bussnisstype_code = ['KC24','KB03_YD']
# cl_bussnisstype_name = ['中心报销','月结算连锁药店']

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

def make_sql(agency_code, insurance_code, n):
    starttime = datetime.datetime.now()
    db = cx_Oracle.connect('smifcmiddledb/1@10.10.66.159:1521/orcl')
    cr = db.cursor() #创建游标

    no = 1
    while (n > 0):
        aaa325_str = ran_strx("1234567890",6)
        # 主表
        ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))	 # 主键
        CREATE_BY = '-1'	 # 创建人
        CREATE_DATE = now	 # 创建时间
        LAST_MODIFIED_BY = '-1'	 # 最后修改人
        LAST_MODIFIED_DATE = now	 # 最后修改时间
        LAST_MODIFIED_VERSION = '1.0'	 # 版本信息
        AAA325 = aaa325_str	 # 唯一识别退费申请
        AAB034 = agency_code	 # 社保经办机构账户
        AAB001 = '20201102'	 # 单位编号
        AAF020 = '769357'	 # 主管税务部门代码
        AAE494 = '0'+ran_strx("34",1)	 # 退费类型 04误收退费 03 结算退费
        AAE491 = '建设银行中关村支行'	 # 退费银行营业网点名称
        AAE495 = '5438268356'	 # 退费银行行号
        AAE492 = '北京市中心社会保障局'	 # 退费银行账户名称
        AAE493 = ran_strx("1234567890",16)	 # 退费银行账号
        AAA321 = '1'	 # 数据传输类型 取值为：新增、撤销
        AAA322 = ran_strx("1234567890",15)	 # 传输批次号
        AAE418 = str(now)	 # 传输时间戳
        AAE005 = '13'+ran_strx("1234567890",9)	 # 联系电话：退费申请人联系电话
        AAC001 = ''	 # 人员编号：与单位编号互斥
        AAZ400 = '123456'	 # 社保业务系统编码
        VOU_GUID = ''	 # 会计平台凭证id
        VOU_NO = ''	 # 凭证字号
        VOU_DATE = ''	 # 入账日期
        VOU_STATUS = '0'	 # 入账状态
        EXCHANGE_PLAN_ID = ''	 # 数据交换方案id
        EXCHANGE_PLAN_STATUS = ''	 # 数据交换方案状态
        PROC_DEF_ID = ''	 # 流程定义id
        PROC_INST_ID = ''	 # 流程实例id
        NODE_ID = ''	 # 节点id
        TASK_ID = ''	 # 任务id
        AUDIT_STATUS = ''	 # 审核状态
        CW_BATCH_NO = ''	 # 财务批次号
        PAY_STATUS = ''	 # 支付状态
        VOU_GUID1 = ''	 # 退票凭证id
        VOU_NO1 = ''	 # 退票凭证字号
        VOU_DATE1 = ''	 # 退票凭证日期
        IS_RETURN = ''	 # 是否生成退票凭证
        FIELD01 = ''	 # 备用字符字段
        FIELD02 = ''	 # 备用字符字段
        FIELD03 = ''	 # 备用字符字段
        FIELD04 = ''	 # 备用字符字段
        FIELD05 = ''	 # 备用字符字段
        AMT01 = ''	 # 备用金额字段
        AMT02 = ''	 # 备用金额字段
        AMT03 = ''	 # 备用金额字段
        AMT04 = ''	 # 备用金额字段
        AMT05 = ''	 # 备用金额字段

        sqlG = " insert into SMR_REFUND(ID, CREATE_BY, CREATE_DATE, LAST_MODIFIED_BY, LAST_MODIFIED_DATE, LAST_MODIFIED_VERSION, AAA325, AAB034, AAB001, AAF020, AAE494, AAE491, AAE495, AAE492, AAE493, AAA321, AAA322, AAE418, AAE005, AAC001, AAZ400, VOU_GUID, VOU_NO, VOU_DATE, VOU_STATUS, EXCHANGE_PLAN_ID, EXCHANGE_PLAN_STATUS, PROC_DEF_ID, PROC_INST_ID, NODE_ID, TASK_ID, AUDIT_STATUS, CW_BATCH_NO, PAY_STATUS, VOU_GUID1, VOU_NO1, VOU_DATE1, IS_RETURN, FIELD01, FIELD02, FIELD03, FIELD04, FIELD05, AMT01, AMT02, AMT03, AMT04, AMT05)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48) "

        cr.execute(sqlG, (ID, CREATE_BY, CREATE_DATE, LAST_MODIFIED_BY, LAST_MODIFIED_DATE, LAST_MODIFIED_VERSION, AAA325, AAB034, AAB001, AAF020, AAE494, AAE491, AAE495, AAE492, AAE493, AAA321, AAA322, AAE418, AAE005, AAC001, AAZ400, VOU_GUID, VOU_NO, VOU_DATE, VOU_STATUS, EXCHANGE_PLAN_ID, EXCHANGE_PLAN_STATUS, PROC_DEF_ID, PROC_INST_ID, NODE_ID, TASK_ID, AUDIT_STATUS, CW_BATCH_NO, PAY_STATUS, VOU_GUID1, VOU_NO1, VOU_DATE1, IS_RETURN, FIELD01, FIELD02, FIELD03, FIELD04, FIELD05, AMT01, AMT02, AMT03, AMT04, AMT05))

        # 子表
        id = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))	 # 主键
        create_by = '-1'	 # 创建人
        create_date = now	 # 创建时间
        last_modified_by = '-1'	 # 最后修改人
        last_modified_date = now	 # 最后修改时间
        last_modified_version = '1.0'	 # 版本信息
        aaa325 = aaa325_str	 # 退费申请uuid
        aaa320 = ran_strx("1234567890",10)	 # 唯一识别退费明细
        aaz400 = '123456'	 # 社保业务系统编码
        aae496 = round(random.uniform(100000, 10), 2)	 # 本次申请退费额
        aae497 = round(random.uniform(100000, 10), 2)	 # 单位缴纳部分退费总额
        aae498 = round(random.uniform(100000, 10), 2)	 # 个人缴纳部分退费总额
        aae499 = round(random.uniform(100000, 10), 2)	 # 滞纳金退费总额
        aae500 = round(random.uniform(100000, 10), 2)	 # 利息退费总额
        aad009 = ran_strx("1234567890",8)	 # 电子税票号码
        aae140 = insurance_code	 # 险种类型
        aae041 = otherStyleTime2	 # 费款所属期起
        aae042 = otherStyleTime2	 # 费款所属期止
        aae542 = round(random.uniform(100000, 10), 2)	 # 实缴金额
        aae056 = round(random.uniform(100000, 10), 2)	 # 滞纳金
        aae239 = round(random.uniform(100000, 10), 2)	 # 利息
        aae531 = otherStyleTime1	 # 入国库日期
        aae530 = otherStyleTime1	 # 上解时间
        aaa322 = '1'	 # 数据传输类型 取值为：新增、撤销
        aae418 = ran_strx("1234567890",10)	 # 传输批次号
        aae005 = str(now)	 # 传输时间戳
        aab001 = ran_strx("1234567890",6)	 # 单位编号
        aab121 = ''	 # 调整前单位部分缴费基数
        aab120 = ''	 # 调整前个人部分缴费基数
        aab288 = ''	 # 调整后单位部分缴费基数
        aab289 = ''	 # 调整后个人部分缴费基数
        aab290 = ''	 # 调整单位部分缴费基数差额
        aab291 = ''	 # 调整个人部分缴费基数差额
        aab292 = ''	 # 调整前单位部分费率
        aab293 = ''	 # 调整后单位部分费率
        aab294 = ''	 # 调整前个人部分费率
        aab295 = ''	 # 调整后个人部分费率
        vou_guid = ''	 # 会计平台凭证id
        vou_no = ''	 # 凭证字号
        vou_date = ''	 # 入账日期
        vou_status = '0'	 # 入账状态
        exchange_plan_id = ''	 # 数据交换方案id
        exchange_plan_status = ''	 # 数据交换方案状态
        field01 = ''	 # 备用字符字段
        field02 = ''	 # 备用字符字段
        field03 = ''	 # 备用字符字段
        field04 = ''	 # 备用字符字段
        field05 = ''	 # 备用字符字段
        amt01 = ''	 # 备用金额字段
        amt02 = ''	 # 备用金额字段
        amt03 = ''	 # 备用金额字段
        amt04 = ''	 # 备用金额字段
        amt05 = ''	 # 备用金额字段

        sqlF = " insert into SMR_REFUND_UNIT(id, create_by, create_date, last_modified_by, last_modified_date, last_modified_version, aaa325, aaa320, aaz400, aae496, aae497, aae498, aae499, aae500, aad009, aae140, aae041, aae042, aae542, aae056, aae239, aae531, aae530, aaa322, aae418, aae005, aab001, aab121, aab120, aab288, aab289, aab290, aab291, aab292, aab293, aab294, aab295, vou_guid, vou_no, vou_date, vou_status, exchange_plan_id, exchange_plan_status, field01, field02, field03, field04, field05, amt01, amt02, amt03, amt04, amt05)  " \
               " values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49,:50,:51,:52,:53) "

        cr.execute(sqlF, (id, create_by, create_date, last_modified_by, last_modified_date, last_modified_version, aaa325, aaa320, aaz400, aae496, aae497, aae498, aae499, aae500, aad009, aae140, aae041, aae042, aae542, aae056, aae239, aae531, aae530, aaa322, aae418, aae005, aab001, aab121, aab120, aab288, aab289, aab290, aab291, aab292, aab293, aab294, aab295, vou_guid, vou_no, vou_date, vou_status, exchange_plan_id, exchange_plan_status, field01, field02, field03, field04, field05, amt01, amt02, amt03, amt04, amt05))

        if n % 10000 == 0:
            db.commit()

        no += 1
        n -= 1

    cr.close()
    db.commit()
    db.close()
    endtime = datetime.datetime.now()
    print("耗时H：" + str(round((endtime - starttime).seconds / 3600, 2)))


if __name__ == '__main__':
    # 传参： agency_code, insurance_code, n
    make_sql('00', '310', 200000)



