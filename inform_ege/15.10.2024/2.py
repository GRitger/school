from ipaddress import ip_network

n = 0
for ip in ip_network("192.168.240.0/255.255.255.0", False):
    s = f'{int(ip):032b}'
    if s.count("1") == s.count("0"):
        n += 1
print(n)