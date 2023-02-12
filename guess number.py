import random
import math

def is_valid(n):
    return True if n.isdigit() and int(n) in range(1, 101) else print('\nЧИСЛО должно быть от 1 до 100\n')

def is_right(n):
    pass
    if n > a:
        return 'Мое число меньше!'
    elif n < a:
        return 'Мое число больше!'
    else:
        return 'Угадал, но это ничего не значит!'

def is_last_symbol(cnt):
    if cnt == 1:
        return 'ка'
    elif cnt in range(1, 5):
        return 'ки'
    else:
        return 'ок'

def balance(name, bln, bln1):
    print(f'''  Баланс:       
        {name} {bln1} коинов.
        Угадайка {bln} коинов.
        Ставка 25 коинов. Число от 1 до 100.
        ''')

def if_balance(bln):
    if bln == 0 or bln == 200:
        global flag
        flag = True
    return bln == 0 or bln == 200

bln, bln1, flag, name = 100, 100, False, input('Введи свое имя: ')

print(f''' Добро пожаловать в Угадай число, {name}!
    Правила игры: 
        Играем пока у одного из нас не станет 0 коинов. 
        У каждого в начале по 100 коинов.
        Ставка 25 коинов. 
        Всего 8 попыток!

        Я гарантирую, что загадываю корректные числа.
        Надеюсь ты будешь делать также.
        ''')

while flag == False:
    a = random.randint(1, 100)
    if if_balance(bln):
        print('')
        break
    else:
        balance(name, bln, bln1)

    cnt = 7
    while cnt > 0:
        if if_balance(bln):
            break
        print(f'{name}. У тебя {cnt} попыт{is_last_symbol(cnt)}. Введи свою догадку-число: ')
        n = input()
        if is_valid(n):
            n = int(n)
            cnt -= 1
        else:
            cnt -= 1
            continue
        print(is_right(n))
        if is_right(n) == 'Угадал, но это ничего не значит!':
            bln -= 25
            bln1 += 25
            break
        elif cnt == 0:
            print(f'Аххаха {name}, ты исчерпал все попытки!')
            bln += 25
            bln1 -= 25
            break

    if if_balance(bln):
        print('')
    else:
        balance(name, bln, bln1)
        print('Теперь угадывать буду я.')

    cnt, left, right = 0, 1, 100
    while True:
        if if_balance(bln):
            break
        mdl = (left + right) // 2
        if cnt == math.ceil(math.log2(int(100))):
            print(f"{name}, ты обманул меня и поменял число!!!! поздравля...нет. очки твои")
            break
        print(f'Итак. У меня {7-cnt} попыт{is_last_symbol(7-cnt)}')
        print(f'Твоё число {mdl}, верно?')
        print('\n"=", если равно!\n">", если больше \n"<", если меньше:\n')
        sing = input('Введи ">", если больше или "<", если меньше:\n')
        if sing != "=" and sing != ">" and sing != "<":
            cnt -= 1
            print(f'Что это было? Стало {7-cnt} попыт{is_last_symbol(7-cnt)}')
        elif sing == '<':
            right = mdl - 1
            cnt += 1
        elif sing == '>':
            left = mdl + 1
            cnt += 1
        elif sing == '=':
            cnt += 1
            print(f'Здорово! Я угадал за {cnt} попыт{is_last_symbol(cnt)}\n')
            bln += 25
            bln1 -= 25
            break

    if bln == 200:
        print("Хаха! я победил тебя! Пока неудачник!")
    elif bln == 0:
        print(f'Ты меня уделал. Поззззддравляю везззунчик! Прощай {name}.')
