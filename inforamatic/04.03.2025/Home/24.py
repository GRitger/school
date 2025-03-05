with open("24.txt") as fil:
    st = fil.readline()

i = 1
j = 0
m = 0
while i <= len(st):
    temp = st[j:i]
    cx = temp.count("X")
    cy = temp.count("Y")
    if cx <= 5 and cy <= 5:
        i += 1
        m = max(m, len(temp))
    else:
        j += 1
print(m)