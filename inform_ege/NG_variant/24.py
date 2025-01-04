with open ("24.txt") as f:
    c = 0
    for st in f:
        if st.count("S") == st.count("X"):
            c += 1
print(c)