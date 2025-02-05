from fnmatch import *

def qwe(x):
    s = 0
    while x:
        s += x% 10
        x //= 10
    return s

ch = 700000
n  = 0
a = []
while n < 5:
    ch += 1
    f = str(ch)[-1] != 2 and str(ch)[-4] != 4
    if ch % 13 == 0 and str(ch).count("1") == 0 and f and not(fnmatch(str(ch), "*0??3*")):
        print(ch, qwe(ch) )
        n+= 1
