userstring = input('введите 12345 прописью:   ')
print('вы ввели:', userstring)
# заменить пробелы тире 1
devidedstr = userstring.split(' ')
print('это первый способ:','-'.join(devidedstr))

# заменить пробелы тире 2
newuserstring=userstring.replace(' ','-')
print ('это второй способ:', newuserstring)







