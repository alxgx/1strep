# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами
name = input('name:')
age = input('age:')
city = input('city:')

# 0
print('0: привет,', name, 'из города', city, ', тебе уже', age, ', поздравляем!')

# 1
result = '1: привет, %s из города %s, тебе уже %s, поздравляем!' % (name, city, age)
print(result)

# 2
# userlist = input('введите ваше имя, возраст и город').split()
result1 = '2: привет, {} из города {}, тебе уже {}, поздравляем!'.format(name, city, age)
print(result1)

# 3
result3 = f'3: привет, {name} из города {city}, тебе уже {age}, поздравляем!'
print(result3)

