lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3]
# lst = [1, 2, 3, 4, 5]
# lst = [1]
# lst = []

i = len(lst) - len(lst) // 2
j = [lst[:i], lst[i:]]
print(j)
