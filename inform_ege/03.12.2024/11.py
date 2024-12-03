with open ("11.txt") as f:
    s = f.readline()
print(len(s))
a = s.split("AXMM")
a.sort(key=len)
print(len(a[-1]))
#sdkpovpompompormemr
