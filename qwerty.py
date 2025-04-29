import requests
for i in range(40):
    r = requests.get('http://31.135.225.58:10040')
    print(i, r)
