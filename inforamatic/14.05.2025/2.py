with open("2.txt") as f:
    st = f.readline()

l = len(st)
for j in range(100, 1, -1):
    for i in "QAZWSXEDCRFVTGBYHNUJMIKLOP":
        st = st.replace(i*j, f'{j}{i}' )
print(8*(l - len(st)))