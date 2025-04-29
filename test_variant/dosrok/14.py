st = "0123456789QAZWSXEDCRFVTGBYHNUJMIKOLP"
st = sorted(st)[:21]
for i in st:
    s = int(f'82934{i}2',21) + int(f'2924{i}{i}7',21) + int(f'67564{i}8',21)
    if s % 20 == 0:
        print(s // 20)