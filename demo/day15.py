biao = []
with open('baidu_x_system.log','r') as z:
    for a in z.readlines():
        b = a.split('\t')
        for c in b:
            sub_c = c.split(' ')
        if sub_c:
            biao.append(sub_c)
tong = [x[0] for x in biao]
zi = {}
for i in tong:
    zi[i] = zi.get(i,0)+1
print(zi)
z.close()