# 2. Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить строку
# наибольшей длины. fg
t = 0
d = 0
for i in open('text18-20.txt', encoding='utf-16'):
    print(i, end='')
    for j in i:
        d += 1
print(end='\n')
print('Количество символов: ', d, end='\n')
f1 = open('text18-20.txt', encoding='utf-16')
f1.close()
f2 = open('new_text18-20.txt', 'w')
f2.close()