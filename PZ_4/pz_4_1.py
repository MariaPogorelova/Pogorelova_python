#Дано вещественное число X и  целое число N (>0).
#Найти значение выражения 1 - X^2/(2!) + X^4/(4!) - ..... + ((-1)^N - X^2N)/((2-N)!)/ N!

X = float(input("Введите значение X (вещественное число): "))
N = int(input("Введите значение N (целое число, N > 0): "))
s = 0
sign = 1
n = 0
while n <= N:
    factorial = 1
    i = 1
    while i <= 2 * n:
        factorial *= i
        i += 1
    term = sign * (X ** (2 * n)) / factorial
    s += term
    sign *= -1
    n += 1
result = s + 1

print(f"Приближенное значение cos({X}): {result}")

