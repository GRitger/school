def f(x):
    st = ""
    while x:
        st = str(x%7) + st
        x = x//7
    return st
n = 0
for x in range(1,1000):
    st = f(7**666 + 7**333 + 49**x -343)
    if st.count("6") == 49:
        print(x)
        break

