from ipaddress import ip_network


for ip in ip_network("218.194.82.148/255.255.255.192", False):
    print(ip)