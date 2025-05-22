from string import ascii_lowercase, digits
alf = digits + ascii_lowercase
with open("24-345.txt") as f:
    st = f.readline().lower()

al = '0123456789ab'
for i in alf:
    if i not in al:
        st = st.replace(i,"*")
a = st.split("*")
a.sort(key=len)
for i in a:
    print(i, len(i))
print(st.find("50941682035703092451678035068274190648079532107589206143081270549360457306198205783120469034657219080000b8a9"))

