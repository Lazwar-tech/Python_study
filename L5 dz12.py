import string

s = input('Введите строку: ')

s = s.translate(str.maketrans('', '', string.punctuation))
s = s.title()
s = s[:140]
s = '#' + ''.join(s.split())
print(s)