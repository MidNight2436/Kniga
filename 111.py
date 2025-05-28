number = int(input("Введите число 1: "))
print("Делится на", 1)
k = 1
while k < number // 2:
    k = k + 1
    if number % k != 0:
        continue
    print("Делится на", k)
print("Делится на", number)


number = int(input("Введите число 2: "))
k = 1
while k < number // 2:
    if number % k == 0:
        print("Делится на", k)
    k = k + 1
print("Делится на", number)