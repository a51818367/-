

username = 'root'
password = 'admin'
for i in range(3):
    user = input("请输入账号：")
    passwd = input('请输入密码')
    if user == username and passwd == password:
        print("Welcome %s login."%(user))
        break
    elif i == 2:
        print("对不起，您输入的密码错误次数已达%s次"%(i+1))
    else:
        print("Error username or passwd.")















