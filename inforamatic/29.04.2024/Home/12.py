from ipaddress import ip_network
c = 0
for i in ip_network("172.16.168.0/255.255.255.128", False).hosts():
    print(i)
    break