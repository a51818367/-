
class denglu:
    def __init__(self,driver):  # __init__ 构造方法
        self.driver = driver    # 声明driver为全局变量
        self.driver.maximize_window()

    def login(self,username,pwd):
        # 输入用户名
        self.driver.find_element_by_id("loginname").send_keys(username)
        # 输入密码
        self.driver.find_element_by_id("password").send_keys(pwd)
        # 点击登陆
        self.driver.find_element_by_id("submit").click()

    def chenggongjieguo(self):   # 成功结果
        return self.driver.title   # 返回标题

    def shibaijieguo(self):   # 失败结果
        return self.driver.find_element_by_id("msg_uname").text  # text()  提取元素的文本信息