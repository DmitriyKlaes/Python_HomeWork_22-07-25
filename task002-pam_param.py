# пара-ра-рам рам-пам-папам па-ра-па-дам (текст задачи отдельно в файле)


def sense_of_rhythm(chant):
    import re
    count = [len(re.findall(r'[ауоыиэяюёе]', x)) for x in chant]
    if all(x == count[0] for x in count):
        print('Парам пам-пам')
    else:
        print('Пам парам')
        
        
sense_of_rhythm(input('Введите кричалку: ').split())


# от препода

def check(text):
    sets = set()
    for i in text.split():
        count = 0
        for j in i:
            if j in 'ауоыиэяюёе':
                count += 1
        sets.add(count)
    if len(sets) == 1:
        return 'yes'
    return 'no'


text = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
print(check(text))
