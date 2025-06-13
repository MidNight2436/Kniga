n = int(input("Ведите длинну списка "))
spisok = []
i = 0
while i + 1 <= n:
    i += 1
    spisok.append(i)

def summa():
    n = 0
    for i in range(0, len(spisok)):
        if spisok[i] % 2 == 1:
            n += spisok[i]
    return(n)

print(spisok)
print(summa())



n = int(input("Введите длину списка "))
spisok = list(range(1, n+1))
print(spisok)
print(sum(i for i in spisok if i % 2 == 1))
