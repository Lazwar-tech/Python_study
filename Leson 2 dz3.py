n = int(input('Ввести пятизначное число: '))
x = 0
x = x + 10000 * (n % 10)
x = x + 1000 * (n // 10 % 10)
x = x + 100 * (n // 100 % 10)
x = x + 10 * (n // 1000 % 10)
x = x + 1 * (n // 10000 % 10)
print(x)
