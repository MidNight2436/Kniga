n = int(input('Введите число для факториала: '))
i = 1
x = 1
while i <= n:
    x *= i
    i += 1
print('Факториал числа '+ str(n)+' равен '+ str(x))