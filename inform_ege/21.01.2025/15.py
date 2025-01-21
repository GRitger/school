with open("15.txt") as f:
    st = f.readline()

j = 0
i = 1
F = 0
a = []
while i < len(st):
    temp = st[j:i]
    F = True
    for q in range(len(temp)-1):
        if temp[q] > temp[q + 1] or temp.count("A") + temp.count("E") + temp.count("I") + temp.count("O") + temp.count(
                "U") + temp.count("Y") > 1:
            F = False
            break
    if not F:
        j += 1
    else:
        if len(temp) == 10:
            print(temp)
        a.append(i-j)
        i += 1

print(max(a))
