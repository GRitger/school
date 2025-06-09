from string import ascii_lowercase
with open("24-294.txt") as f:
    st = f.readline().lower()
for i in ascii_lowercase:
    st = st.replace(i, "*")
for i in "13579":
    st = st.replace(i+i, i+"*"+i)
i = 0
j = 1
ans1 = 0
ans2 = ""
while j < len(st):
    temp = st[i:j]
    if temp.count("*") > 0:
        i = j
        j += 1
    else:
        if temp.count("7") < 80:
            j += 1
        elif temp.count("7") == 80:
            if len(temp) > ans1:
                ans1 = len(temp)
                ans2 = temp
            j +=1
        else:
            i += 1
print(ans1, ans2)