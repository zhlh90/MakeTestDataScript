import cx_Oracle


# 财务批次号
batchNo = '2020112600000007'
# 支付流水号，从数据表中查询
db = cx_Oracle.connect('shyb1119/1@168.10.49.152:1521/ybtest')
cr = db.cursor() #创建游标
# 查询字段
# sqlG = "select sys_name from sys_app where sys_id = '673'"
# cr.execute(sqlG)
# row = cr.fetchone()
# 查询字段 传参
# cr.execute("select sys_name from sys_app where sys_id =：1",['673'])
# row = cr.fetchone()
# 查询clob
# sqlG = "select REQUEST_MESSAGE from SMC_SYS_XML_LOG where BUSINESS_NO = '1002' and  REQUEST_MESSAGE like '%2020112600000007%';"
cr.execute("select REQUEST_MESSAGE from SMC_SYS_XML_LOG where BUSINESS_NO = :1 and  REQUEST_MESSAGE like :2",['1002','%2020112600000007%'])
msgId = ''
for row in cr:
    msgId = bytes.fromhex(row[0]).decode('utf8')#或者print(row[11].read())，row[11]是clob字段

print(msgId)
#
# print(row[0])
# pram = []
# for i in cr:
#     text = i[0].read()
#     pram.append(text)
cr.close()
db.close()




