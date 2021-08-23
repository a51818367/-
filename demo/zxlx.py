# 题目一
class kongtiao:
    __pinpai = ""
    __jiage = ""
    def setPinpai(self,pinpai):
        self.__pinpai = pinpai
    def getPinpai(self):
        return self.__pinpai
    def setJiage(self,jiage):
        self.__jiage = jiage
    def getJiage(self):
        return self.__jiage
    def kaiji(self):
        print("空调开机了...")
    def zidongguanbi(self,guanbi):
        print("空调将在",int(guanbi),"分钟后自动关闭...")

q = kongtiao()
q.setPinpai('海尔')
q.setJiage("3400")
q.kaiji()
q.zidongguanbi(10)
print(q.getPinpai(),q.getJiage())
# 题目二
class xuesheng:
    __xingming = ""
    __nianling = ""
    def setXingming(self,xingming):
        self.__xingming = xingming
    def getXingming(self):
        return self.__xingming
    def setNianling(self,nianling):
        if nianling >120 or nianling <0:
            print("您年龄输入非法！")
        else:
            self.__nianling = nianling
    def getNianling(self):
        return self.__nianling
    def jieshao(self):
        print("大家好，我叫",self.__xingming,"，今年",self.__nianling,"岁了！")
    def bijiao(self,tongzhuo):
        if self.__nianling > tongzhuo.getNianling():
            print('我比同桌大',(self.__nianling - tongzhuo.getNianling()),'岁！')
        elif self.__nianling < tongzhuo.getNianling():
            print('我比同桌小',(tongzhuo.getNianling() - self.__nianling),'岁！')
        else:
            print('我俩一样大！')
a = xuesheng()
a.setXingming('张三')
a.setNianling(18)

a1 = xuesheng()
a1.setXingming('李四')
a1.setNianling(16)

a.bijiao(a1)
a1.bijiao(a)
a.jieshao()
a1.jieshao()
# 题目三
class dianhua:
    __xingming = ""
    __xingbie = ""
    __nianling = ""
    __huafei = ""
    __pinpai = ""
    __dianchi = ""
    __pingmu = ""
    __daiji = ""
    __jifen = ""
    def setXingming(self,xingming):
        self.__xingming = xingming
    def getXingming(self):
        return self.__xingming
    def setXingbie(self,xingbie):
        if xingbie != "男" and xingbie != "女":
            print("赋值错误！")
        else:
            self.__xingbie = xingbie
    def getXingbie(self):
        return self.__xingbie
    def setNianling(self,nianling):
        if nianling >100 or nianling < 0:
            print('年龄错误')
        else:
            self.__nianling = nianling
    def getNianling(self):
        return self.__nianling
    def setHuafei(self,huafei):
        self.__huafei = huafei
    def getHuafei(self):
        return self.__huafei
    def setPinpai(self,pinpai):
        self.__pinpai = pinpai
    def getPinpai(self):
        return self.__pinpai
    def setDianchi(self,dianchi):
        self.__dianchi = dianchi
    def getDianchi(self):
        return self.__dianchi
    def setPingmu(self,pingmu):
        self.__pingmu = pingmu
    def getPingmu(self):
        return self.__pingmu
    def setDaiji(self,daiji):
        self.__daiji = daiji
    def getDaiji(self):
        return self.__daiji
    def setJifen(self,jifen):
        self.__jifen = jifen
    def getJifen(self):
        return self.__jifen
    def faduanxin(self):
        print(p.__xingming,p.__xingbie,p.__nianling,p.__huafei,p.__pinpai,p.__dianchi,p.__pingmu,p.__daiji,p.__jifen)
    def dadianhua(self,phone,time):
        if phone == None:
            print("手机号为空！")
            return
        elif self.dadianhua == phone:
            print("不能给自己打电话!")
            return
        else:
            print("正在给",phone,"打电话，","电话时长",time)
            if self.__huafei < 1:
                print("话费不足！")
                return
            #elif self.__huafei >= time:
            if time > 1 and time <= 10:
                if self.__huafei < time:
                    print("当前话费余额不能打", time, "分钟的电话！")
                    return
                print("正在给",phone,"打电话。。。")
                self.__huafei = self.__huafei - time
                self.__jifen = self.__jifen + str(time*15)
                print("电话已结束，当前话费余额为：￥",round(self.__huafei,2),",积分为：",self.__jifen)
            elif time > 10 and time <= 20:
                if self.__huafei < time*0.8:
                    print("当前话费余额不能打", time, "分钟的电话！")
                    return
                print("正在给", phone, "打电话。。。")
                self.__huafei = self.__huafei - time*0.8
                self.__jifen = self.__jifen + time * 39
                print("电话已结束，当前话费余额为：￥", round(self.__huafei,2), ",积分为：", self.__jifen)
            elif time > 20:
                if self.__huafei < time*0.65:
                    print("当前话费余额不能打", time, "分钟的电话！")
                    return
                print("正在给", phone, "打电话。。。")
                self.__huafei = self.__huafei - time*0.65
                self.__jifen = self.__jifen + time * 48
                print("电话已结束，当前话费余额为：￥", round(self.__huafei,2), ",积分为：", self.__jifen)
            else:
                print("分组输入非法！")

