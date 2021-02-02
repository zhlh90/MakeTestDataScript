# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import random


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


# 生成xml文件。传参：主附件数量，明细数量，每个明细的附件数量，生成文件名称，DealNo，MsgId
def makeXmlFile(fileNo, recDetailNo, recfileNo, fileName, dealNo, msgId):

    data = ET.Element('Root')       # 创建节点
    tree = ET.ElementTree(data)     # 创建文档

    mainname = ET.Element('Head')
    data.append(mainname)

    # 报文头部分
    MsgType = ET.Element('MsgType')
    MsgId = ET.Element('MsgId')
    Src = ET.Element('Src')
    SrcName = ET.Element('SrcName')
    SrcZone = ET.Element('SrcZone')
    SrcUserName = ET.Element('SrcUserName')
    Dst = ET.Element('Dst')
    DstName = ET.Element('DstName')
    WorkDate = ET.Element('WorkDate')
    MsgTime = ET.Element('MsgTime')
    Remark = ET.Element('Remark')

    MsgType.text = 'R0001'
    MsgId.text = msgId
    Src.text = '130001'
    SrcName.text = '河北省财政厅'
    SrcZone.text = '1300'
    SrcUserName.text = '演示'
    Dst.text = ''
    DstName.text = ''
    WorkDate.text = '20191209'
    MsgTime.text = '20191209'
    Remark.text = fileName

    mainname.append(MsgType)
    mainname.append(MsgId)
    mainname.append(Src)
    mainname.append(SrcName)
    mainname.append(SrcZone)
    mainname.append(SrcUserName)
    mainname.append(Dst)
    mainname.append(DstName)
    mainname.append(WorkDate)
    mainname.append(MsgTime)
    mainname.append(Remark)

    #报文体部分

    bodyname = ET.Element('Body')
    data.append(bodyname)

    DealNo = ET.Element('DealNo')
    Year = ET.Element('Year')
    Month = ET.Element('Month')
    SysId = ET.Element('SysId')

    DealNo.text = dealNo
    Year.text = '2019'
    Month.text = '12'
    SysId.text = 'RS'

    bodyname.append(DealNo)
    bodyname.append(Year)
    bodyname.append(Month)
    bodyname.append(SysId)
    # 主附件部分
    Files = ET.Element('Files')
    bodyname.append(Files)
    for i in range(fileNo):
        File = ET.Element('File')

        FileType = ET.Element('FileType')
        FilePath = ET.Element('FilePath')
        FileName = ET.Element('FileName')

        FileType.text = '1'
        FilePath.text = '/home/data/'
        FileName.text = '01.jpg'

        File.append(FileType)
        File.append(FilePath)
        File.append(FileName)
        Files.append(File)
    # 明细部分
    RecDetails = ET.Element('RecDetails')
    bodyname.append(RecDetails)
    for i in range(recDetailNo):
        RecDetail = ET.Element('RecDetail')

        InsTypeCode = ET.Element('InsTypeCode')
        InsTypeName = ET.Element('InsTypeName')
        IoItemCode = ET.Element('IoItemCode')
        IoItemName = ET.Element('IoItemName')
        BkCode = ET.Element('BkCode')
        BkName = ET.Element('BkName')
        BkAccoNo = ET.Element('BkAccoNo')
        BkAccoName = ET.Element('BkAccoName')
        BkZone = ET.Element('BkZone')
        Amount = ET.Element('Amount')
        InBalance = ET.Element('InBalance')
        OutBalance = ET.Element('OutBalance')
        NumPeople = ET.Element('NumPeople')
        Level = ET.Element('Level')
        OutUseReason = ET.Element('OutUseReason')

        # InsTypeCode.text = '1102'
        # InsTypeName.text = '城乡居民基本养老保险基金'
        InsTypeCode.text = '1101'
        InsTypeName.text = '企业职工基本养老保险基金'
        IoItemCode.text = '0502'
        IoItemName.text = '转移支出'
        BkCode.text = '102'
        BkName.text = '中国工商银行'
        BkAccoNo.text = '130011010022737-01'
        BkAccoName.text = '省厅专户1101-活期'
        BkZone.text = '1300'
        Amount.text = str(round(random.uniform(5000000, 800), 2))
        InBalance.text = str(round(random.uniform(5000000, 800), 2))
        OutBalance.text = str(round(random.uniform(5000000, 800), 2))
        NumPeople.text = str(round(random.uniform(200, 0)))
        Level.text = str(round(random.uniform(5000000, 800), 2))
        OutUseReason.text = '测试_5001_M4'

        RecDetail.append(InsTypeCode)
        RecDetail.append(InsTypeName)
        RecDetail.append(IoItemCode)
        RecDetail.append(IoItemName)
        RecDetail.append(BkCode)
        RecDetail.append(BkName)
        RecDetail.append(BkAccoNo)
        RecDetail.append(BkAccoName)
        RecDetail.append(BkZone)
        RecDetail.append(Amount)
        RecDetail.append(InBalance)
        RecDetail.append(OutBalance)
        RecDetail.append(NumPeople)
        RecDetail.append(Level)
        RecDetail.append(OutUseReason)
        RecDetails.append(RecDetail)
        # 明细附件部分
        RecFiles = ET.Element('Files')
        RecDetail.append(RecFiles)
        for j in range(recfileNo):
            RecFile = ET.Element('File')

            RecFileType = ET.Element('FileType')
            RecFilePath = ET.Element('FilePath')
            RecFileName = ET.Element('FileName')

            RecFileType.text = '1'
            RecFilePath.text = '/home/data/'
            RecFileName.text = '01.jpg'

            RecFile.append(RecFileType)
            RecFile.append(RecFilePath)
            RecFile.append(RecFileName)
            RecFiles.append(RecFile)

    # 增加换行符
    __indent(data)
    filepath = '../Data_xml/' + fileName +'.xml'
    tree.write(filepath, encoding='utf-8', xml_declaration=False)
    with open(filepath, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + content)


if __name__ == '__main__':
    # 生成xml文件。传参：主附件数量，明细数量，每个明细的附件数量，生成文件名称，DealNo，MsgId
    makeXmlFile(1, 1, 1, 'R0001-正向测试用例_5001_M4', 'asdfghjkqwe7', 'R0001_20191209')

    # 生成xml文件。传参：主附件数量，明细数量，每个明细的附件数量，生成文件名称，DealNo，MsgId
    # makeXmlFile(1, 1, 1, 'R0001-正向测试用例2', 'absdfghjka', 'R0001_20190821')
    # 生成xml文件。传参：主附件数量，明细数量，每个明细的附件数量，生成文件名称，DealNo，MsgId
    # makeXmlFile(1, 100, 1, 'R0001-报文中含100条明细', 'absdfghjka100', 'R0001_20190821')
    # makeXmlFile(1, 50, 1, 'R0001-报文中含50条明细', 'absdfghjka50', 'R0001_20190821')
    # makeXmlFile(1, 10, 1, 'R0001-正向测试_10条明细_9103', 'qwertyuiop10', 'R0001_20190823')
