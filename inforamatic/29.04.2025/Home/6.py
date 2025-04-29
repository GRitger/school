from ipaddress import ip_network
c = 0
for i in ip_network("83.152.68.115/255.255.224.0", False).hosts():
    print(i)