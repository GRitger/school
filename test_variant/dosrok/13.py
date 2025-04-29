from ipaddress import ip_network
for i in ip_network("143.168.72.213/255.255.255.240", False).hosts():
    print(i)