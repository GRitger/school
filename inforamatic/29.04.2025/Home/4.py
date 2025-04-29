from ipaddress import ip_network
c = 0
for i in ip_network("192.168.31.80/255.255.255.240"):
    st = f'{int(i) : 032b}'
    c = max(c, st.count("1"))
print(c)