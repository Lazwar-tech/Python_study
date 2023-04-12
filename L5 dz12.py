import string

s = input('Введите строку: ')

s = s.translate(str.maketrans('', '', string.punctuation))
s = s.title()
s = '#' + ''.join(s.split())
s = s[:140]
print(s)

long = len(s)
print(long)