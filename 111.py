nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(nums)
#del nums[len(nums)-1]
#print(nums)
del nums[-1]
print(nums)

print(list(reversed(nums)))

nums = [2*k+1 for k in range(7)]
print(nums)
print(sorted(nums, reverse=True))

numbers = list(range(1, 10,))
print(numbers)

for number in range(1, 10):
    print(number)