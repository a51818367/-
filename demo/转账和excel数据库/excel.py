import xlrd,pymysql
# 1、读取本地 Excel 数据集
wb = xlrd.open_workbook(filename=r"D:\python自动化测试------------\python自动化\day07\任务\2020.xls",encoding_override=True)
# print("数据行数：",sheet.nrows,"---","数据列数：",sheet.ncols)
# 2、连接数据库，创建游标，创建插入语句
a1121 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='lt')
cursor = a1121.cursor()
# sql = "create table 'test1' ('qwe' varchar(50) ) charset=utf8"
# 创建表
for i in ('1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'):
    sql = "create table if not exists %s(`日期` VARCHAR(10),`服装名称` VARCHAR(16),`价格/件` VARCHAR(16),`本月库存数量` VARCHAR(16),`销售量/每日` VARCHAR(16))" % i
    cursor.execute(sql)
    a1121.commit()
# 创建插入sql语句
for a in ('1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'):
    # k值(`日期`,`服装名称`,`价格/件`,`本月库存数量`,`销售量/每日`)-----可不写
    query = 'insert into '+a+' (`日期`,`服装名称`,`价格/件`,`本月库存数量`,`销售量/每日`)values(%s,%s,%s,%s,%s)'
    sheet = wb.sheet_by_name(a)
    rows = sheet.nrows
    for r in range(rows):
        data = sheet.row_values(r)
        sql = query
        p = data
        cursor.execute(sql, p)
        a1121.commit()
