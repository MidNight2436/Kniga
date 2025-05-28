number = int(input("Введите число: "))
num = number // 2
k = 2
while k < num:
    if number % k == 0:
        print("Число не явялется простым")
        break
    else: k = k + 1
else:
    print("Число является простым")
print("Проверка завершена")