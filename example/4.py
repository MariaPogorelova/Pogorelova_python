# Запишем в файл data_3.txt структуру данных - список
l = ['-99 6 12 -36 20 45 100 -15']
f3 = open('data_3.txt', 'w')
f3.writelines(l)
f3.close()
# Дублируем список в новый файл data_4.txt
f4 = open('data_4.txt', 'w')
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()
# разбиваем строку и ее значения преобразуем в числа
f3 = open('data_3.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()
# Ищем максимальный элемент и количество отрицательных элементов
# в файле data_3.txt и записываем в файл data_4.txt
f3 = open('data_3.txt')
max, t = 0, 0
for i in range(len(k)):
    max = max if max > k[i] else k[i]
    if k[i] < 0:
        t += 1
f4 = open('data_4.txt', 'a') # открываем файл для дозаписи
f4.write('\n')
print('Количество элементов: ', len(k), 'Максимальный элемент: ', max, file=f4)
f4.close()