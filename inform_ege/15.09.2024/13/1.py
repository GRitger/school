from ipaddress import *
c = 0
for ip in ip_network('192.168.32.160/255.255.255.240',0):
    if bin(int(ip))[2:].count("1") % 2 == 0:
        c += 1
print(c)