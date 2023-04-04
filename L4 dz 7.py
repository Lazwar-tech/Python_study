# lst = [0, 1, 0, 3, 12]
# lst = [0]
lst = [1, 0, 3, 0, 0, 0, 5]
# lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# lst = [1, 0, 3, 0, 0, 0, 5]

lst2 = []
for i in lst:
    if i != 0:
        lst2.append(i)
for i in range(lst.count(0)):
    lst2.append(0)
print(lst2)