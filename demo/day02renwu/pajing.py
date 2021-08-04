

jing = -20
pa = 3
hua = -2
tian = 1
while jing<0:
    print ('天数',tian,end='   ')
    jing +=pa
    print ("距离",jing,end="   ")
    if jing>=0:
        break
    jing += hua
    print("滑下",jing)
    if jing >=0:
        break
    tian += 1




















