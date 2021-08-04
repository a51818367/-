'''
    猜数字：
        需求：系统随机产生一个数字，让用户从键盘输入您要的数字。(0~10000)
            1.如果猜中，则恭喜
            2.如果猜的数字比系统的数字大，温馨提示：大了
            3.如果猜小了，温馨提示：小了。
            一直到用户猜中为止。
        技术选型：
            1.random
            2.input
            3.if....else
            4.while
    金币功能：
        0.先登录，若登陆成功！
        1.玩家初始化5000硬币，猜错扣500,金币不够，系统锁定。
        2.猜中，奖励10000硬币，是否进行第二轮游戏。
'''

username = '1121'
password = '1121'
while True:
    user = input("请输入账号：")
    passwd = input('请输入密码：')
    if user == username and passwd == password:
        break
    else:
        print("账号密码不正确")



qi = 5000
kou = -500
jiang = 10000
import random
# 1.实现步骤
num = random.randint(0,10000)
count = 0
while True:
    count =  count + 1
    chose = input("输入您要的猜的数字：")
    chose = int(chose)
    if qi > 0:
        if chose > num:
            qi = qi + kou
            print("大了！","您现在有",qi,"金")
        elif chose < num:
            qi = qi + kou
            print("小了！","您现在有",qi,"金")
        else:
            num = random.randint(0,10000)
            qi = qi + jiang
            print("恭喜，您猜中了，本次数字为：",num,"，您本次输入了",count,"次！您现在有",qi,"金")
    else:
        print("GG")
        break












