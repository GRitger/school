from ipaddress import ip_network

n = 0
for ip in ip_network("176.112.100.128/255.255.255.224", False):
    s = f'{int(ip):032b}'
    if s.count("1") % 2 :
        n += 1
print(n)