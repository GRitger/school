with open ("H9po-M08oq.txt") as f:
    st = f.readline()
ans = 0
a = st.split("&")
for i in range(len(a)-1):
    if i == 73168:
        rmgowmgpo = 87
    b = 0
    k1=k2=""
    temp = a[i].split(".")
    if len(temp) > 1 and len(temp[-2]) >=4 and temp[-2][-4] != "0" and len(temp[-1]) >= 1 :
        b += 4+1+len(temp[-1])
        k1 =temp[-2][-4:]+"."+temp[-1]
        temp = a[i+1].split(".")
        if len(temp) > 1 and len(temp[0]) == 4 and temp[0][0] != "0" and len(temp[1]) >=1:
            b += 4 + 2 + len(temp[1])
            ans = max(ans, b)
            k2 = temp[0]+"."+temp[1]
    if b > ans:
        ans = b
        print(k1+"&"+k2, i)
print(ans)