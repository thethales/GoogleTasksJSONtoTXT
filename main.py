import json


with open('Tasks.json',encoding='UTF8') as f:
  data = json.load(f)

for item in data['items']:
    f = open("output/list_" + item["title"] +".txt", "w", encoding='UTF8')
    for task in item['items']:
        f.writelines(task["title"] + "\n")
    f.close()
