ls = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in ls:
    name = i.split()
    print(f'привет, {name[-1].title()}!')
