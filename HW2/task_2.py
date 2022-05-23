my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(my_list):
    if my_list[i].isdigit() and my_list[i].isalnum():
        my_list.insert(i, '"')
        my_list[i + 1] = f'{int(my_list[i + 1]):02d}'
        my_list.insert(i + 2, '"')
        i += 2
    elif my_list[i][0] == "+" and my_list[i][-1].isdigit():
        my_list.insert(i, '"')
        my_list[i + 1] = f'+{int(my_list[i + 1]):02d}'
        my_list.insert(i + 2, '"')
        i += 2
    else:
        i += 1

print(' '.join(my_list))
