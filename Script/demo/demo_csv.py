# -*- coding: utf-8 -*
import csv
import random
import os


# 基金险种代码
jjxz_code = ['1101', '1102', '1105']
# 基金险种名称
jjxz_name = ['企业职工基本养老保险基金', '城乡居民基本养老保险基金', '城乡居民基本医疗保险基金']
# 缴费类型
jflx_code = ['10', '20', '31', '32', '33', '34', '35', '40']
# 缴费标识
jfbs_code = ['缴费', '退费']
# 组织机构类型
zzjglx_code = ['11', '13', '15', '17', '19', '31', '32', '33', '34', '35', '36', '37', '39', '310', '330', '390']
# 经济类型
# jjlx_code = ['110', '120', '130', '140', '150', '160', '170', '']
jjlx_code = ['110', '120', '130', '140', '150', '160', '170']
# 行业
hy_code = ['A01', 'A02', 'A03', 'A04', 'A05', 'B06', 'B07']


# 从字符串中随机取n个字符组成字符串
def ran_strx(strx, n):
    items = list(strx)
    str2 = ''
    for i in range(0, n):
        random.randint(0, len(items)-1)
        str1 = items[random.randint(0, len(items)-1)]
        str2 += str(str1)
    return str2


# 单位缴费明细
def dwjf_csvtext(nd, yf, instype, dist, pathName, n):
    if yf.__len__() == 1:
        yf1 = '0' + yf
    else:
        yf1 = yf
    headers = ['社保业务系统编码', '统筹区编码', 'UUID', '社保经办机构编号', '征集通知流水号', '电子税票号码（缴费凭证号）',
               '险种类型', '单位编号', '对应费款所属期', '缴费类型', '缴费人数', '职工工资总额',
               '单位缴费基数总额', '个人缴费基数总额', '单位缴费比例或定额标准', '单位实缴金额', '个人缴费比例或定额标准',
               '个人实缴金额', '滞纳金', '利息', '缴费标识', '上解时间', '入国库时间', '主管税务部门代码', '数据传输类型',
               '传输批次号', '传输时间戳', '到账标记', '缴费明细流水号', '行政区划代码', '单位名称', '单位类型', '经济类型',
               '行业']

    rows = []
    no = 1
    while (n>0):
        SBYWXTBM = dist + '0001'
        TCQBM_DM = dist
        SBUUID = dist + str(nd)+str(yf1)+str(no)
        SBJBJG_DM = dist + '0101'
        ZJTZLSH = '987654321'
        DZSPHM = '876543219'
        XZLX_DM = instype
        DWBH = 'AAA'+yf1+str(n)
        DYFKSSQ = nd + yf1
        JFLX_DM = jflx_code[int(random.uniform(0, 8))]
        JFRS = int(random.uniform(1, 100000))
        ZGGZZE = round(random.uniform(2000000, 800), 2)
        DWJFJSZE = round(random.uniform(500000, 800), 2)
        GRJFJSZE = round(random.uniform(500000, 800), 2)
        SWJFFL = round(random.uniform(0, 1), 2)
        DWJFJE = round(random.uniform(500000, 800), 2)
        GRJFFL = round(random.uniform(0, 1), 2)
        GRJFJE = round(random.uniform(5000, 800), 2)
        ZNJ = round(random.uniform(500000, 800), 2)
        LX = round(random.uniform(500000, 800), 2)
        JFBS = jfbs_code[int(random.uniform(0, 2))]
        SJSJ = nd + yf1 + '01112233'
        RGKSJ = nd + yf1 + '01121314'
        ZGSWJG_DM = 'AAF'+yf1+str(n)
        SJCSLX = '1'  # 新增类型
        CSPCH = '11223344556677'
        CSSJC = nd +yf1 + '01122222'
        DZBJ = '1'  # 到账成功
        JFMXLSH = '998877665544332211'
        DIST = dist
        DWMC = ran_strx("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤", 2)+'企业'
        DWLX = zzjglx_code[int(random.uniform(0, 16))]
        JJLX = jjlx_code[int(random.uniform(0, 7))]
        HY = hy_code[int(random.uniform(0, 7))]

        row ={'社保业务系统编码':SBYWXTBM, '统筹区编码':TCQBM_DM, 'UUID':SBUUID, '社保经办机构编号':SBJBJG_DM, '征集通知流水号':ZJTZLSH,
              '电子税票号码（缴费凭证号）':DZSPHM,
               '险种类型':XZLX_DM, '单位编号':DWBH, '对应费款所属期':DYFKSSQ, '缴费类型':JFLX_DM, '缴费人数':JFRS, '职工工资总额':ZGGZZE,
               '单位缴费基数总额':DWJFJSZE, '个人缴费基数总额':GRJFJSZE, '单位缴费比例或定额标准':SWJFFL, '单位实缴金额':DWJFJE, '个人缴费比例或定额标准':GRJFFL,
               '个人实缴金额':GRJFJE, '滞纳金':ZNJ, '利息':LX, '缴费标识':JFBS, '上解时间':SJSJ, '入国库时间':RGKSJ, '主管税务部门代码':ZGSWJG_DM, '数据传输类型':SJCSLX,
               '传输批次号':CSPCH, '传输时间戳':CSSJC, '到账标记':DZBJ, '缴费明细流水号':JFMXLSH, '行政区划代码':DIST, '单位名称':DWMC, '单位类型':DWLX, '经济类型':JJLX,
               '行业':HY}
        rows.append(row)
        no += 1
        n -= 1
    path = '../Data_csv/' + pathName
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.mkdir(path)
    file_name = '../Data_csv/' + pathName + '/01_'+ instype + '_' + dist + '_' + nd + yf1 + '01_112233.csv'
    with open(file_name, 'w', newline='', encoding='utf-8')as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)


if __name__ == '__main__':
    # 文件名：01_1101_623443_20190621_100530.CSV
    # （文件业务类型_险种代码_行政区划编号_业务日期_创建文件的时分秒.CSV）
    # 传参：年度 月份 险种代码 行政区划编号 数据文件夹名称 文件包含记录数
    dwjf_csvtext('2020', '1', '1101', '1300', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '1', '1101', '130100', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '1', '1101', '130102', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '1', '1101', '130103', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '1', '1101', '130200', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '1', '1101', '130202', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '1', '1101', '130203', '01单位缴费明细_正向数据', 5)

    dwjf_csvtext('2020', '2', '1101', '1300', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '2', '1101', '130100', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '2', '1101', '130102', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '2', '1101', '130103', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '2', '1101', '130200', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '2', '1101', '130202', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '2', '1101', '130203', '01单位缴费明细_正向数据', 5)

    dwjf_csvtext('2020', '3', '1101', '1300', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '3', '1101', '130100', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '3', '1101', '130102', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '3', '1101', '130103', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '3', '1101', '130200', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '3', '1101', '130202', '01单位缴费明细_正向数据', 5)
    dwjf_csvtext('2020', '3', '1101', '130203', '01单位缴费明细_正向数据', 5)
