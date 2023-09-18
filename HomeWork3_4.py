# print ('введите три числа')
# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных
# a = float(input('1:  '))
# b = float(input('2:  '))
# c = float(input('3:  '))

# я сделал для любого количества чисел, но думаю, что так делать нельзя, это какой-то г**код:) :
# - считается количество минусов в строке:
user_list = input('введите числа через пробел: ').split()
user_list_numbers = list(map(float, user_list))
print('вы ввели:', user_list_numbers)
length = len(user_list_numbers)
print('первый способ:')
# print ('количество чисел:', length)
result_negative_string = str(user_list)
negative_amount = result_negative_string.count('-')
positive_amount = length - negative_amount
print ('количество отрицательных чисел:', negative_amount)
print('количество положительных чисел:', positive_amount)


# проверки для трех чисел через сравнение c 0:
a = user_list_numbers.pop(0) < 0
b = user_list_numbers.pop(0) < 0
c = user_list_numbers.pop(0) < 0
result_list = [a,b,c]
print ('второй способ:')
result_string2 = str(result_list)
print (result_string2)
negative_amount2 = result_string2.count('True')
positive_amount2 = result_string2.count('False')
print ('количество отрицательных чисел вторым способом:', negative_amount2)
print ('количество положительных чисел вторым способом:', positive_amount2)






