# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе число

while not input("start? (y/n)") == 'n':
    try:
        num1 = float(input("число 1:"))
    except ValueError:
        print('введено не число')
        continue
    act = input("+-/* **")
    try:
        num2 = float(input("число2:"))
    except ValueError:
        print('введено не число')
        continue
    if act == "+":
        res = num1 + num2
    elif act == "-":
        res = num1 - num2
    elif act == "*":
        res = num1 * num2
    elif act == "/":
        try:
            res = num1 / num2
        except ZeroDivisionError:
            print('деление на ноль')
            continue
    elif act == "**":
        res = num1 ** num2
    else:
        print('введено неверное действие')
        continue
    print(num1, act, num2, "=", round (res, 4))

