# 这里使用内置的 xml 库；parse是解析xml文件的，parseString是解析数据流的
# from xml.dom.minidom import parse, parseString
import urllib

# # print（res_xml）
# dom_tree = parseString(res_xml)
# dom_obj = dom_tree.documentElement
# # print(dom_obj)
# # 这里可以根据标签名称进行搜索，有多个相同标签的话，可以使用for循环提取
# this_dom_res_obj = dom_obj.getElementsByTagName('Test_Info_Frmweb_Result')
# # 提取消息体
# this_dom_data = this_dom_res_obj[0].childNodes[0].data
# print(this_dom_data)
#
#
# # 接口不同，消息体和需要传入的参数也是不同的。body可以参照你需要请求的webservice接口的数据样例
# body = '''<?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <Test_Info_Frmweb xmlns="http://localhost/">
#       <sImport>''' + str(这里添加上需要发送的参数，这里可以指定编码) + '''</sImport>
#     </Test_Info_Frmweb>
#   </soap:Body>
# </soap:Envelope>'''
#
# # 需要注意的是这里的SOAPAction，一定要正确。
# headers = {
#         'Host': '192.168.1.10',
#         'Content-Type': 'text/xml; charset=utf-8',
#         'Content-Length': str(len(body)),
#         'SOAPAction': "http://localhost/Test_Info_Frmweb"
#     }
# # 发送请求
# res_xml = requests.post(url=webservice_url, data=body.encode('utf-8'), headers=headers).content.decode('utf-8')


def InvokeWebservice(phone,msg):
    texturl='http://127.0.0.1:7789/SMSService.asmx?op=SendShortMessage'
    postcontent='<?xml version="1.0" encoding="utf-8"?>'
    postcontent+='<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
    postcontent+='<soap:Body>'
    postcontent+='<SendShortMessage xmlns="http://tempuri.org/">'
    postcontent+='<phonenum>'+phone+'</phonenum>'#参数
    postcontent+='<message>'+msg+'</message>'#参数
    postcontent+='</SendShortMessage>'
    postcontent+='</soap:Body>'
    postcontent+='</soap:Envelope>'
    req=urllib.request.Request(texturl,data=postcontent.encode('utf-8'),headers={'Content-Type': 'text/xml'})
    urllib.request.urlopen(req)
