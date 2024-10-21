from ipaddress import *

c = 0
for ip in ip_network('128.224.31.192/255.255.255.192', False):
    nul = len(bin(int(ip))[2:]) - bin(int(ip))[2:].count("1")
    if nul**0.5 == int(nul**0.5):
        c += 1
print(c)
