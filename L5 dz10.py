import keyword

name = input("Введите имя переменной: ")

if name in keyword.kwlist:
    print(False)
elif name[0].isdigit() or name[0].isupper() and name[0] != '_':
    print(False)
else:
    for st in name:
        if not st.isalnum() and st != '_':
            print(False)
            break
        elif st.isupper():
            print(False)
            break
    else:
        print(True)


