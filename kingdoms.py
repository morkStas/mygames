from random import *
import sys

# Домашний недельный проект игра государства. Идея и разработка: Иван Полстянов

res = (  # главный игровой кортеж
    "уголь", "уголь", "уголь", "уголь", "нефть", "нефть", "нефть", "нефть", "газ", "газ", "газ", "газ",
    "металлы", "металлы", "металлы", "металлы", "дерево", "дерево", "дерево", "дерево", "дерево", "дерево",
    "металлы", "металлы", "вода", "вода", "вода", "вода", "вода", "вода", "уголь", "уголь", "нефть", "нефть",
    "газ", "газ", "НАУКА", "НАУКА", "НАУКА", "НАУКА", "НАУКА", "НАУКА", "НАУКА", "НАУКА", "НАУКА", "НАУКА", "НАУКА",
    "ЛОТЕРЕЯ", "ЛОТЕРЕЯ", "ЛОТЕРЕЯ", "ДЕНЬГИ", "ДЕНЬГИ", "ДЕНЬГИ", "ДЕНЬГИ", "АРМИЯ", "АРМИЯ", "АРМИЯ", "АРМИЯ",
    "АРМИЯ", "КУЛЬТУРА", "КУЛЬТУРА", "КУЛЬТУРА", "КУЛЬТУРА", "РЕЛИГИЯ", "РЕЛИГИЯ", "РЕЛИГИЯ")

dictators = ('Бладимир Лепин', 'Гирозито', 'Апольт Килдер', 'Иозев Здалин', 'Анвар-баша', 'Гин Ыр Дзен',
             'Ко Си Лин', 'Бол Болт', 'Заддом Сухейн', 'Ахиа Кан', 'Кидаки Додзёо', 'Чан Майчи',
             'Мяу Дзэтун', 'Гладимир Будим')  # Кортеж соперников
again, nations, counter, end = 'д', 20, 0, 1
name = input('\n\n\n\t\t\tВаше имя: ')
print(f'Приветствую Вас {name}, добро пожаловать в пошаговую игру "Государства"!.')


# описания разделов  (в разработке)
# science = {'Транспорт', 'Антибиотики', 'Интернет', 'Канализация', 'Бумага', 'Атом', 'Электрификация', 'Электроника'}
# money = {'Золото', 'Платина', 'Валюта', 'Алмазы'}
# army = {'Спецназ', 'ВДВ', 'ВМФ'}
# culture = {'Кинематограф', 'Театр', 'Художество', 'Скульптура'}
# faith = {'Христианство', 'Буддизм', 'Индуизм', 'Растафарианство'}
#
# # Наименования государств игры - дабавить!
# kingdoms = {'Кайсай', 'Раззея', 'Аневика', 'Крамция', 'Мангрия', 'Кертания', 'Говея', 'Зоньша', 'Идания', 'Естьлания',
# 'Кмурция', 'Какмада'}


def rules():
    print(f'''      Правила игры: 
    У Вас от 1 до 4 Соперников на выбор.
    От Вас требуется первым захватить не менее 6 государств из 20 (Всего: 20 нейтральных).
    Один ход это одно действие. Действие: Обменять ресурсы, применить Событие или АКТИВ.
        Ресурсы, Действия и АКТИВЫ выдаются произвольно вместе их 6 штук.
        РЕСУРСЫ это: уголь, нефть, газ, дерево, вода, металлы.
    Вы можете обменивать больше одного ресурса ТОЛЬКО если они одинаковые. Иначе только один.
        События это: Деньги, Армия, Культура. 
    Их нельзя обменивать. Только применять на соперников.
    ДЕНЬГИ выкупают 1 государство у соперника, когда у него нет РЕЛИГИИ или АРМИИ.
    АРМИЯ может отобрать государство у другого игрока если у него нет двух АРМИЙ.
    КУЛЬТУРА производит  революцию в государстве  другого игрока если у того нет РЕЛИГИИ, та-
 ким образом государство снова становится нейтральным.
        АКТИВЫ это: НАУКА, РЕЛИГИЯ, ЛОТЕРЕЯ
    НАУКА покупает 1 государство за один ход. НАУКА работает если у Вас нет РЕЛИГИИ.
    РЕЛИГИЯ может защитить вас от КУЛЬТУРЫ и ДЕНЕГ, но не дает применить НАУКУ. РЕЛИГИЮ можно 
 продать только обменяв полностью всю религию и всю науку при условии, что науки больше.
    ЛОТЕРЕЯ может  случайным  образом подарить Вам или Вашему сопернику государство или приме-
 нить случайное Событие.
    
        Правильные варианты ввода(примеры):
    Если ресурс:  "нефть"
    Если Действие(номер врага и Действие):  "3 культура"
    Если АКТИВ:  "лотерея"
        
        ЕСЛИ ВЫ ВНИМАТЕЛЬНО ИЗУЧИЛИ ПРАВИЛА ДАВАЙТЕ ИГРАТЬ.
''')


