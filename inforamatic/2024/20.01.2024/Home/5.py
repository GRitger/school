from ipaddress import ip_network
n = 0
for ip in ip_network("192.168.32.160/255.255.255.240", False):
    st = f'{int(ip):32b}'
    if st.count("0") >21:
        n+=1
print(n)