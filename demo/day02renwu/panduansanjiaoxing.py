a = int(input("输入第一条边:"))
b = int(input("输入第二条边:"))
c = int(input("输入第三条边:"))
if a > 0 and b > 0 and c > 0:
    if a + b > c and b + c > a and a + c > b:
        if a == b and b == c:
            print("这是等边三角形")
        elif a == b or b == c or c == a:
            print("这是等腰三角形")
        else:
            print("这是一般三角形")
    elif a + b == c or b + c == a or a + c == b:
        print("这是个直角三角形")
    else:
        print('非三角形')
else:
    print("请输入大于0的数字")
