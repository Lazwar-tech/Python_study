while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    sign = input("Введите оператор (+,-,*,/): ")
    if sign == "+":
        print(a + b)
    elif sign == "-":
        print(a - b)
    elif sign == "*":
        print(a * b)
    elif sign == "/":
        if not b:
            print("На ноль не делится")
        if b > 0:
            print(a / b)
    else:
        print("Неверный оператор")
    finish = input("Хотите продолжить работу\nкалькулятора? (y/n): ")
    if finish.lower() != "y":
        print("Завершение работы")
        break
