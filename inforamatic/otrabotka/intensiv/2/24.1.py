from string import ascii_lowercase

with open("24-347.txt") as f:
    st = f.readline().lower()

for i in ascii_lowercase:
    if i not in "ab":
        st = st.replace(i, "*")

a = st.split("*")
for i in range(len(a)):
    if len(a[i]) > 0 and a[i][0] == "0":
        a[i] = a[i][1:]
a.sort(key = len)

for i in a:
    if len(i) > 0:
        t = int(i, 12) % 11
        if t == 0:
            print(i, t)

print(st.find("4638075912032784596100638012594706928157034038129647050273485106908253407169090385741620352076419800058623") + len("4638075912032784596100638012594706928157034038129647050273485106908253407169090385741620352076419800058623"))