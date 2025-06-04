with open ("5.txt") as f:
    s = f.readline()

a = s.split("Y")
m = 0
a.sort(key=len)
print(len(a[-1]))
for i in a:
    temp = i.split(".")
    if len(temp) <= 6:
        m = max(m, len(i))
        #print(i, m)
    else:
        for j in range(len(temp) - 5):
            print(i, m)
            m = max(m, len(temp[j])+ len(temp[j+1])+len(temp[j+2])+len(temp[j+3])+len(temp[j+4])+len(temp[j+5])+5)


print(m)
