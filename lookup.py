import csv

query = input('Search: ')

for word, result in csv.reader(open('data.csv', 'r', newline='')):
  if word == query:
    print(result)
