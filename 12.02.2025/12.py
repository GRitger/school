
st = "1"*2026
while "11111" in st or "222" in st:
    if "11111" in st:
        st = st.replace("11111", "22")
    else:
        st= st.replace("222", "2")

print(st)