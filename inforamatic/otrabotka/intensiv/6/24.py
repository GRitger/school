from string import ascii_lowercase
with open("24.txt")  as f:
    st = f.readline().lower()
    for i in ascii_lowercase:
        if i not in "abcd":
            st =st.replace(i, "*")

a = st.split("*")
a.sort(key=len)

for i in range(len(a)):
    while len(a[i]) > 0 and a[i][0] == "0":
        a[i] = a[i][1:]
a.sort(key=len)

print(st.find("2b7450450937681206413258079070926134580762180493504983671520053791264080395462810706739412850061592348700437d15c"))