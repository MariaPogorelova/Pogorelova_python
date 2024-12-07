#Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара взаимно противоположных.
a, b, c = input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите третье число: ")

if (a == -b) or (a == -c) or (b == -c):
    print("true")
else:
    print("false")