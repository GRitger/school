from ipaddress import ip_network

c = 0
for i in ip_network("151.192.0.0/255.224.0.0"):
    st = f'{bin(int(i))}:32b'
    if st.count("1") == 16:
        c+= 1
print(c)