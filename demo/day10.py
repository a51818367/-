class shuibei:
    __gaodu = ""
    __rongji = ""
    __yanse = ""
    __caizhi = ""
    __mc = ""
    def setGaodu(self,gaodu):
        self.__gaodu = gaodu
    def getGaodu(self):
        return self.__gaodu
    def setRongji(self,rongji):
        self.__rongji = rongji
    def getRongji(self):
        return self.__rongji
    def setYanse(self,yanse):
        self.__yanse = yanse
    def getYanse(self):
        return self.__yanse
    def setCaizhi(self,caizhi):
        self.__caizhi = caizhi
    def getCaizhi(self):
        return self.__caizhi
    def setMc(self,mc):
        self.__mc = mc
    def getMc(self):
        return self.__mc
q = shuibei()
q.setGaodu(12)
q.setRongji(12)
q.setCaizhi('木')
q.setYanse('白')
q.setMc("可乐")
print(q.getGaodu(),q.getRongji(),q.getYanse(),q.getCaizhi(),q.getMc())
class bjbdn:
    __pmdx = ""
    __jg = ""
    __cpu = ""
    __nc = ""
    __djsc = ""
    __dz = ""
    __dyx = ""
    __ksp = ""
    def setPmdx(self,pmdx):
        self.__pmdx = pmdx
    def getPmdx(self):
        return self.__pmdx
    def setJg(self,jg):
        self.__jg = jg
    def getJg(self):
        return self.__jg
    def setCpu(self,cpu):
        self.__cpu = cpu
    def getCpu(self):
        return self.__cpu
    def setNc(self,nc):
        self.__nc = nc
    def getNc(self):
        return self.__nc
    def setDjsc(self,djsc):
        self.__djsc = djsc
    def getDjsc(self):
        return self.__djsc
    def setDz(self,dz):
        self.__dz = dz
    def getDz(self):
        return self.__dz
    def setDyx(self,dyx):
        self.__dyx = dyx
    def getDyx(self):
        return self.__dyx
    def setKsp(self,ksp):
        self.__ksp = ksp
    def getKsp(self):
        return self.__ksp
a = bjbdn() # 后加括号
a.setPmdx("45")
a.setJg('4500')
a.setCpu('amd')
a.setNc('512mb')
a.setDjsc('10小时')
a.setDz('金山打字')
a.setDyx("微笑")
a.setKsp("神话")
print(a.getPmdx(),a.getJg(),a.getCpu(),a.getNc(),a.getDjsc(),a.getDz(),a.getDyx(),a.getKsp())




