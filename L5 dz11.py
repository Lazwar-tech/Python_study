while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    sign = input("Введите оператор (+,-,*,/): ")
    if sign == "+":
        c = a + b
        print(c)
    elif sign == "-":
        c = a - b
        print(c)
    elif sign == "*":
        c = a * b
        print(c)
    elif sign == "/":
        if not b:
            print("На ноль не делится.")
        if b != 0:
            c = a / b
            print(c)
    else:
        print("Неверный оператор")
    finish = input("Продолжить работу? (y/n): ")
    if finish.lower() != "y":
        print("Завершение работы")
        break
