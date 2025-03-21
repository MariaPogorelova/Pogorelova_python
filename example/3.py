#программа выводит каждую строчку построчно
try:
    f1 = open('text.txt', 'r', encoding='utf-8')
    for i in f1:
        print(i, end='')
except FileNotFoundError:
    print("ошибка! файл не найден")
