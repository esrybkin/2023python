# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibon(number):
    num1 = 0
    num2 = 1
    for i in range(number):
        yield num2
        num1, num2 = num2, num1 + num2

print(*fibon(15))

