# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.

def f_morse(text):

    morse = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••',
             'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—',
             'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—','y': '—•——',
             'z': '——••', ' ': ' '}

    morse_text = ""
    for letter in text:
        # if letter not in morse_text: morse_text += "#"
        # else:
        morse_text += morse.get(letter)

    print(morse_text)

f_morse('hello world')