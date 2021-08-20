# 连接数据库，db= 数据库名称
# from itertools import count
import pymysql
# 创建数据库bank，表名称bank，列数据名称为开户方法下数据名称。注意金额格式
# 获取连接对象
a1121 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='bank',charset="utf8")
cursor = a1121.cursor()  # 创建控制台
# 开户
def hk_hk(zhanghao,yue,xingming,mima,guojia,shengfen,jiedao,menpaihao,kaihuhang,type):
    # 判断数据库是否已满
    sql = 'select count(*) from bank'  # 记录sql语句
    cursor.execute(sql)      # 提交sql语句
    g = cursor.fetchone()    # 返回值执行语句的相关信息
    if g[0] > 100:
        return 3
    # 正常开户
    sql = 'insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    p = [zhanghao,yue,xingming,mima,guojia,shengfen,jiedao,menpaihao,kaihuhang,type]
    cursor.execute(sql, p)
    return 1
def randomzh():    #生成随机账号
    while True:
        z = ''
        for i in range(8):
            import random
            # h = chr(random.randrange(ord('0'), ord('9') + 1))
            h = str(random.randint(1,99999999)).zfill(8)
            z += h
            sql = 'select zhanghao from bank'
            cursor.execute(sql)
            d = cursor.fetchall()
            if z not in d or z[0] != 0:
                return z
def kh():
    a = '普通卡'
    b = '白金卡'
    xingming = input("请输入您的用户名：")
    mima = input("请输入您的密码：")
    guojia = input("请输入您的国家：")
    shengfen = input("请输入您的省份：")
    jiedao = input("请输入您的街道：")
    menpaihao = input("请输入您的门牌号：")
    kaihuhang = '中国农业银行'
    type = input("请选择您办理卡的类型：\n1.普通卡（转出额度每次<=2万）\n2.白金卡（转出额度每次<=5万）\n请输入序号：")
    yue = int(input("请输入您的存款金额："))
    if type == "1":
        type = a
    elif type == "2":
        type = b

    zhanghao= randomzh()
    '''# 创建游标，查询获得的数据以 字典（dict） 形式返回
    cursor = a1121.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行SQL语句，插入数据到 test 表，栏位名称为 name,value
    cursor.execute('insert into shujuku (zhanghao,yue,xingming,mima,guojia,shengfen,jiedao,menpaihao,kaihuhang,type) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(zhanghao,yue,xingming,mima,guojia,shengfen,jiedao,menpaihao,kaihuhang,type))
    a1121.commit()'''
    s = hk_hk(zhanghao,yue,xingming,mima,guojia,shengfen,jiedao,menpaihao,kaihuhang,type)
    if s == 3:
        print('用户已满')
    elif s == 1:
        print(''.center(23, '*'))
        print('*','开户成功',' ')
        print('*','账号',zhanghao,' ')
        print('*','姓名',xingming,' ')
        print('*','密码','******',' ')
        print('*','国家',guojia,' ')
        print('*','省份',shengfen,' ')
        print('*','街道',jiedao,' ')
        print('*','门牌号',menpaihao,' ')
        print('*','余额',yue,' ')
        print('*','类型',type,'')
        print(''.center(23, '*'))
# 查找存钱账号
def czcqzh(zhanghao_cq):
    sql = "select * from bank where zhanghao = %s"
    p = [zhanghao_cq]
    cursor.execute(sql, p)
    d = cursor.fetchall()
    if not d:
        return 1
    return 0
# 存钱主体
def cq():
    zhanghao_cq = input("请输入账号：")
    yue_cq = input("请输入金额：")
    d = czcqzh(zhanghao_cq)
    if d == 1:
        print("账号不存在！")
    elif d == 0:
        # 用sql语句把账户存入金钱
        sql = "update bank set yue = yue + %s where zhanghao = %s"
        p = [yue_cq, zhanghao_cq]
        cursor.execute(sql, p)
        # 用sql语句查询账户金钱
        sql = "select yue from bank where zhanghao= %s "
        p = [zhanghao_cq]
        cursor.execute(sql, p)
        d = cursor.fetchone()
        print("余额为：", d[0])
