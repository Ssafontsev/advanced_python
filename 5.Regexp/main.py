import csv
import re
from pprint import pprint

PHONE_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB = r'+7(\2)-\3-\4-\5 \6\7'

def open_file():
  with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
  return contacts_list

def formatting_names():
  new_list = list()
  for item in open_file():
    full_name = ' '.join(item[:3]).split(' ')
    print(full_name)
    result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
              re.sub(PHONE_PATTERN, PHONE_SUB, item[5]), item[6]]
    new_list.append(result)
  return new_list

def reformatting():
  new_list = formatting_names()
  for contact in new_list:
    first_name = contact[0]
    last_name = contact[1]
    for new_contact in new_list:
      new_first_name = new_contact[0]
      new_last_name = new_contact[1]
      if first_name == new_first_name and last_name == new_last_name:
        if contact[2] == "":
          contact[2] = new_contact[2]
        if contact[3] == "":
          contact[3] = new_contact[3]
        if contact[4] == "":
          contact[4] = new_contact[4]
        if contact[5] == "":
          contact[5] = new_contact[5]
        if contact[6] == "":
          contact[6] = new_contact[6]
  result_list = list()
  for i in new_list:
    if i not in result_list:
      result_list.append(i)
  return result_list

def saving_csv():
  with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(reformatting())
  return

if __name__ == '__main__':
  saving_csv()