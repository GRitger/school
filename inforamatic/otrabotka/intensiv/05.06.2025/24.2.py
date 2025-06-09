def fu(qwert):
    s = qwert
    flag = False
    while len(s):
        arr = [int(x) for x in s.split("=") if len(x) > 0]
        for i in range(len(arr) -1):
            if arr[i] == arr[i+1]:
                return True, s
        if not flag:
            s = s[1:]
    else:
        s = qwert
        while len(s):
            arr = [int(x) for x in s.split("=") if len(x) > 0]
            for i in range(len(arr) - 1):
                if arr[i] == arr[i + 1]:
                    return True, s
            if not flag:
                s = s[:-1]
    return flag

with open("24-320.txt") as f:
    st = f.readline()
while "==" in st:
    st = st.replace("==", " ")

a = st.split()
for i in range(len(a)):
    if len(a[i]) > 1:
        if a[i][0] == "=":
            a[i] = a[i][1:]
        if a[i][-1] == "=":
            a[i] = a[i][:-1]

a.sort(key= len, reverse=True)
for i in a:
    z = fu(i)
    if z[0]:
        print(len(z[1]), z[1])
        break