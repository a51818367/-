import xlrd

wb = xlrd.open_workbook(filename=r"D:\python自动化测试------------\python自动化\day07\任务\2020.xls",encoding_override=True)
biao={}
for i in range (12):
    st=wb.sheet_by_index(i)
    row =st.nrows
    clo = st.ncols
    for r in range(1, row):
        for c in range(0, clo):
            d=st.cell_value(r, 1)
            b = st.cell_value(r,4)
            if d not in biao:
                biao[d]={
                    "销售量":b,
                    "单价": st.cell_value(r, 2)
                }
            elif d in biao:
                biao[d]={
                    "销售量":biao[d]["销售量"]+b,
                    "单价":st.cell_value(r,2)
                }
            break
print()
qne=0.0 #全年销售额
qnl=0.0#全年销售量
for i in biao:
    qne=qne+float(biao[i]["销售量"])*float(biao[i]["单价"])
    qnl=qnl+biao[i]["销售量"]
print("全年的销售总额：",qne,"元")
for i in biao:
    aa=(biao[i]["销售量"] /qnl)*100
    nn=biao[i]["销售量"]*biao[i]["单价"]/qne*100
    print(i,"的销售占比：",'%.2f'% aa,"%")
    print(i,"的销售额占比：",'%.2f'% nn, "%")


max=biao["羽绒服"]["销售量"]
for i in biao:
    if max<biao[i]["销售量"]:
        max=biao[i]["销售量"]
        f=i
print("最畅销的衣服是:",f)

min=biao["羽绒服"]["销售量"]
for i in biao:
    if min>biao[i]["销售量"]:
        min=biao[i]["销售量"]
        a=i
print("全年销量最低的衣服:",a)