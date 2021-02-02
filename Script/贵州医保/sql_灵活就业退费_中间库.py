# -*- coding: utf-8 -*
import datetime
import time

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

    path = '../../Data_sql/基金收入/灵活退费SQL/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + 'SMR_REFUND_UNIT'+str(otherStyleTime3)+'.sql'
    # file_name_item = path + 'MID_PAY_PLAN_ITEM'+str(otherStyleTime3)+'.sql'
    SMR_REFUND_FILE = open(file_name, 'w', encoding='utf-8')
    # SMRTS_PAY_PLAN_ITEM_file = open(file_name_item, 'w', encoding='utf-8')

    # 主子表sql
    str_head_zhu = "insert into SMR_REFUND_P values ("
    str_head_item = "insert into SMR_REFUND_PERSON values ("

    no = 1
    while (n > 0):
        aaa325_str = ran_strx("1234567890",6)
        # 主表
        ID = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))	 # 主键
        CREATE_BY = '-1'	 # 创建人
        CREATE_DATE = otherStyleTime	 # 创建时间
        LAST_MODIFIED_BY = '-1'	 # 最后修改人
        LAST_MODIFIED_DATE = otherStyleTime	 # 最后修改时间
        LAST_MODIFIED_VERSION = '1.0'	 # 版本信息
        AAA325 = aaa325_str	 # 唯一识别退费申请
        AAB034 = agency_code	 # 社保经办机构账户
        #灵活就业退费不能有单位编号字段
        AAB001 = ''	 # 单位编号
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
        AAC001 = ran_strx("1234567890",6)	 # 人员编号：与单位编号互斥
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

        # 子表
        id = otherStyleTime3 + str(n) + ''.join(random.sample(string.ascii_lowercase + string.digits, 13))	 # 主键
        create_by = '-1'	 # 创建人
        create_date = otherStyleTime	 # 创建时间
        last_modified_by = '-1'	 # 最后修改人
        last_modified_date = otherStyleTime	 # 最后修改时间
        last_modified_version = '1.0'	 # 版本信息
        aaa325 = aaa325_str	 # 退费申请uuid
        aaa319 = ran_strx("1234567890",10)	 # 唯一识别退费明细
        aaz400 = '123456'	 # 社保业务系统编码
        aad009 = ran_strx("1234567890", 8)  # 电子税票号码
        aac001 = ran_strx("1234567890",6)
        aae140 = insurance_code  # 险种类型
        aaa115 = '1'
        aae041 = otherStyleTime2	 # 费款所属期起
        aae042 = otherStyleTime2	 # 费款所属期止
        aae082 = round(random.uniform(100000, 10), 2)
        aae239 = round(random.uniform(100000, 10), 2)
        aic152 = round(random.uniform(100000, 10), 2)
        aae530 = otherStyleTime1	 # 上解时间
        aae531 = otherStyleTime1	 # 入国库日期
        aaf020 = '78712631'
        aab121 = round(random.uniform(100000, 10), 2)
        aab120 = round(random.uniform(100000, 10), 2)
        aab288 = round(random.uniform(100000, 10), 2)
        aab289 = round(random.uniform(100000, 10), 2)
        aab290 = round(random.uniform(100000, 10), 2)
        aab291 = round(random.uniform(100000, 10), 2)
        aab292 = ''	 # 调整前单位部分费率
        aab293 = ''	 # 调整后单位部分费率
        aab294 = ''	 # 调整前个人部分费率
        aab295 = ''	 # 调整后个人部分费率
        aaa321 = '0'+ran_strx("123456789",1)
        aaa322 = ran_strx("1234567890",10)
        aae418 = str(now)	 # 传输时间戳
        aab034 = agency_code
        aae546 = round(random.uniform(100000, 10), 2)
        aae547 = round(random.uniform(100000, 10), 2)
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




        line = str_head_zhu + '"' + ID + '", "' + CREATE_BY + '","'  + CREATE_DATE  + '","' + LAST_MODIFIED_BY + '","' + LAST_MODIFIED_DATE + '","' + LAST_MODIFIED_VERSION + '", "' +  AAA325 + '", "' +  AAB034 + '", "' +  AAB001 + '", "' +  AAF020 + '", "' +  AAE494 + '", "' +  AAE491 + '", "' +  AAE495 + '", "' +  AAE492 + '", "' +  AAE493 + '", "' +  AAA321 + '", "' +  AAA322 + '", "' +  AAE418 + '", "' +  AAE005 + '", "' +  AAC001 + '", "' +  AAZ400 + '", "' +  VOU_GUID + '", "' +  VOU_NO + '", "' +  VOU_DATE + '", "' +  VOU_STATUS + '", "' +  EXCHANGE_PLAN_ID + '", "' +  EXCHANGE_PLAN_STATUS + '", "' +  PROC_DEF_ID + '", "' +  PROC_INST_ID + '", "' +  NODE_ID + '", "' +  TASK_ID + '", "' +  AUDIT_STATUS + '", "' +  CW_BATCH_NO + '", "' +  PAY_STATUS + '", "' +  VOU_GUID1 + '", "' +  VOU_NO1 + '", "' +  VOU_DATE1 + '", "' +  IS_RETURN + '", "' +  FIELD01 + '", "' +  FIELD02 + '", "' +  FIELD03 + '", "' +  FIELD04 + '", "' +  FIELD05 + '", "' +  AMT01 + '", "' +  AMT02 + '", "' +  AMT03 + '", "' +  AMT04 + '", "' +  AMT05 + '");'

        line_item = str_head_item + '"' + id + '", "' + create_by + '","' + create_date + '","' + last_modified_by + '","' + last_modified_date + '","' + last_modified_version + '", "' +  aaa325 + '", "' +  aaa319 + '", "' +  aaz400  + '", "' +  aad009  + '", "' +  aac001  + '", "' +  aae140  + '", "' +  aaa115  + '", "' +  aae041 + '", "' +  aae042 + '", "' +  str(aae082) + '", "' +  str(aae239) + '", "' +  str(aic152) + '", "' +  aae530 + '", "' +  aae531 + '", "' +  aaf020  + '", "' +  str(aab121) + '", "' +  str(aab120) + '", "' +  str(aab288) + '", "' +  str(aab289) + '", "' +  str(aab290) + '", "' +  str(aab291) + '", "' +  aab292 + '", "' +  aab293 + '", "' +  aab294 + '", "' +  aab295 + '", "' +  aaa321 + '", "' +  aaa322 + '", "' +  aae418 + '", "' +  aab034  + '", "' +  str(aae546) + '", "' +  str(aae547) + '", "' +  exchange_plan_id + '", "' +  exchange_plan_status + '", "' +  field01 + '", "' +  field02 + '", "' +  field03 + '", "' +  field04 + '", "' +  field05 + '", "' +  amt01 + '", "' +  amt02 + '", "' +  amt03 + '", "' +  amt04 + '", "' +  amt05 + '");'


        line = line.replace('\"', '\'')
        line_item = line_item.replace('\"', '\'')

        no += 1
        n -= 1

        SMR_REFUND_FILE.write(line + '\n')
        SMR_REFUND_FILE.write(line_item + '\n')



if __name__ == '__main__':
    # 传参： agency_code, insurance_code, n
    make_sql('520201', '310', 10)



