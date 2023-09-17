# print ('введите три числа')
# a = float(input('1:  '))
# b = float(input('2:  '))
# c = float(input('3:  '))
# x = (a + b + c)/3

userlist = input('введите числа через пробел: ').split()
print('вы ввели:', userlist)
user_list_numbers = list(map(float, userlist))
x = sum(user_list_numbers)/len(user_list_numbers)
print ('среднее значение:', round (x, 3))

