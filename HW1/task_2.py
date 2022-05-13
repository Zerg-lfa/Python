numbers_cub = []

for number in range(1, 1000, 2):
    cub = number ** 3
    numbers_cub.append(cub)

for number in numbers_cub:
    amounts = 0
    for num in str(number):
        amounts = amounts + int(num)
    if amounts % 7 == 0:
        print(amounts)

print(numbers_cub)


i = 0
for num in numbers_cub:
    num = num + 17
    numbers_cub[i] = num
    i += 1

for number in numbers_cub:
    amounts = 0
    for num in str(number):
        amounts = amounts + int(num)
    if amounts % 7 == 0:
        print(amounts)


print(numbers_cub)