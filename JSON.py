import json

# это наши данные, которые я взяла из новеллки
# но я перевела их на английский потому что на русском не читаются данные
friends = {
    'first': 'You',
    'second': 'Vasia',
    'third': 'Katya'
}
# это запись наших данных
with open('friend.json', 'w') as file:
    json.dump(friends, file, indent=4)

# это удаление какиех-то определенных данных
with open('friend.json', 'r') as file:
    friends = json.load(file)
del friends["third"]

with open('friend.json', 'w') as file:
     json.dump(friends, file, indent=4)

import csv

friends = [
    ['You'],
    ['Vasia'],
    ['Katya']
]
with open('friend.csv', 'w', newline = '') as file:
    writer = csv.writer(file)

    for frrr in friends:
        writer.writerow(frrr)