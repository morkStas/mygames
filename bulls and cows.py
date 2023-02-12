from tkinter import *
from tkinter.dialog import *
import random

x = ''                  # x для случайного числа (для тестирования)
cnt = 0                                           # Счётчик ходов

def lst_smbl(b):                                # функция меняющая окончания быков
    if b == 0:
        return ' быков'
    elif b == 1:
        return '-го быка'
    else:
        return ' быка'
def lst_smbl1(c):                                # функция меняющая окончания коров
    if c == 1:
        return ' корову'
    elif c == 0:
        return ' коров'
    else:
        return ' коровы'
def check_cycl(x,y):                            # цикл сверки чисел x и y
    b, c = 0, 0
    for i in range(4):
        if x[i] == y[i]:
            b += 1                          # добавляем быка
        elif y[i] in x:
            c += 1                       # добавляем корову
    return b, c

def play(event):                                # основная функция игры
    global x, cnt
    if len(x) == 0:
        numbers = '0123456789'
        x = ''.join(random.sample(numbers, 4))  # x случайное число
        msg2.config(text='')
    y = ent.get()                               # y введенное игроком
    b, c = check_cycl(x, y)                     # возвращаем количество быков и коров
    cnt += 1                                      # счётчик ходов

# на этом игра завершена, дальше оформление и графика.

    msg2.config(text = msg2.cget('text') + str(cnt) + '-я догадка ' + y + ' содержит: \n' + str(b) + f'{lst_smbl(b)} и ' + str(c) + f'{lst_smbl1(c)}\n')
    ent.delete(0, END)                          # очищаем окно ввода ent
    if b == 4:                                  # победа
        gameOwer = Dialog(title = 'Вы победили за ' + str(cnt) + ' ходов; ',
               text = '     Будешь играть ещё?           ',
               bitmap = 'questhead',
               default = 0,
               strings = ('Да', 'Нет'))
        if gameOwer.num == 1: exit()            # Закончить игру
        cnt = 0                                   # Очистить счётчик ходов
        x = ''                                  # Очистить строку x для случайного числа
        msg2.config(text='Бык : цифра на своём месте.\n'
               'Корова:\nцифра не на своём месте.')     # Выводим правила игры в окно сообщений

tk = Tk()                                       # Создаём окно пиложения
w = tk.winfo_screenwidth()
h = tk.winfo_screenheight()
w = w//2 # середина экрана
h = h//2
w = w - 250 # смещение от середины
h = h - 300

tk.geometry('500x600+{}+{}'.format(w, h))                          # Задаём размер окна пиложения в пикселях
tk.title('Быки и Коровы Полстянов')                       # Название программы в заголовке окна

msg = Message(width=400, padx=10, pady=5,
              text='Я загадал 4 цифры. Попробуй угадать их!\nГарантирую - цифры не повторяются\n\nВведи и нажми "Enter":')               # Создаём окно сообщений
msg.pack(padx=10, pady=5)                       # Размещаем окно сообщений в окне tk
msg.config(font=('Arial', 12, 'bold'), justify='center')        # Параметры для msg

ent = Entry(width=12, justify='center', font=('Arial', 12))                           # Создаём поле ввода
ent.pack(pady=20)                                      # Размещаем поле ввода в окне tk
ent.focus()                                     # Поместить фокус в поле ввода
ent.bind('<Return>', play)                     # Опеределяем функцию плэй по энтеру


msg2 = Message(width=250, padx=10, pady=5,
              text='Бык : цифра на своём месте.\n'
               'Корова:\nцифра не на своём месте.')     # Создаём окно сообщений
msg2.pack(side='left', padx=10, pady=5)                      # Размещаем окно сообщений в окне tk
msg2.config(font=('times', 12, 'normal'))       # Параметры для msg

msg3 = Message(width=150, text='Блокнот для тебя:')     # Создаём окно блокнот
msg3.pack(side='top')
msg3.config(font=('times', 12, 'normal'))
ent2 = Text(height=250)                           # Создаём поле для блокнота
ent2.pack(side='right', padx=20, pady=20)


mainloop()                                      # Цикл ожидания событий