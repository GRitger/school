with open("24.txt") as f:
    st = f.readline()

for i in "QAZWSXEDCRFVTGBYHNUJMIKOLP":
    st = st.replace(i, " ")
a = st.split()
a.sort(key = len)
print(a)
