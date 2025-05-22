from fnmatch import fnmatch

for i in range(1, 10**8+1):
    if i < 10**8 and fnmatch(str(i), "12*34?5") and i % 2025 == 0:
        print(i, i // 2025)