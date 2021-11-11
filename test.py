import requests

BASE = "http://127.0.0.1:5000/"


data1 = json.loads(open('user.json').read())
data2 = json.loads(open('project.json').read())
data3 = json.loads(open('expense.json').read())
data4 = json.loads(open('category.json').read())

for i in range(len(data1)):
    response1 = requests.put(BASE + "user/" + str(i), data1[i])
    print(response1.json())

for i in range(len(data2)):
    response2 = requests.put(BASE + "project/" + str(i), data2[i])
    print(response2.json())

for i in range(len(data3)):
    response3 = requests.put(BASE + "expense/" + str(i), data3[i])
    print(response3.json())

for i in range(len(data4)):
    response4 = requests.put(BASE + "category/" + str(i), data4[i])
    print(response4.json())