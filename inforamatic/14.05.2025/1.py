with open("1.txt") as f:
    st = f.readline()
c = 0
i = st.index("A")
j = i +1
while j < len(st):
    if st[j] == "A" and abs(i-j) > 1:
        i = j
        c += 1
    j += 1
print(c)