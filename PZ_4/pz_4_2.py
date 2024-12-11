#Дано целое число N (>0)
#Найти сумму 1^1 + 2^2 + N^N

N = input("Введите целое число N: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Ошибка!")
        N = input("Введите целое число N: ")

if N <= 0:
    print("Ошибка: N должно быть больше нуля")
else:
    total_sum = 0
    i = 1
    while i <= N:
        total_sum = total_sum + i ** i
        i += 1

    print(total_sum)
