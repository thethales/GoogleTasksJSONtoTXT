import json

# GootleTaskJSONtoTXT - GTJT


def ConvertFile(file='Tasks.json'):
  try:
    with open(file,encoding='UTF8') as f:
      data = json.load(f)

    for item in data['items']:
      f = open("output/list_" + item["title"] +".txt", "w", encoding='UTF8')
      for task in item['items']:
          f.writelines(task["title"] + "\n")
      f.close()
  except ValueError as e:
      return False
  return True