rules()


def lastes(cnt):  # окончания слов
    if cnt == 1:
        return 'государство'
    elif cnt in range(2, 5):
        return 'государства'
    else:
        return 'государств'


def protect(npt, user_index):  # защитa от введенного бреда
    if npt == '':
        print('Надо хотябы что-то ввести!')
        return [False, None, None]
    if npt.isalnum():
        if npt.upper() == 'РЕЛИГИЯ':
            if userlist[user_index].count('НАУКА') > userlist[user_index].count('РЕЛИГИЯ'):
                answer = input('Напечатайте "да" если хотите продать всю религию и всю науку: ')
                if answer.lower() == 'да':
                    return [True, 'ПРОДАТЬ', npt.upper()]
            else:
                print(f'Религию нельзя продавать если у Вас нет науки больше чем религии.')
                return [False, None, None]
        elif npt.upper() == 'НАУКА':
            if 'РЕЛИГИЯ' in userlist[user_index]:
                print(f'НАУКУ нельзя применять пока у Вас есть РЕЛИГИЯ')
                return [False, None, None]
            else:
                print(f'Применено: {npt}')
                return [True, name, npt.upper()]
        elif npt.upper() == 'ЛОТЕРЕЯ':
            print(f'Применено: {npt.upper()}')
            return [True, name, npt.upper()]
        elif npt.lower() in res:
            print(f'Продано: {npt.lower()}')
            return [True, 'ПРОДАТЬ', npt.lower()]
        else:
            print(f'Ничего не произошло! {name}, надо вводить ресурс или актив(НАУКА,ЛОТЕРЕЯ) '
                  f'или номер соперника и АКТИВ!')
            return [False, None, None]
    order, prod = npt.upper().split()
    if order.isalpha() and prod.isdigit():
        order, prod = prod, order
    if int(order) in range(1, len(rivals)):
        if prod == 'НАУКА':
            print(f'НАУКУ нельзя применять на врага!')
            return [False, None, None]
        elif prod == 'РЕЛИГИЯ':
            print(f'Религию нельзя применять на врага!')
            return [False, None, None]
        elif prod in res:
            print(f'Применено: {prod}')
            return [True, rivals[int(order)], prod]
    elif order == 'продать' and prod in res:
        print(f'Продано: {prod}')
        return [True, order.upper(), prod.lower()]
    else:
        print(f'Ничего не произошло! {name}, надо вводить ресурс или актив(НАУКА, ЛОТЕРЕЯ) '
              f'или номер соперника и АКТИВ!')
        return [False, None, None]


def infrm(info):
    if info == 'res':
        ress = [i for i in userlist[0] if i in ("уголь", "нефть", "газ", "вода", "дерево", "металлы")]
        sorted(ress)
        return " ".join(map(str, ress))
    elif info == 'activ':
        ress = [i for i in userlist[0] if i in ('НАУКА', 'РЕЛИГИЯ', 'ЛОТЕРЕЯ')]
        return " ".join(map(str, ress))
    elif info == 'spactiv':
        ress = [i for i in userlist[0] if i in ('ДЕНЬГИ', 'АРМИЯ', 'КУЛЬТУРА')]
        return " ".join(map(str, ress))
    else:
        return ''


