def task1():
    chisla = [1, 2, 15, 19, 37]
    n = int(input('введите число: '))
    if n in chisla:
        print('исходный список: ', chisla)
        print('введенное число: ', n)
        print('Поздравляю, Вы угадали число!')
    else:
        print('сходный список: ', chisla)
        print('введенное число: ', n)
        print('Нет такого числа!')
def task2():
    chisla = [1, 2, 3, 2, 5, 6, 8, 6, 10]
    povtori = set([x for x in chisla if chisla.count(x) > 1])
    print('повторяющихся чисел в списке: ', povtori)

# def task22():
#     chisla = [1, 2, 3, 2, 5, 6, 8, 6, 10]
#     povtori = []
#     for i in chisla:
#         if chisla.count(i) > 1:
#             povtori.append(i)
#     povtorii = set(povtori)
#     print('повторяющихся чисел в списке: ', povtorii)

def task3():
    dni = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
    otdyh = int(input('сколько выходных дней вы хотите иметь на неделе? '))
    weekends = dni[-otdyh:]
    rabota = dni[:-otdyh]
    print('ваши выходные дни: ', weekends)
    print('ваши рабочие дни: ', rabota)

def task4():
    group20 = ['Иванов', 'Петров', 'Сидоров', 'Кузьменко', 'Орлова', 'Озерова', 'Дегтярева', 'Вол', 'Демченко', 'Яблонев']
    group25 = ['Зеленый', 'Семенов', 'Белкина', 'Иванов', 'Захарова', 'Петрова', 'Бойцев', 'Калмычек', 'Токарева', 'Поспелова']
    football = tuple(group20[:5] + group25[:5])
    print('группа 20: ', group20)
    print('группа 25: ', group25)
    print('футбольная команда: ', football)
    print(len(football))
    football = sorted(football)
    print(football)
    ivanov = football.count('Иванов')
    print('в команде с фамилией "Иванов" ', ivanov, ' человек(a)')
task1()
task2()
task3()
task4()