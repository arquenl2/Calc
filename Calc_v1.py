import math
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.BLACK)
print(Back.CYAN)

run = True
while run:
    what = input("\nВыберите действие: +, -, *, /, **, % ")
    a = float(input("Введите первое число: "))
    b = float(input('Введите второе число: '))
    if what == '+':
        c = a + b
        print('Результат: ' + str(c))
    elif what == '-':
        c = a - b
        print('Результат: ' + str(c))
    elif what == '*':
        c = a * b
        print('Результат: ' + str(c))
    elif what == '/':
        c = a / b
        print('Результат: ' + str(c))
    elif what == '**':
        c = a ** b
        print('Результат: ' + str(c))
    else:
        run = False
        print('Выбрана неверная операция ')
input()