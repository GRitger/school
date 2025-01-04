with open("15.txt") as f:
    st = f.readline()

string = "KLMNK"
m_max = -10000000000000000000000000000000
m = 1
j = 0
for i in range(len(st)-1):
    if st[i] + st[i+1] in string:
        m += 1
        m_max = max(m, m_max)
    else:
        m = 1
print(m_max)