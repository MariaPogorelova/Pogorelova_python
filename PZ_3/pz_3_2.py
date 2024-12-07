#Даны два числа. Вывести вначале большее, а затем меньшее из них.
a, b = input("Введите первое число: "), input("Введите второе число: ")

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

if a > b:
    print(a)
    print(b)
else:
    print(b)
    print(a)