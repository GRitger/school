from ipaddress import *

c = 0
for ip in ip_network('156.178.54.144/255.255.255.240', False):
    one = f'{int(ip) : 32b}'
    if one.count("111") > 0:
        c += 1
print(c)