def stages(userlst, status):  # этап отображения статуса для игрока
    print(f'''----ooO----------Статистика----(пример ввода: "газ" или "наука" или "2 деньги")
|     Ресурсы:
| {infrm('res')}
|     Действия:
| {infrm('activ')}
|     АКТИВЫ:
| {infrm('spactiv')}
|   
|   Соперники: ''')
    print(f'| -> {name} {status[0]} {lastes(status[0])}')
    for i in range(1, len(rivals)):
        print(f"| {i}: {rivals[i]} {status[i]} {lastes(status[i])}")
    print(f'''|
| Свободно для покупки: {nations} {lastes(nations)}
'---------------------------------------ooO------''')


def sci(rivals_index):  # как поступает наука
    global nations
    if 'РЕЛИГИЯ' in userlist[rivals_index]:
        print(f'НАУКУ нельзя применить пока у Вас есть РЕЛИГИЯ')
    elif nations >= 2:
        a = randint(1, nations * 2)
        if a == 4 or a == 12:
            nations -= 2
            userstate[rivals_index] += 2
            userlist[rivals_index][userlist[rivals_index].index('НАУКА')] = choice(res)
            print(f'\t\tполучено 2(два) государства.')
        else:
            nations -= 1
            userstate[rivals_index] += 1
            userlist[rivals_index][userlist[rivals_index].index('НАУКА')] = choice(res)
            print(f'\t\tполучено государство.')


def mon(rival_name, activ, user_index):  # расчет как поступает деньги
    rival_index = rivals.index(rival_name)
    if 'РЕЛИГИЯ' in userlist[rival_index]:
        userlist[user_index][userlist[user_index].index('ДЕНЬГИ')] = choice(res)
        userlist[rival_index][userlist[rival_index].index('РЕЛИГИЯ')] = choice(res)
        print('\t\tпротив игрока ' + rival_name + ' - защита РЕЛИГИЕЙ. НЕУДАЧА.')
    elif 'АРМИЯ' in userlist[rival_index]:
        userlist[user_index][userlist[user_index].index('ДЕНЬГИ')] = choice(res)
        userlist[rival_index][userlist[rival_index].index('АРМИЯ')] = choice(res)
        print('\t\tпротив игрока ' + rival_name + ' - защита АРМИЕЙ. НЕУДАЧА.')
    else:
        userlist[user_index][userlist[user_index].index('ДЕНЬГИ')] = choice(res)
        userstate[rival_index] -= 1
        userstate[user_index] += 1
        print('\t\tпротив игрока ' + rival_name + ' получено государство.')


def arm(rival_name, activ, user_index):  # расчет как поступает армия
    rival_index = rivals.index(rival_name)
    if userlist[rival_index].count('АРМИЯ') >= 2:
        userlist[user_index][userlist[user_index].index('АРМИЯ')] = choice(res)
        userlist[user_index][userlist[user_index].index('АРМИЯ')] = choice(res)
        userlist[rival_index][userlist[rival_index].index('АРМИЯ')] = choice(res)
        print('\t\tпротив игрока ' + rival_name + ' - защита АРМИЕЙ. НЕУДАЧА.')
    else:
        userlist[user_index][userlist[user_index].index('АРМИЯ')] = choice(res)
        userstate[rival_index] -= 1
        userstate[user_index] += 1
        print('\t\tпротив игрока ' + rival_name + ' получено государство.')


