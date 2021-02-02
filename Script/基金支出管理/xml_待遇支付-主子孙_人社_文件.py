# -*- coding:utf-8 -*-
import os
import xml.etree.ElementTree as ET
import random
import time
import datetime
from Script import shenfenzhenghao


# 统筹区
cl_AAA037_code = ['1002133','1002134']
cl_AAA037_name = ['养老金','离休金']
# 往来单位
cl_org_unit_code = ['999','998']
cl_org_unit_name = ['上海市待遇支付往来单位001','上海市待遇支付往来单位002']
# 增加换行符
def __indent(elem, level=0):
    i = "\n" + level*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            __indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

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

# 从字符串中随机取n个字符组成字符串
def ran_strx(strx, n):
    items = list(strx)
    str2 = ''
    for i in range(0, n):
        random.randint(0, len(items)-1)
        str1 = items[random.randint(0, len(items)-1)]
        str2 += str(str1)
    return str2

# 生成xml文件。传参：主表个数，子表个数，孙子个数，生成文件名称，AAZ031，MsgId
def makeXmlFile(mainNum, detailNum, childNum):
    data = ET.Element('Data')       # 创建节点
    tree = ET.ElementTree(data)     # 创建文档
    for i in range(mainNum):
        Main = ET.Element('Main')
        data.append(Main)
        creater = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
        moder = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
        nowdate = otherStyleTime
        yesdate = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
        amout = random.uniform(100000, 20)
        amout = round(amout, 2)
        # 主表
        P1 = ET.Element('P1')
        INSURANCE_CODE = ET.Element('INSURANCE_CODE')
        INSURANCE_NAME = ET.Element('INSURANCE_NAME')
        P4 = ET.Element('P4')
        P6 = ET.Element('P6')
        P7 = ET.Element('P7')
        P8 = ET.Element('P8')
        P9 = ET.Element('P9')
        P10 = ET.Element('P10')
        P11 = ET.Element('P11')
        P12 = ET.Element('P12')
        P13 = ET.Element('P13')
        P14 = ET.Element('P14')
        P15 = ET.Element('P15')
        P16 = ET.Element('P16')
        P17 = ET.Element('P17')
        P18 = ET.Element('P18')
        P19 = ET.Element('P19')
        P27 = ET.Element('P27')
        P28 = ET.Element('P28')
        P29 = ET.Element('P29')
        P30 = ET.Element('P30')
        AAZ031 = ET.Element('AAZ031')
        P23 = ET.Element('P23')

       #主表赋值
        P1.text = otherStyleTime6
        INSURANCE_CODE.text = '110'
        INSURANCE_NAME.text = '城镇企业职工基本养老保险'
        P4.text = 'YW' + otherStyleTime3 + str(i)
        P6.text = '00'
        P7.text = '上海市'
        P8.text = '00'
        P9.text = '上海保险事业管理局'
        P10.text = 'DYZFZZS'
        P11.text = '待遇支付-主子孙'
        P12.text = '2'
        P13.text = str(amout)
        P14.text = '000'
        P15.text = otherStyleTime
        P16.text = '1'
        P17.text = '310000'
        P18.text = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
        P19.text = otherStyleTime
        P27.text = '上海银行'
        P28.text = '313'
        P29.text = '张三'
        P30.text = ran_strx("0123456789", 16)
        AAZ031.text = P4.text
        P23.text = P4.text

       #主表
        Main.append(P1)
        Main.append(INSURANCE_CODE)
        Main.append(INSURANCE_NAME)
        Main.append(P4)
        Main.append(P6)
        Main.append(P7)
        Main.append(P8)
        Main.append(P9)
        Main.append(P10)
        Main.append(P11)
        Main.append(P12)
        Main.append(P13)
        Main.append(P14)
        Main.append(P15)
        Main.append(P16)
        Main.append(P17)
        Main.append(P18)
        Main.append(P19)
        Main.append(P27)
        Main.append(P28)
        Main.append(P29)
        Main.append(P30)
        Main.append(AAZ031)
        Main.append(P23)


        #子表
        Details = ET.Element('Details')
        Main.append(Details)
        for j in range(detailNum):
            Detail = ET.Element('Detail')
            Details.append(Detail)
            detailamout = round(amout / detailNum, 2)
            #子表
            INSURANCE_CODE = ET.Element('INSURANCE_CODE')
            INSURANCE_NAME = ET.Element('INSURANCE_NAME')
            S3 = ET.Element('S3')
            S4 = ET.Element('S4')
            S5 = ET.Element('S5')
            S6 = ET.Element('S6')
            S7 = ET.Element('S7')
            S8 = ET.Element('S8')
            S9 = ET.Element('S9')
            S10 = ET.Element('S10')
            S11 = ET.Element('S11')
            S12 = ET.Element('S12')
            S13 = ET.Element('S13')
            S14 = ET.Element('S14')
            S15 = ET.Element('S15')
            S16 = ET.Element('S16')
            S17 = ET.Element('S17')
            S18 = ET.Element('S18')
            S19 = ET.Element('S19')
            S93 = ET.Element('S93')
            S94 = ET.Element('S94')
            S95 = ET.Element('S95')
            S100 = ET.Element('S100')
            S81 = ET.Element('S81')
            S82 = ET.Element('S82')
            S83 = ET.Element('S83')
            S84 = ET.Element('S84')
            S85 = ET.Element('S85')
            S86 = ET.Element('S86')
            S87 = ET.Element('S87')
            S88 = ET.Element('S88')
            AGENCY_CODE = ET.Element('AGENCY_CODE')
            AGENCY_NAME = ET.Element('AGENCY_NAME')

        #子表赋值
            INSURANCE_CODE.text = '110'
            INSURANCE_NAME.text = '城镇企业职工基本养老保险'
            S3.text = otherStyleTime6
            S4.text = cl_org_unit_code[j]
            S5.text = cl_org_unit_name[j]
            S6.text = otherStyleTime6
            S7.text = '01'
            S8.text = shenfenzhenghao.outIDcard()
            S9.text = '2'
            S10.text = str(detailamout)
            S11.text = ran_strx("0123456789", 10)
            S12.text = ran_strx("0123456789", 15)
            S13.text = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
            S14.text = otherStyleTime
            S15.text = otherStyleTime2
            S16.text = '银行返回结果失败'
            S17.text = '银行附言：收到款项'
            S18.text = '1'
            S19.text = otherStyleTime3 + str(i)+ str(j)
            S93.text = '上海银行'
            S94.text = '313'
            S95.text = '张三'
            S100.text = P4.text
            S81.text = ran_strx("0123456789", 15)
            S82.text = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 3)
            S83.text = '313'
            S84.text = '上海银行'
            S85.text = '00'
            S86.text = '上海区县'
            S87.text = '123456123456'
            S88.text = '23435462'
            AGENCY_CODE.text = '00'
            AGENCY_NAME.text = '上海保险事业管理局'

            #加入节点
            Detail.append(INSURANCE_CODE)
            Detail.append(INSURANCE_NAME)
            Detail.append(S3)
            Detail.append(S4)
            Detail.append(S5)
            Detail.append(S6)
            Detail.append(S7)
            Detail.append(S8)
            Detail.append(S9)
            Detail.append(S10)
            Detail.append(S11)
            Detail.append(S12)
            Detail.append(S13)
            Detail.append(S14)
            Detail.append(S15)
            Detail.append(S16)
            Detail.append(S17)
            Detail.append(S18)
            Detail.append(S19)
            Detail.append(S93)
            Detail.append(S94)
            Detail.append(S95)
            Detail.append(S100)
            Detail.append(S81)
            Detail.append(S82)
            Detail.append(S83)
            Detail.append(S84)
            Detail.append(S85)
            Detail.append(S86)
            Detail.append(S87)
            Detail.append(S88)
            Detail.append(AGENCY_CODE)
            Detail.append(AGENCY_NAME)


            # 孙表
            Children = ET.Element('Children')
            Detail.append(Children)
            for k in range(childNum):
                childavgamout = round(detailamout /childNum, 2)
                Child = ET.Element('Child')
                Children.append(Child)

                ID = ET.Element('ID')
                CREATE_BY = ET.Element('CREATE_BY')
                CREATE_DATE = ET.Element('CREATE_DATE')
                LAST_MODIFIED_BY = ET.Element('LAST_MODIFIED_BY')
                LAST_MODIFIED_DATE = ET.Element('LAST_MODIFIED_DATE')
                LAST_MODIFIED_VERSION = ET.Element('LAST_MODIFIED_VERSION')
                AAA036 = ET.Element('AAA036')
                AAA037 = ET.Element('AAA037')
                AAA085 = ET.Element('AAA085')
                AAA088 = ET.Element('AAA088')
                AAE002 = ET.Element('AAE002')
                AAE003 = ET.Element('AAE003')
                AAE019 = ET.Element('AAE019')
                AAZ031 = ET.Element('AAZ031')
                AAZ220 = ET.Element('AAZ220')
                BIE504 = ET.Element('BIE504')
                BIE505 = ET.Element('BIE505')
                BIE506 = ET.Element('BIE506')
                YW001 = ET.Element('YW001')
                YW002 = ET.Element('YW002')
                YW003 = ET.Element('YW003')
                YW004 = ET.Element('YW004')
                YW005 = ET.Element('YW005')

                #赋值
                CREATE_BY.text = ''
                CREATE_BY.text = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
                CREATE_DATE.text = otherStyleTime
                LAST_MODIFIED_BY.text = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)
                LAST_MODIFIED_DATE.text = otherStyleTime
                LAST_MODIFIED_VERSION.text = '1.0'
                AAA036.text = cl_AAA037_code[k]
                AAA037.text = cl_AAA037_name[k]
                AAA085.text = '1'
                AAA088.text = '1'
                AAE002.text = otherStyleTime2
                AAE003.text = otherStyleTime2
                AAE019.text = str(childavgamout)
                AAZ031.text = '2020061594350925355'
                AAZ220.text = S19.text
                BIE504.text = otherStyleTime
                BIE505.text = '1'
                BIE506.text = 'CX' + otherStyleTime4 + str(childNum)
                YW001.text = ''
                YW002.text = ''
                YW003.text = ''
                YW004.text = ''
                YW005.text = ''

                Child.append(ID)
                Child.append(CREATE_BY)
                Child.append(CREATE_DATE)
                Child.append(LAST_MODIFIED_BY)
                Child.append(LAST_MODIFIED_DATE)
                Child.append(LAST_MODIFIED_VERSION)
                Child.append(AAA036)
                Child.append(AAA037)
                Child.append(AAA085)
                Child.append(AAA088)
                Child.append(AAE002)
                Child.append(AAE003)
                Child.append(AAE019)
                Child.append(AAZ031)
                Child.append(AAZ220)
                Child.append(BIE504)
                Child.append(BIE505)
                Child.append(BIE506)
                Child.append(YW001)
                Child.append(YW002)
                Child.append(YW003)
                Child.append(YW004)
                Child.append(YW005)



   # 增加换行符
    __indent(data)

    path = '../../Data_xml/支付计划/'
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = path + '待遇支付-主子孙xml文件'+str(otherStyleTime3)+'.xml'
    tree.write(file_name, encoding='utf-8', xml_declaration=False)
    with open(file_name, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + content)


if __name__ == '__main__':
    # 2020年数据
    makeXmlFile(1, 2, 2)
