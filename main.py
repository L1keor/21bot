start = int(input('Введите номер игры с которой начнете ставить: '))
stop = int(input('Введите номер игры на которой закончите ставить: '))
prognoz = []
sstavka = int(input('Введите сумму по сколько будете ставить: '))
rmmbr = ''
stavka = int(sstavka)
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

print('Масть игроку в', start, 'игре:', prognoz[1], 'Ставка:', stavka)

for i in range(1, len(prognoz)):
    chk = str(input('Заход или нет(+, -): '))
    if chk == '+':
        stavka = sstavka
        print('Масть игроку в', i + start, 'игре:', prognoz[i], 'Ставка:', stavka)
    elif chk == '-':
        rmmbr = prognoz[i-1]
        stavka *= 3
        print('Масть игроку в', i + start, 'игре:', rmmbr, 'Ставка:', stavka)
