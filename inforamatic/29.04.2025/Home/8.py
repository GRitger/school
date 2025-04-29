from ipaddress import ip_network
c = 0
for i in ip_network("135.13.142.29/255.255.255.128", False).hosts():
    print(i)
    break