def task1():
    countries = {"Россия": "Москва", "Бельгия": "Брюссель", "Испания": "Мадрид", "Италия": "Рим", "Аргентина": "Буэнос-Айрес"}
    for country, capital in countries.items():
        print(country, '-', capital)
    print('----------------------------------------')
    country = "Испания"
    print(countries[country], '- столица', country)
    print('----------------------------------------')
    scountries = sorted(countries.keys())
    for country in scountries:
        print(country, '-', countries[country])

def task2():
    words = {"А": "1", "В": "1", "Е": "1", "И": "1", "Н": "1", "О": "1", "Р": "1", "С": "1", "Т": "1", \
             "Д": "2", "К": "2", "Л": "2", "М": "2", "П": "2", "У": "2", \
             "Б": "3", "Г": "3", "Ё": "3", "Ь": "3", "Я": "3", \
             "Й": "4", "Ы": "4",
             "Ж": "5", "З": "5", "Х": "5", "Ц": "5", "Ч": "5", \
             "Ш": "8", "Э": "8", "Ю": "8", \
             "Ф": "10", "Щ": "10", "Ъ": "10"}
    def calcul(word):
        count = 0
        for bukva in word.upper():
            count += int(words.get(bukva, 0))
        return count
    word = input('введите слово: ')
    print('стоимость вашего слова:', word, '=', calcul(word))

def task3():
    students = {"Софья": ("русский", "английский"), "Анастасия": ("русский", "английский", "латынь", "китайский"), \
                "Евгений": ("испанский", "английский", "китайский")}
    kit = []
    alllang = set()
    for student, languages in students.items():
        alllang.update(languages)
        if 'китайский' in languages:
            kit.append(student)
    print('количество различных языков:', len(alllang))
    print('сортированный список всех языков:', sorted(alllang))
    print('студенты, знающие китайский язык:', kit)
task3()
