count = int(input('Введите колличество степеней двойки '))
spisok = []
for i in range(0, count + 1):
    x = 2 ** i
    spisok.append(x)
print(f'Список степеней двойки {spisok}')



count = int(input('Введите количество степеней двойки '))
spisok = [2**i for i in range(count + 1)]
print(f'Список степеней двойки {spisok}')