from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
for item in contacts_list:
  newstr = ' '.join(item[:3]).split(' ')
  print(newstr)


pattern = r"(8|\+7)?\s*\((\d+)\)\s*(\d+)(-|\s)(\d+)(-|\s)(\d+)"
# phones_list = re.findall(pattern, el)
# print(phones_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)