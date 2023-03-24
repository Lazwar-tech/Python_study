print('ol')
age = 35 # в age указатель на область памяти, где лежит 35
[3]
print(id(age))


9794144

[4]
print(id(35))
9794144

[5]
y = 35
print(id(y))
9794144

[6]
z = y
print(id(z))
9794144

[7]
print(id(256))
9801216