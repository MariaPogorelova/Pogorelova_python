# В двумерном списке найти сумму элементов первых двух строк.
a = [[0] * 7 for i in range(5)]
k = 0
for i in range(5):
   for j in range(6, -1, -1):
       a[i][j] = k
       k += 1

print(*a, sep='\n')