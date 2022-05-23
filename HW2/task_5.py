prices = [57.8, 46.51, 97, 23.1, 56, 84.11, 65.34, 45.07, 48, 15.12, 69.5, 73.06]

print(id(prices))
prices.sort()
print(id(prices))

for price in prices:
    if type(price) == float:
        rub = int(price)
        kop = str(price % 1)[2:4]
        print(f'{rub}руб {int(kop):02d}коп', end= '; ')
    else:
        rub = int(price)
        kop = 0
        print(f'{rub}руб {int(kop):02d}коп', end='; ')




prices_rev = prices.copy()

print(end='\n')

prices_rev.reverse()
print(prices_rev)

print(prices_rev[:5])