def cult(rival_name, activ, user_index):  # расчет как поступает культура
    rival_index = rivals.index(rival_name)
    global nations
    if 'РЕЛИГИЯ' in userlist[rival_index]:
        userlist[user_index][userlist[user_index].index('КУЛЬТУРА')] = choice(res)
        userlist[rival_index][userlist[rival_index].index('РЕЛИГИЯ')] = choice(res)
        print('\t\tпротив игрока ' + rival_name + ' - защита РЕЛИГИЕЙ. НЕУДАЧА.')
    else:
        userlist[user_index][userlist[user_index].index('КУЛЬТУРА')] = choice(res)
        userstate[rival_index] -= 1
        nations += 1
        print('\t\tпротив игрока ' + rival_name + ' произошла революция.')


def lott(rivals_index):
    global nations
    resource = choice(res)
    lucky = choice(rivals)
    if resource in ("ДЕНЬГИ", "АРМИЯ", "КУЛЬТУРА"):
        order, cnt = 0, 0
        if sum(userstate) - userstate[rivals_index] > 0:
            temp = userlist[rivals.index(lucky)].copy()
            userlist[rivals.index(lucky)].append(resource)
            for j in range(0, len(rivals)):
                if userstate[j] > cnt and j != rivals_index:
                    cnt = j
            userlist[rivals_index][userlist[rivals_index].index('ЛОТЕРЕЯ')] = choice(res)
            turn(rivals[cnt], resource, rivals.index(lucky))
            userlist[rivals.index(lucky)].clear()
            userlist[rivals.index(lucky)].append(temp)
            print(f'\t\tв ходе лотереи получено и применено {resource}')
        else:
            userlist[rivals_index][userlist[rivals_index].index('ЛОТЕРЕЯ')] = resource
            if nations > 0:
                nations -= 1
                userstate[rivals.index(lucky)] += 1
                print('\t\t ' + lucky + ' в ходе лотереи получено государство.')
            else:
                print('\t\tЛОТЕРЕЯ не УДАЛАСЬ!')
    else:
        userlist[rivals_index][userlist[rivals_index].index('ЛОТЕРЕЯ')] = resource
        if nations > 0:
            nations -= 1
            userstate[rivals.index(lucky)] += 1
            print('\t\t ' + lucky + ' в ходе лотереи получено государство.')
        else:
            print('\t\tЛОТЕРЕЯ НЕ УДАЛАСЬ!')


def change(resource, rivals_index):  # обмен ресурсов из списка res
    if resource == 'РЕЛИГИЯ':
        for i, item in enumerate(userlist[rivals_index]):
            if item == resource or item == 'НАУКА':
                userlist[rivals_index][i] = choice(res)
    else:
        for i, item in enumerate(userlist[rivals_index]):
            if item == resource:
                userlist[rivals_index][i] = choice(res)


def turn(order, resource, rivals_index):  # ход
    if order == 'ПРОДАТЬ':
        change(resource, rivals_index)
    elif order in rivals:
        if resource == 'НАУКА':
            sci(rivals_index)
        elif resource == 'ЛОТЕРЕЯ':
            lott(rivals_index)
        elif resource == 'ДЕНЬГИ':
            mon(order, resource, rivals_index)
        elif resource == 'АРМИЯ':
            arm(order, resource, rivals_index)
        elif resource == 'КУЛЬТУРА':
            cult(order, resource, rivals_index)


