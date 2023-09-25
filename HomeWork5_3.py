# Вывести четные числа от 2 до N по 5 в строку
n = int(input('enter N: '))
numbers = [i for i in range(n) if i % 2 == 0]
print(numbers, '\n')
s = (len(numbers))
# символов в строке k=5=шаг цикла:
k = 5
for i in range(1, s, k):
    print(numbers[i:i+5])