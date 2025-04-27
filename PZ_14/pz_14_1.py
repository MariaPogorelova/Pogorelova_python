# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
# «произведение».
import re
old_word = re.compile("\bроман\b")
new_word = 'произведение'
with open('writer.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print(re.sub(old_word, new_word, text))

