# 2. Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить строку
# наибольшей длины.
t = 0
d = 0
max_line = 0
for i in open('text18-20.txt', encoding='utf-8'):
    print(i, end='')
    if len(i) > max_line:
        longest = i
        max_line = len(i)
        print(i)
    for j in i:
        d += 1
print(end='\n')
print('Количество символов: ', d, end='\n')
print(f"строка наибольшей длины: {max_line}")
f1 = open('text18-20.txt', encoding="utf-8")