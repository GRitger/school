with open("24_21717.txt") as f:
    st = f.readline()

i = 0
j = 1
l = 10**10
ans = ""
while j < len(st):
    temp = st[i:j]
    if temp.count("RSQ") == 130 and temp[-1] != "Q":
        l = min(l, len(temp))
        i += 1
        ans = temp
    else:# temp.count("RSQ") < 130:
        j += 1

print(l, temp)