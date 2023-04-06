a = float(input("Ввести первое число: "))
b = float(input("Ввести второе число: "))

sign = input("Ввести тип операции('+,-,*,/) : ")
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
        print("На ноль не делится")
    else:
        c = a / b
        if b:
            print(c)
