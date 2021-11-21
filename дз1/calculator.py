# simple calculator

num1 = float(input('Введите первое число: '))
sign = input('Укажите знак операции (+ - * /): ').strip()
num2 = float(input('Введите второе число: '))

if sign == '+':
    print('Результат: ', num1+num2)
elif sign == '-':
    print('Результат: ', num1-num2)
elif sign == '*':
    print('Результат: ', num1*num2)
elif sign == '/':
    print('Результат: ', num1/num2)
else:
    print('Неверный знак операции. Выполнение невозможно.')
