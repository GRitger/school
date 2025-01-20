from ipaddress import ip_network
n = 0
for ip in ip_network("124.8.0.0/255.248.0.0", False):
    st = f'{int(ip):32b}'
    n = max(st.count("0"), n)
print(n)