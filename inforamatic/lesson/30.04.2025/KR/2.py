from fnmatch import fnmatch

for i in range(1, 10**8+1):
    if i < 10**8 and fnmatch(str(i), "1*2??76") and i % 1923 == 0:
        print(i, i // 1923)