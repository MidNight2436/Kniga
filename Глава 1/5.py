spisok = []
for k in range(0, 10):
    print(k*5 + 3)
    x = 5*k + 3
    if x % 5 == 3:
        spisok.append(x)
print(spisok)
print(sorted(spisok, reverse=True))
