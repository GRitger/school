from ipaddress import ip_network
c =0
for i in ip_network("115.192.0.0/255.192.0.0",False):
    st = f'{int(i): 032b}'
    if st.count("1") % 3:
        c += 1

print(c)
