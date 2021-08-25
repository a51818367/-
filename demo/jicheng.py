class chushi:
    __name = ""
    __age = 0
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    def setage(self,age):
        self.__age = age
    def getage(self):
        return self.__age

class chuzi(chushi):
    chaocai = ""
    def chaoc(self):
        print("厨师正在做",self.chaocai)

class tudi(chuzi):
    zuofan = ""

    def zuof(self):
        print("李四正在做",self.zuofan)




t = tudi()
t.setname("张三")
t.setage(20)
print(t.getname(),t.getage())


t.zuofan = "炒面"
t.chaocai = "肉"
print(t.chaoc(),t.zuof())
