def bot_tries(rivals_index):
    list_res = userlist[rivals_index]
    tmp_rvl = sum([userstate[i] for i in range(len(userstate)) if i != rivals_index])
    lower_res = [i for i in list_res if i.islower()]
    if 'НАУКА' in list_res and nations > 0 and 'РЕЛИГИЯ' not in list_res:
        print(rivals[rivals_index] + ' применено: НАУКА')
        return [rivals[rivals_index], 'НАУКА']
    elif 'ЛОТЕРЕЯ' in list_res and nations > 0:
        print(rivals[rivals_index] + ' применено: ЛОТЕРЕЯ')
        return [rivals[rivals_index], 'ЛОТЕРЕЯ']
    elif 'ДЕНЬГИ' in list_res and tmp_rvl > 0:
        temp, rvl = 0, ''
        for i in range(len(rivals)):
            if i != rivals_index and userstate[i] > 0:
                if temp < userstate[i]:
                    temp, rvl = userstate[i], rivals[i]
        print(rivals[rivals_index] + ' применено: ДЕНЬГИ')
        return [rvl, 'ДЕНЬГИ']
    elif 'АРМИЯ' in list_res and tmp_rvl > 0:
        temp, rvl = 0, ''
        for i in range(len(rivals)):
            if i != rivals_index and userstate[i] > 0:
                if temp <= userstate[i]:
                    temp, rvl = userstate[i], rivals[i]
        print(rivals[rivals_index] + ' применено: АРМИЯ')
        return [rvl, 'АРМИЯ']
    elif 'КУЛЬТУРА' in list_res and tmp_rvl > 0:
        temp, rvl = 0, ''
        for i in range(len(rivals)):
            if i != rivals_index and userstate[i] > 0:
                if temp <= userstate[i]:
                    temp, rvl = userstate[i], rivals[i]
        print(rivals[rivals_index] + ' применено: КУЛЬТУРА')
        return [rvl, 'КУЛЬТУРА']
    elif len(lower_res) > 0:
        cnt, val = 0, ''
        for i in lower_res:
            if lower_res.count(i) > cnt:
                cnt, val = lower_res.count(i), i
        print(rivals[rivals_index] + ' продано: ресурсы')
        return ['ПРОДАТЬ', val]
    else:
        print(rivals[rivals_index] + ' пропускает ход')
        return ['ПРОДАТЬ', 'РЕЛИГИЯ']


def rival_difficulty():  # Выбор соперников и сложности и создание глобальных списков
    r = input('--- Количество соперников от 1 до 4(больше = сложнее): ')

    if r.isdigit():
        if int(r) in range(1, 5):
            riv = [name] + sample(dictators, int(r))
            state = [0 for _ in range(int(r) + 1)]

            srlst = [sample(res, 6)] + [sample(res, 5) for _ in range(int(r))]

            if name.lower() == 'god':
                srlst[0] = sample(res, 20)
                print('GOD, теперь у вас 24 актива и ресурса', sep='\n\t\t\t')
            return [1, srlst, state, riv]
        else:
            print("От 1 до 4!!!")
            return [0, None, None, None]
    else:
        print("Цифры!!!")
        return [0, None, None, None]


def play():  # основная функция игры, цикл ходов
    global counter, end
    while end == 1:
        print('\n--- ', str(counter + 1) + '-й этап')
        stages(userlist, userstate)
        print('--- для правил напечатайте слово "правила".')  # отображение окна статистики
        npt = input('\t--- Ход игрока. Ввод: ')
        if npt.lower() == 'правила':
            rules()
            continue
        flag_check, order, resource = protect(npt, 0)
        if not flag_check:  # защита от ввода бреда
            continue
        turn(order, resource, 0)  # ход игрока
        if userstate[0] >= 6:
            print(f"Поздравляю! {rivals[i]} вы победили в этой игре!\n\n" * 10)
            end = 0
            break
        print('--- Соперники ходят:')
        for i in range(1, len(rivals)):  # ход ботов
            order, resource = bot_tries(i)

            turn(order, resource, i)
            for val in userstate:
                if val >= 6:
                    print(f"ПОРАЖЕНИЕ! Победил {rivals[i]}!\n\n" * 10)
                    end = 0
                    break
        counter += 1


while True:  # цикл запуска игры, правил, запуска выбора соперников и уровня сложности!
    if again.lower() in 'д да ок хорошо конечно ага давай yes sure ok common yea yeah yep real go':
        nations, counter, end = 20, 0, 1
        flag, userlist, userstate, rivals = rival_difficulty()
        if flag:
            play()
        else:
            continue
        again = input('Играем еще раз?:')
    elif again.lower() in 'нет н неа но не "не хочу" все хватит no not nah nope n отстань прекратить закончить stop end':
        print('До скорого, до встречи и, "пока-пока" или до скорых встреч.')
        break
    else:
        continue


