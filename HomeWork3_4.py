# print ('введите три числа')
# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных
# a = float(input('1:  '))
# b = float(input('2:  '))
# c = float(input('3:  '))

# я сделал для любого количества чисел, но думаю, что так делать нельзя, это какой-то г**код:) :

user_list = input('введите числа через пробел: ').split()
user_list_numbers = list(map(float, user_list))
print('вы ввели:', user_list_numbers)
length = len(user_list_numbers)
print ('количество чисел:', length)
result_negative_string = str(user_list)
negative_amount = result_negative_string.count('-')
positive_amount = length - negative_amount
print ('количество отрицательных чисел:', negative_amount)
print('количество положительных чисел:', positive_amount)


# проверки для трех чисел через сравнение, но не смог результат привести к числу без if
# a = user_list_numbers.pop(0) < 0
# b = user_list_numbers.pop(0) < 0
# c = user_list_numbers.pop(0) < 0
# result_list = [a,b,c]
# result_string = str(result_list)
# print(result_string)
# positive_amount = result_string.replace('false','1')
# print(positive_amount)





