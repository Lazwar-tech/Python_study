digit = int(input("Ввести целое число: "))
if digit <= 0:
    print("Число не должно быть нулевым.")
else:
    digit_str = str(digit)
    result = 1
    for i in digit_str:
        result = result * int(i)
    while result > 9:
        digit_str = str(result)
        result = 1
        for i in digit_str:
            result = result * int(i)
    print(result)

