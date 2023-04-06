# lst = [1, 3, 5]
# lst = [6]
lst = []

if lst:
    result = sum(lst[::2]) * lst[-1]
else:
    result = 0
print(result)


