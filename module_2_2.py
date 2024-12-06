first = int(input('Ввод в консоль 1: '))
second = int(input('Ввод в консоль 2: '))
third = int(input('Ввод в консоль 3: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second != third:
    print(0)
    
