'''任务：
        优化购物小条
        10机械革命优惠券，0.5
        20张卫龙辣条优惠券 0.3
        15张HUA WEI WATCH 0.8
        随机抽取一张优惠券。


'''

shop = [
    ["lenovo PC", 5600],
    ["HUA WEI WATCH", 1200],
    ["Mac pro", 12000],
    ["洗衣机", 3000],
    ["机械革命", 5000],
    ["卫龙辣条", 4.5],
    ["老干妈辣酱", 20],
]

import random
youhuijuan = ['机械革命5折优惠券','机械革命5折优惠券','机械革命5折优惠券','机械革命5折优惠券','机械革命5折优惠券','机械革命5折优惠券','机械革命5折优惠券','机械革命5折优惠券','机械革命5折优惠券','机械革命5折优惠券',
              '卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券','卫龙辣条3折优惠券',
              'HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券','HUA WEI WATCH 8折优惠券'
              ]
yhj = random.randint(0,44)
print("你获得的优惠券为：",youhuijuan[yhj])
if youhuijuan[yhj] == '机械革命5折优惠券':
    a = 0.5
    s = 4
elif youhuijuan[yhj] == '卫龙辣条3折优惠券':
    a = 0.3
    s = 5
else:
    a = 0.8
    s = 1

money = input("输入您的初始金额：")
money = int(money)

mycar = []

i  = 0
while i < 20:
    for key,value in enumerate(shop):
        print(key,value)
    # 请输入您要卖的商品
    chose = input("请输入您要买的商品:")
    o = 0
    if chose.isdigit():
        chose = int(chose) # "1" --> 1
        if chose > len(shop) or chose < 0: # 9 > 7
            print("该商品不存在！别瞎弄！")
        else:
                if  chose == s and money > shop[chose][1]:
                    money = money - shop[chose][1] * a
                    mycar.append(shop[chose])
                    print("恭喜，商品添加成功！您的余额为：￥",money)
                    s = -99
                    f = shop[chose][1] * a
                    f = round(f, 2)



                elif chose != s and money > shop[chose][1] :
                    money = money - shop[chose][1]
                    mycar.append(shop[chose])
                    o = o+1
                    print("恭喜，商品添加成功！您的余额为：￥",money)
                else:
                    print("温馨提示：您的余额不足，穷鬼！请买其他商品！")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break
    else:
        print("对不起，别瞎弄！重新输入！")



i = i + 1

# 4. 打印结算购物小条
print("以下是您的购物小条，请拿好！！！！！")
print("".center(30,"-"))
for key,value in enumerate(mycar):
    print(key,value)
print(youhuijuan[yhj],"一张已使用，折后",f)
print("".center(30,"-"))


















