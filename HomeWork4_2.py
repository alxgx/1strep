# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

text = input('enter some text: \n')
result_dict = {i: text.count(i) for i in text}
print(result_dict)
