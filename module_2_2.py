first = (input('Введите целое число: ', ))
second = (input('Введите целое число: ', ))
third = (input('Введите целое число: ', ))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second and second != third and first != third:
    print(0)
