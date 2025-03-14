# 2. Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить строку
# наибольшей длины.
t = 0
d = 0
for i in open('text18-20.txt', encoding='utf-16'):
    print(i, end='')
    for j in i:
        d += 1
print(end='\n')
print('Количество символов: ', d, end='\n')
# разбиваем строку и ее значения преобразуем в числа
f1 = open('text18-20.txt', encoding='utf-16')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

f1.close()
f2 = open('new_text18-20.txt', 'w')
f2.close()