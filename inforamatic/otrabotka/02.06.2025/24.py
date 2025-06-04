from string import ascii_lowercase
with open("24-278.txt") as f:
    st = f.readline().lower()
    alf = "qazwsxedcrvtgbyhujmiop13579"
    for i in alf:
        st = st.replace(i, "*")

#print(st)
i = 882441
j = 882442
ans1 = 0
ans2 = ""
print(st.find("2FKLKLLKNNLFKFNKFKLNFFKKLLNFFFLKNNFKNNNNKKNFLNKLKNFKNLFNNF".lower()))
while j < len(st):
    temp = st[i:j+1]
    if len(temp) == 5000:
        qwe = 23131
    #print(i,j)
    if st[i] == st[j] and st[i] in "02468" and temp.count("0") + temp.count("2")+temp.count("4")+temp.count("6")+temp.count("8") == 2:
        if len(st[i:j+1]) > ans1:
            ans1 = len(st[i:j+1])
            ans2 = st[i:j+1]
            print(ans2)
        else:
            i = j
            j += 1
    if st[i:j+1].count("*") == 0:
        j += 1
    else:
        i = j
        j += 1
