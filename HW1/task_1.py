# duration: int = int(input('Введите продолжительность: '))


duration = 0
counter = 0
while counter < 300000:
    duration +=1
    counter +=1
    if duration < 60:
        print(duration, 'сек')
    elif duration >= 60 and duration < 3600:
        minute = duration // 60
        seconds = duration % 60
        print(minute, 'мин', seconds, 'сек')
    elif duration >= 3600 and duration < 86400:
        hours = duration // 3600
        minute = (duration % 3600) // 60
        seconds = duration % 60
        print(hours, 'час', minute, 'мин', seconds, 'сек')
    elif duration >= 86400:
        days = duration // 86400
        hours = (duration % 86400) // 3600
        minute = ((duration % 86400) % 3600) // 60
        seconds = duration % 60
        print(days, 'день', hours, 'час', minute, 'мин', seconds, 'сек')


