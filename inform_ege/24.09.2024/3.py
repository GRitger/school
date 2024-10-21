with open("26_3.txt") as fal:
    N = int(fal.readline())
    mas_l = [int(i) for i in fal]

N = N//4
mas_l.sort()
s = sum(mas_l)
for i in range(N):
    s -= mas_l[i] * 0.5
print(s)

mas_l.sort(reverse=True)
s = sum(mas_l)
for i in range(N):
    s -= mas_l[i] * 0.5
print(s)