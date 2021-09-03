class excelxinxi:
    biao = []
    biao1 = []
    import xlrd
    wb = xlrd.open_workbook(filename=r"D:\python自动化测试------------\python自动化\day17\代码\autoweb02\草稿\ceshi.xls",encoding_override=True)
    st = wb.sheet_by_name("Sheet1")
    rows = st.nrows
    # print(rows)
    for row in range(1,rows):
        data = st.row_values(row)
        a = data[0]
        b = data[1]
        c = data[2]
        d = data[3]
        # "username":"不再爱了","password":"1234567","except":"Student Login"
        zidian = {
            "username":a,"password":b,"except":c,"state":d
        }
        biao.append(zidian)
    # print(biao)
    import xlrd
    wb = xlrd.open_workbook(filename=r"D:\python自动化测试------------\python自动化\day17\代码\autoweb02\草稿\ceshi.xls",encoding_override=True)
    st = wb.sheet_by_name("Sheet2")
    rows = st.nrows
    # print(rows)
    for row in range(1,rows):
        data = st.row_values(row)
        a = data[0]
        b = data[1]
        c = data[2]
        d = data[3]
        # "username":"不再爱了","password":"1234567","except":"Student Login"
        zidian = {
            "username":a,"password":b,"except":c,"state":d
        }
        biao1.append(zidian)