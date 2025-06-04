from ipaddress import ip_network
n = 0
for ip in ip_network("119.124.96.0/255.255.240.0", False):
    st = f'{int(ip):32b}'
    if st[-1] == "0":
        n+=1
print(n)