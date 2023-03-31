lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3]
# lst = [1, 2, 3, 4, 5]
# lst = [1]
# lst = []

if len(lst) != 0:
    lst.insert(0, lst.pop())
    print(lst)
else:
    print([])






