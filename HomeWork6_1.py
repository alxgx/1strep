# TODO
# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int

def foo_bin_dec(x):
    """
    :param x: int
    :return: bin and decimal
    """
    x_bin = bin(x)
    # убираем 0b и приводим к строке:
    x_dec_str = str(x_bin)[2:]
    x_dec = 0
    # n - это степень двоек для каждого символа строки при переводе в десятичную систему
    # перебираем строку слева, поэтому степень = длина строки -1:
    n = len(x_dec_str) - 1
    for i in range (len(x_dec_str)):
        x_dec += int(x_dec_str[i]) * (2 ** (n))
        n = n - 1

    print('binary: ', x_bin)
    print('decimal: ', x_dec)

foo_bin_dec(666)