start = int(input('Введите номер игры с которой начнете ставить: '))
stop = int(input('Введите номер игры на которой закончите ставить: '))
prognoz = []
for i in range(start, stop+1):
    if i > 25:
        n = i - 26
    else: n = 150 + i - 26
    res = input('Введите первую масть игрока в %d игре (п, ч, т, б): ' % n)
    if res == 'ч':
        prognoz.append('Черви')
    elif res == 'п':
        prognoz.append('Пики')
    elif res == 'т':
        prognoz.append('Трефы')
    elif res == 'б':
        prognoz.append('Бубны')
    else: prognoz.append('Хз')

for i in range(len(prognoz)):
    print('Масть игроку в', i+start, 'игре:', prognoz[i])