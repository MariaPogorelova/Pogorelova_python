#Дано целое число N (>0)
#Найти сумму 1^1 + 2^2 + N^N

N = int(input("Введите целое число: "))
total_sum = 0
i = 1

while i <= N:
    total_sum = total_sum + i ** i
    i += 1

print(total_sum)