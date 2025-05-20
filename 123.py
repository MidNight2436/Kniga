def sqsum(n):
    nums = [k*k for k in range(1, n+1)]
    return sum(nums)
m = 10
print('Сумма квадратов чисел от 1 до', str(m)+':', sqsum(m))

