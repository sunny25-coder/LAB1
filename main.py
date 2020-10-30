import re

address = open('email.TXT', 'r') #исходный файл
result = open('result.txt', 'w') #файл с результатом


template = '@([A-Za-z0-9]+)' #шаблон в формате группы регулярных выражений

line = address.readlines()
data = []
for i in range(len(line)):
    flag = 0
    if line[i].strip():
        domain = re.findall(template, line[i])
        if i == 0:  #если первый домен в списке,сравнивать не с чем
            data.append(domain[0])
        else:
            for j in data:
                if j == domain[0]:
                    flag = 1
                    break
            if flag == 0: #если повторений не нашлось, добавляем
                data.append(domain[0])

for h in data:
    result.write(h + '\n')

address.close()
result.close()