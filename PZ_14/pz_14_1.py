# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
# «произведение».
import re
surname = r'^([\w\-]+)'
with open('writer.txt','r', encoding='utf-8') as file:
    text = file.read()

all_surnames = set(re.findall(surname, text, re.MULTILINE))
count_surnames = len(all_surnames)
print('Фамилии писателей: ', all_surnames)
print('Количество фамилий: ', count_surnames)
new_words = text.replace('роман', 'произведение')

with open('new_writer.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(new_words)

