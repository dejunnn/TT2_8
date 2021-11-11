import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes":10, "name": "Jim", "views": 10},{"likes":40, "name": "Cim", "views": 10000},
#         {"likes":20, "name": "Aim", "views": 100},{"likes":50, "name": "Dim", "views": 100000},
#         {"likes":30, "name": "Bim", "views": 1000},{"likes":60, "name": "Eim", "views": 1000000}]

data = json.loads(open('user.json').read())

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())