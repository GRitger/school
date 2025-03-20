from ipaddress import ip_network
c = 0
for ip in ip_network("200.33.100.0/255.255.248.0",0):
    b = f'{int(ip): 032b}'
    if b.count("1") % 7:
        c += 1
print(c)