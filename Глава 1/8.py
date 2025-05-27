n = int(input("Введите колличество элементов в последовательности Фибоначи: "))
spisok = [1, 1]
i = 1
x = 1
y = 1
while i <= n:
    s = x + y
    spisok.append(s)
    y = x
    x = s
    i += 1
print(spisok)