
def thesaurus_adv(*names):
    out_info = {}
    for name in names:
        ls = name.split()
        out_info.setdefault(ls[1][0], {})
        out_info[ls[1][0]].setdefault(ls[0][0], [])
        out_info[ls[1][0]][ls[0][0]].append(name)
    return out_info

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))