nums = {}

for i in range(2, 10):
    nums[i] = []
    for a in range(2, 100):
        if a % i == 0:
            nums[i].append(a)

    print(f'Для числа {i}, кратны {len(nums[i])} чисел, эти числа {nums[i]}')
