for num in range(1, 101):
    if num % 100 >= 10 and num % 100 <= 20:
        print(num, 'процентов')
    elif num % 10 == 1:
        print(num, 'процент')
    elif num % 10 >= 2 and num % 10 <= 4:
        print(num, 'процента')
    else:
        print(num, 'процентов')