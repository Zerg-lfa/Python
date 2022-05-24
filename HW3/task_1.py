numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def  num_translate(num):
    return numbers.get(num)

for i in numbers:
    print(num_translate(i))

# эксперементы с лямбдой , такое решение в теории тоже верно ?
print(list(map(lambda num: numbers.get(num), numbers)))



def num_translate_adv(num):
    if num.istitle():
        num = num.lower()
        return numbers.get(num).capitalize()
    return numbers.get(num)




print(num_translate_adv('one'))

