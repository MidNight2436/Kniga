count = int(input('Введите колличество степеней двойки '))
spisok = []
for i in range(0, count + 1):
    x = 2 ** i
    spisok.append(x)
print(f'Список степеней двойки {spisok}')