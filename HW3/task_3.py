

def thesaurus(*names):
    out_info = {}
    for name in names:
        out_info.setdefault(name[0], [])
        out_info[name[0]].append(name)
    return out_info


list = thesaurus("Иван", "Мария", "Петр", "Илья", "Андрей", "Егор", "Елисей")
print(list)
print(sorted(list.keys()))


# print(thesaurus("Иван", "Мария", "Петр", "Илья", "Андрей", "Егор", "Елисей"))
