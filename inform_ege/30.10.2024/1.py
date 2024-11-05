from itertools import product
count = 0
st = "0123456789abcdef"
for i in product('нч', repeat=8):
    x = "".join(i)
    if x.count('ч')==3:
        if x[0]=='ч':
            count+=7*8**7
        else:
            count+=8**8
print(count)