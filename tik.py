#praktika2
def task1():
    pin1 = input("Введите пароль: ")
    pin2 = input("Повторите введеный пароль: ")
    if pin1 == pin2:
        print("Пароль принят")
    else:
        print("Пароль не принят")

task1()

def task2():
    mesto = int(input("Введите место в вагоне: "))
    if 1 <= mesto <= 36:
        if mesto % 2 == 0:
            print("Верхнее место в купе")
        else:
            print("Нижнее место в купе")
    else:
        if mesto % 2 == 0:
            print("Верхнее боковое место")
        else:
            print("Нижнее боковое место")

def task3():
    year = input("Введите какой сейчас год: ")
    if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
        print("Год " + year + " - високосный")
    else:
        print("Это год не високосный")

def task4():
    color1 = input("Введите название цвета: ")
    color2 = input("Введите название цвета: ")
    if color1 == ('желтый' or color1 == 'Желтый' or color1 == 'жёлтый' or color1 == 'Жёлтый' or color1 == 'ЖЕЛТЫЙ' or color1 == 'ЖЁЛТЫЙ') and \
            (color2 == 'красный' or color2 == 'Красный' or color2 == 'КРАСНЫЙ'):
        print('Оранжевый')
    elif (color1 == 'желтый' or color1 == 'Желтый' or color1 == 'жёлтый' or color1 == 'Жёлтый' or color1 == 'ЖЕЛТЫЙ' or color1 == 'ЖЁЛТЫЙ') and \
            (color2 == 'синий' or color2 == 'Синий' or color2 == 'СИНИЙ'):
        print('Зеленый')
    elif (color2 == 'желтый' or color2 == 'Желтый' or color2 == 'жёлтый' or color2 == 'Жёлтый' or color2 == 'ЖЕЛТЫЙ' or color2 == 'ЖЁЛТЫЙ') and \
            (color1 == 'красный' or color1 == 'Красный' or color1 == 'КРАСНЫЙ'):
        print('Оранжевый')
    elif (color2 == 'желтый' or color2 == 'Желтый' or color2 == 'жёлтый' or color2 == 'Жёлтый' or color2 == 'ЖЕЛТЫЙ' or color2 == 'ЖЁЛТЫЙ') and \
            (color1 == 'синий' or color1 == 'Синий' or color1 == 'СИНИЙ'):
        print('Зеленый')
    elif (color1 == 'синий' or color1 == 'Синий' or color1 == 'СИНИЙ') and (color2 == 'красный' or color2 == 'Красный' or color2 == 'КРАСНЫЙ'):
        print('Фиолетовый')
    elif (color2 == 'синий' or color2 == 'Синий' or color2 == 'СИНИЙ') and (color1 == 'красный' or color1 == 'Красный' or color1 == 'КРАСНЫЙ'):
        print('Фиолетовый')
    else:
        print('Ошибка, введите цвета еще раз!')

#praktika3
def task31():
    n = int(input('Введите количество слов: '))
    itog = ''
    while n > 0:
        slovo = input('Введите слово: ')
        itog += slovo + ' '
        n -= 1
    print(itog)

def task32():
    slovo = 't'
    itog = ''
    while slovo != 'stop':
        slovo = input('Введите слово: ')
        if slovo != 'stop':
            itog += slovo + ' '
    print(itog)

def task33():
    slovo = input('Введите слово: ')
    if 'ф' in slovo or 'Ф' in slovo:
        print('Ого! Это редкое слово!')
    else:
        print('Эх, это не очень редкое слово...')

#
def task34():
    from random import randint
    mistakes = 0
    good = 0
    while mistakes < 3:
        a = randint(1, 30)
        b = randint(1, 30)
        print(str(a) + ' + ' + str(b) + ' =')
        otvet = input("Ответ: ")
        if otvet == str(a + b):
            good += 1
            print('Правильно!')
        else:
            mistakes += 1
            print('Ответ неверный')
    print('Игра окончена. Правильных ответов: ' + str(good))

