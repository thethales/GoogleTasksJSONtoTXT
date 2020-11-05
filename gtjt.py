import json

# GootleTaskJSONtoTXT - GTJT


def removeSpecialChars(str):
  return ''.join(e for e in str if e.isalnum())

def ConvertFile(file='Tasks.json',output_dir='output'):
  try:
    with open(file,encoding='UTF8') as f:
      data = json.load(f)

    for item in data['items']:
      f_title = output_dir + "/list_" +  removeSpecialChars(item["title"]) + ".txt"
      f = open( f_title, "w", encoding='UTF8')
      for task in item['items']:
          f.writelines(task["title"] + "\n")
      f.close()
  except ValueError as e:
      return False
  return True


