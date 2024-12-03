st = [1] *10

for i in range(2,11):
    j = 0
    while j < 10:
        if st[j] == 0:
            st[j] = 1
        else:
            st[j] = 0
        j += i
print(st)