# 查找取钱账号
def czqqzh(zhanghao_qq,mima_qq,yue_qq):
    # 验证是否存在该卡号
    sql = "select * from bank where zhanghao = %s"
    p = [zhanghao_qq]
    cursor.execute(sql, p)
    d = cursor.fetchall()
    if not d:
        return 1
    # 验证密码
    sql = "select * from bank where zhanghao = %s and mima = %s"
    w = [zhanghao_qq,mima_qq]
    cursor.execute(sql, w)
    d = cursor.fetchall()
    if not d:
        return 2
    # 验证余额
    sql = "select yue from bank where zhanghao = %s"
    p = [zhanghao_qq]
    cursor.execute(sql, p)
    dd = cursor.fetchone()
    if yue_qq > dd[0]:
        return 3
    return 0
# 取钱主体
def qq():
    zhanghao_qq = input("请输入账号：")
    mima_qq = input("请输入密码：")
    yue_qq = int(input("请输入金额："))
    d = czqqzh(zhanghao_qq,mima_qq,yue_qq)
    if d == 1:
        print("账号不存在！")
    elif d == 2:
        print("密码不对！")
    elif d == 3:
        print("余额不足！")
    elif d == 0:
        # 用sql语句取出金钱
        sql = "update bank set yue = yue - %s where zhanghao = %s"
        p = [yue_qq,zhanghao_qq]
        cursor.execute(sql, p)
        sql = "select yue from bank where zhanghao = %s"
        p2 = [zhanghao_qq]
        cursor.execute(sql, p2)
        x = cursor.fetchone()
        print("取款成功！")
        print("账号：",zhanghao_qq)
        print("取款金额：",yue_qq)
        print("账户余额：",x[0])
# 查找账号和判断转入账号
def pdzz(zhanghao_chu,mima_chu,zhanghao_ru,yue_chu,leixing):
    # 判断转账用户类型
    if leixing == "2":
        # 验证是否存在该卡号
        sql = "select * from bank where zhanghao = %s"
        p = zhanghao_chu
        cursor.execute(sql, p)
        ddd = cursor.fetchall()
        if not ddd:
            return 1
        # 判断两次输入是否是同一账号
        if zhanghao_ru == zhanghao_chu:
            return 4
        # 验证密码
        sql = "select * from bank where zhanghao = %s and mima = %s"
        p = [zhanghao_chu,mima_chu]
        cursor.execute(sql, p)
        ddd1 = cursor.fetchall()
        if not ddd1:
            return 2
        # 验证金额是否足够
        sql = "select yue from bank where zhanghao = %s"
        p1 = [zhanghao_chu]
        cursor.execute(sql, p1)
        ddd = cursor.fetchall()
        # dddd = int(ddd[0])
        if yue_chu > ddd[0][0]:
            return 3
        # 判断转出账户是普通用户还是白金用户
        # -----跳过下行检测
        # no inspection PyUnreachableCode
        sql = "select type from bank where zhanghao = %s"
        p = [zhanghao_chu]
        # d = select(sql,p,mode="all")
        cursor.execute(sql, p)
        d = cursor.fetchall()
        if d[0][0] == "普通卡":
            if yue_chu >= 20000:
                return 6
        elif d[0][0] == "白金卡":
            if yue_chu >= 50000:
                return 7
        return 0
    elif leixing == "1":
        # 验证是否存在该卡号
        sql = "select * from bank where zhanghao = %s"
        p = zhanghao_chu
        cursor.execute(sql, p)
        ddd = cursor.fetchall()
        if not ddd:
            return 1
        # 判断两次输入是否是同一账号
        if zhanghao_ru == zhanghao_chu:
            return 4
        # 验证密码
        sql = "select * from bank where zhanghao = %s and mima = %s"
        p = [zhanghao_chu,mima_chu]
        cursor.execute(sql, p)
        ddd1 = cursor.fetchall()
        if not ddd1:
            return 2
        # 验证金额是否足够
        sql = "select yue from bank where zhanghao = %s"
        p1 = [zhanghao_chu]
        cursor.execute(sql, p1)
        ddd = cursor.fetchall()
        # dddd = int(ddd[0])
        if yue_chu > ddd[0][0]:
            return 3
        return 0
    else:
        print("输入错误")
