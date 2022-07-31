# пара-ра-рам рам-пам-папам па-ра-па-дам (текст задачи отдельно в файле)


def sense_of_rhythm(chant):
    import re
    count = [len(re.findall(r'[ауоыиэяюёе]', x)) for x in chant]
    if all(x == count[0] for x in count):
        print('Парам пам-пам')
    else:
        print('Пам парам')
        
        
sense_of_rhythm(input('Введите кричалку: ').split())