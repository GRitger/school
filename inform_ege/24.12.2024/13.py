with open("13.txt") as f:
    st = f.readline()

for i in "QZXSWDCVFRTGBNHJMKLP":
    st = st.replace(i, "1")
for i in "AEIOUY":
    st = st.replace(i,"0")

a = []
for i in range(len(st) - 2):
    if st[i] == "1" and st[i+1]== "1" and st[i+2] == "0":
        a.append(i)
m = 100000000000000000000000000000000000000000000000000000000000000000000000000000000
print(len(a))
for i in range(len(a)-499):
    m = min(m, a[i+499]-a[i] + 3)
print(m)

i = 0
j = 1

while j < len(st) -1:
    temp = st[i:j+1]
    if temp.count("CD") < 160:
        j += 1
    elif temp.count("CD") == 160:
        j += 1
        m = max(m, len(temp))
    elif temp.count("CD") > 160:
        i += 1
print(m)