# 转账主体
def zz():
    leixing = input("请选择转账类型，\n1.普通转账\n2.跨行转账\n")
    zhanghao_chu = input("请输入账号")
    mima_chu = input("请输入密码")
    zhanghao_ru = input("请输入转入账号")
    yue_chu = int(input("请输入转入金额"))
    q = pdzz(zhanghao_chu,mima_chu,zhanghao_ru,yue_chu,leixing)
    if q == 4:
        print("操作违法！")
    if q == 3:
        print("金额不足！")
    elif q == 2:
        print("密码错误！")
    elif q == 1:
        print("账号不存在！")
    elif q == 6:
        print("转账失败！请升级为白金卡，每次最大转账额度为2万元！")
    elif q == 7:
        print("转账失败！尊敬的白金卡用户，每次最大转账额度为5万元！")
    elif q == 0:
        if leixing == "1":
            # 开始转账 转出账号
            sql = "update bank set yue = yue - %s where zhanghao = %s"
            p = [yue_chu,zhanghao_chu]
            cursor.execute(sql, p)
            # 转入账号
            sql1 = "update bank set yue = yue + %s where zhanghao = %s"
            p1 = [yue_chu,zhanghao_ru]
            cursor.execute(sql1, p1)
            # 查询转出账号余额
            sql2 = "select yue from bank where zhanghao = %s"
            p2 = [zhanghao_chu]
            cursor.execute(sql2, p2)
            d = cursor.fetchone()
            print("转账成功！")
            print("转出账号：",zhanghao_chu)
            print("转入账号：",zhanghao_ru)
            print("转出金额：￥",yue_chu)
            print("存款余额：￥",d[0])
        elif leixing == "2":
            # 开始转账 转出账号
            sql = "update bank set yue = yue - %s where zhanghao = %s"
            p = [yue_chu,zhanghao_chu]
            cursor.execute(sql, p)
            # 转入账号
            # yue = yue + %s * (汇率)
            sql1 = "update bank set yue = yue + %s where zhanghao = %s"
            p1 = [yue_chu,zhanghao_ru]
            cursor.execute(sql1, p1)
            # 查询转出账号余额
            sql2 = "select yue from bank where zhanghao = %s"
            p2 = [zhanghao_chu]
            cursor.execute(sql2, p2)
            d = cursor.fetchone()
            print("转账成功！")
            print("转出账号：",zhanghao_chu)
            print("转入账号：",zhanghao_ru)
            print("转出金额：￥",yue_chu)
            print("存款余额：￥",d[0])
# 判断查询
def pdcx(zhanghao,mima):
    # 验证是否存在该卡号
    sql = "select * from bank where zhanghao = %s"
    pp = [zhanghao]
    cursor.execute(sql, pp)
    d1 = cursor.fetchall()
    if not d1:
        return 1
    # 验证密码
    sqlmm = "select * from bank where zhanghao = %s and mima = %s"
    p = [zhanghao,mima]
    cursor.execute(sqlmm,p)
    dd = cursor.fetchall()
    if not dd:
        return 2
    return 0
# 查询主体
def cx():
    zhanghao = input("请输入账号")
    mima = input("请输入密码")
    e = pdcx(zhanghao,mima)
    if e == 1:
        print("没有该账号")
    elif e == 2:
        print("密码输入有误")
    elif e == 0:
        sql = "select * from bank where zhanghao = %s"
        p = [zhanghao]
        cursor.execute(sql, p)
        d = cursor.fetchall()
        d = list(d)
        print("查询成功！")
        info = '''
                   ----------个人信息------
                   用户名：%s
                   账号：%s
                   地址信息
                       国家：%s
                       省份：%s
                       街道：%s
                       门牌号: %s
                   余额：%s
                   开户行：%s
                   ------------------------
               '''
        print(info % (d[0][2], d[0][0], d[0][4], d[0][5], d[0][6], d[0][7], d[0][1], d[0][9]))
# 循环主体
while True:
    print(''.center(23, '*'))
    print('*','中国农业银行'.center(15),'*'.rjust(1))
    print('*','账户管理系统'.center(15),'*'.rjust(1))
    print('*','V1.0'.center(19),'*'.rjust(1))
    print(''.center(23,'*'))
    print('*',' '.center(19),'*'.rjust(1))
    print('*',1, '.开户','*'.rjust(14))
    print('*',2, '.存钱','*'.rjust(14))
    print('*',3, '.取钱','*'.rjust(14))
    print('*',4, '.转账','*'.rjust(14))
    print('*',5, '.查询','*'.rjust(14))
    print('*',6, '.Bye！','*'.rjust(13))
    print(''.center(23, '*'))

    xuanze = input('请选择业务')
    xuanze = int(xuanze)
    if xuanze < 1 or xuanze > 6:
        print('输入错误')
    else:
        if xuanze == 1:
            kh()
            a1121.commit()
        elif xuanze == 2:
            cq()
            a1121.commit()
        elif xuanze == 3:
            qq()
            a1121.commit()
        elif xuanze == 4:
            zz()
            a1121.commit()
        elif xuanze == 5:
            cx()
            a1121.commit()
        elif xuanze == 6:
            break
