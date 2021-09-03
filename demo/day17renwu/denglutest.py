from ddt import ddt
from ddt import data
from ddt import unpack
from selenium import webdriver
from unittest import TestCase
from excel import excelxinxi
from denglucaozuo import denglu
import warnings # 解决报错
import time
import xlrd
import xlwt
from xlutils.copy import copy

old_excel = xlrd.open_workbook(filename=r"D:\python自动化测试------------\python自动化\day17\代码\autoweb02\草稿\ceshi.xls",encoding_override=True)
st = old_excel.sheet_by_name('Sheet1')
st1 = old_excel.sheet_by_name('Sheet2')
new_excel = copy(old_excel)
# new_excel1 = copy(old_excel)
ws = new_excel.get_sheet(0)
ws1 = new_excel.get_sheet(1)
rows = st.nrows
rows1 = st1.nrows


@ddt
class denglutest(TestCase):

    def setUp(self) -> None: # 在每个方法执行前执行
        warnings.simplefilter('ignore',ResourceWarning) # 解决报错
        self.driver = webdriver.Edge(executable_path='msedgedriver.exe')
        self.driver.get('http://localhost:8080/HKR')

    def tearDown(self) -> None: # 在每个方法执行后执行
        warnings.simplefilter('ignore',ResourceWarning) # 解决报错
        self.driver.quit()

    @data (*excelxinxi.biao)
    def testdengluchenggong(self,shuju):
        warnings.simplefilter('ignore',ResourceWarning) # 解决报错
        # 1.准备数据
        username = shuju['username']
        pwd = shuju['password']
        fanhui = shuju['except']
        # 2.调用被测方法 : 页面操作
        login = denglu(self.driver)
        login.login(username,pwd)

        result = login.chenggongjieguo()
        # 3.获取实际结果并断言
        # self.assertEqual(result,fanhui)

        if result != fanhui:
            self.driver.save_screenshot("loginfai.jpg")
            for row in range(1,rows):
                name = st.cell_value(row,0)
                pd = st.cell_value(row,1)
                fh = st.cell_value(row,2)
                if name == username and pd == pwd and fh == fanhui:
                    # 写入数据
                    ws.write(row,3,'不通过')
                    # 另存为excel
                    new_excel.save('Testpass.xls')
        else:
            for row in range(1,rows):
                name = st.cell_value(row,0)
                pd = st.cell_value(row,1)
                fh = st.cell_value(row,2)
                if name == username and pd == pwd and fh == fanhui:
                    # 写入数据
                    ws.write(row,3,'通过')
                    # 另存为excel
                    new_excel.save('Testpass.xls')


    @data (*excelxinxi.biao1)
    def testdenglushibai(self,shuju):
        warnings.simplefilter('ignore',ResourceWarning) # 解决报错
        # 1.准备数据
        username = shuju['username']
        pwd = shuju['password']
        fanhui = shuju['except']
        # 2.调用被测方法 : 页面操作
        login = denglu(self.driver)
        login.login(username,pwd)

        result = login.shibaijieguo()
        # 3.获取实际结果并断言
        # self.assertEqual(result,fanhui)

        if result != fanhui:
            self.driver.save_screenshot("loginfail.jpg")
            for row in range(1,rows1):
                name = st1.cell_value(row,0)
                pd = st1.cell_value(row,1)
                fh = st1.cell_value(row,2)
                if name == username and pd == pwd and fh == fanhui:
                    # 写入数据
                    ws1.write(row,3,'不通过')
                    # 另存为excel
                    new_excel.save('Testpass.xls')
        else:
            for row in range(1,rows1):
                name = st1.cell_value(row,0)
                pd = st1.cell_value(row,1)
                fh = st1.cell_value(row,2)
                if name == username and pd == pwd and fh == fanhui:
                    # 写入数据
                    ws1.write(row,3,'通过')
                    # 另存为excel
                    new_excel.save('Testpass.xls')