# import string
# #
# start, end = input("Ввести диапазон букв : ").split('-')
# letter_range = string.ascii_letters
# if start > end:
#     letter_range = letter_range[::-1]
# al_bt = letter_range[letter_range.index(start):letter_range.index(end)+1]
# print(al_bt)

import string

letter_range = string.ascii_letters
start, end = input("Ввести диапазон букв : ").split('-')
if end.islower():
    letter_range = string.ascii_letters[string.ascii_lowercase.index
                                        (start.lower()):string.ascii_lowercase.index(end.lower()) + 1]
else:
    letter_range = string.ascii_letters[string.ascii_lowercase.index
                                        (start.lower()):
                                        len(string.ascii_lowercase) + string.ascii_uppercase.index(end.upper()) + 1]
print(letter_range)