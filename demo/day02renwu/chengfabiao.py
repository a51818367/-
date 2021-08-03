
hang = 1
while hang <= 9:
    lie = 1
    while (lie <= hang):
        print("%d*%d = %-2d" % (hang,lie ,hang * lie),end="\t")
        lie += 1
    print("")
    hang += 1

print('倒序打印')
h = 9
while h >= 1:
    l = 1
    while (l <= h):
        print("%d*%d = %-2d" % (h,l ,h * l),end="\t")
        l += 1
    print("")
    h -= 1