p = dianhua()
p.setHuafei(50)

p.dadianhua(155454,10)
# 题目四
# 1
class xuesheng:
    __xuehao = ""
    __xingming = ""
    __xingbie = ""
    __shengao = ""
    __tizhong = ""
    __chengji = ""
    __dizhi = ""
    __dianhua = ""
    def setXuehao(self,xuehao):
        self.__xuehao = xuehao
    def getXuehao(self):
        return self.__xuehao
    def setXingming(self,xingming):
        self.__xingming = xingming
    def getXingming(self):
        return self.__xingming
    def setXingbie(self,xingbie):
        self.__xingbie = xingbie
    def getXingbie(self):
        return self.__xingbie
    def setShengao(self,shengao):
        self.__shengao = shengao
    def getShengao(self):
        return self.__shengao
    def setTizhong(self,tizhong):
        self.__tizhong = tizhong
    def getTizhong(self):
        return self.__tizhong
    def setChengji(self,chengji):
        self.__chengji = chengji
    def getChengji(self):
        return self.__chengji
    def setDizhi(self,dizhi):
        self.__dizhi = dizhi
    def getDizhi(self):
        return self.__dizhi
    def setDianhua(self,dianhua):
        self.__dianhua = dianhua
    def getDianhua(self):
        return self.__dianhua
    def xuexi(self,time):
        print("学习了",time,"小时")
    def youxi(self,ming):
        print('玩了',ming)
    def biancheng(self,hang):
        print("写了",hang,'代码')
    def qiuhe(self,he):
        print('结果',he)
w = xuesheng()
e = int(input('输入数字')) + int(input('输入第二个数字'))
w.qiuhe(e)
# 2
class che:
    __xinghao = ""
    __chelun = ""
    __yanse = ""
    __zhongliang = ""
    __youxiang = ""
    def setXinghao(self,xinghao):
        self.__xinghao = xinghao
    def getXinghao(self):
        return self.__xinghao
    def setChelun(self,chelun):
        self.__chelun = chelun
    def getCHelun(self):
        return self.__chelun
    def setYanse(self,yanse):
        self.__yanse = yanse
    def getYanse(self):
        return self.__yanse
    def setZhongliang(self,zhongliang):
        self.__zhongliang = zhongliang
    def getZhongliang(self):
        return self.__zhongliang
    def setYouxiang(self,youxiang):
        self.__youxiang = youxiang
    def getYouxiang(self):
        return self.__youxiang
    def run(self):
        print('车为',r.getXinghao(),r.getCHelun(),r.getYanse(),r.getZhongliang(),r.getYouxiang())
r = che()
r.setXinghao(1)
r.setChelun(4)
r.setYanse('黑')
r.setZhongliang(115)
r.setYouxiang(60)
r.run()
# 3
# 任务10中重复
# 4
class houzi:
    __leibie = ""
    __xingbie = ""
    __yanse = ""
    __tizhong = ""
    def setLeibie(self,leibie):
        self.__leibie = leibie
    def getLeibie(self):
        return self.__leibie
    def setXingbie(self,xingbie):
        self.__xingbie = xingbie
    def getXingbie(self):
        return self.__xingbie
    def setYanse(self,yanse):
        self.__yanse = yanse
    def getYanse(self):
        return self.__yanse
    def setTizhong(self,tizhong):
        self.__tizhong = tizhong
    def getTizhong(self):
        return self.__tizhong
    def zaohuo(self,cailiao):
        print('用',cailiao,'生火')
    def xuexi(self,xue):
        print('学会了',xue)
t = houzi()
t.zaohuo('木头')
t.xuexi('用棍子')





