fibolist = list()
for i in range(20):
    if i == 0:
        num = 0
        fibolist.append(num)
        continue
    if i == 1:
        num = 1
        fibolist.append(num)
        continue
    num = fibolist[i - 2] + fibolist[i - 1]
    fibolist.append(num)

print(fibolist)
