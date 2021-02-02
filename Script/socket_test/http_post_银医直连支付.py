import json

import cx_Oracle
import requests


def dataExcu(port,batchno):
        # 医保ipport,银医直连服务ipport
        IpPort = '10.10.64.204:7012'
        IpPort_bank = '192.168.50.93:7090'
        conn_DataBase = 'rsjjdb'
        if port == '7012':
                IpPort = '10.10.64.204:7012'
                IpPort_bank = '192.168.50.93:7090'
        # 财务批次号
        batchNo = batchno
        # 支付流水号，从数据表中查询
        db = cx_Oracle.connect('rsjjdb/1@10.10.66.159:1521/orcl')
        cr = db.cursor() #创建游标
        sqlG = "select REQUEST_MESSAGE from SMC_SYS_XML_LOG where BUSINESS_NO = '1002' and  REQUEST_MESSAGE like '%{batch}%';".format(batch=batchNo)
        request_Message = cr.execute(sqlG)
        



        siseq =

        url = "http://" + IpPort_bank + "/testMed/returnMedicalFile"
        values = {
                "bankCode": "313",
                "medicalCode": "00",
                "wsUrl": "http://" + IpPort + "/FM/services/SIMessageServices?wsdl",
                "wsNamespace": "http://webservice.server.direct.smifc.yonyougov.com",
                "siseq": "31310022020101000004367",
                "batchNo": batchNo
        }

# 打印values的数据类型,输出<class 'dict'>
print(type(values))
print(values)
# json.dump将python对象编码成json字符串
values_json = json.dumps(values)
# 打印编码成json字符串的values_json的数据类型,输出<class 'str'>
print(type(values_json))
print(values_json)
# # requests库提交数据进行post请求
# req = requests.post(url, data=values_json)
# # 打印Unicode编码格式的json数据
# print(req.text)
# # 使用json.dumps()时需要对象相应的类型是json可序列化的
# change = req.json()
# # json.dumps序列化时对中文默认使用ASCII编码,如果无任何配置则打印的均为ascii字符,输出中文需要指定ensure_ascii=False
# new_req = json.dumps(change, ensure_ascii=False)
# # 打印接口返回的数据,且以中文编码
# print(new_req)
