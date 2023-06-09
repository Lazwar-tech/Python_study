seconds = int(input("Введите количество секунд: "))
if seconds < 0 or seconds >= 8640000:
    print("Ошибка: введенное число должно быть больше или равно 0 и меньше 8640000")
else:
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    if days % 10 == 1 and days % 100:
        days_str = "день"
    elif days % 10 in [2, 3, 4] and days % 100 not in [11, 12, 13, 14]:
        days_str = "дня"
    else:
        days_str = "дней"
    print(f"{days} {days_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")