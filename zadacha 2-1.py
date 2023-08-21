# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def convert(number: int, base: int) -> str:
    all_numbers = '0123456789abcdef'
    res = ''
    while number > 0:
        res = all_numbers[number % base] + res
        number = number // base
    return res

a: int = int(input('Введите значение '))
b: int = int(input('Введите систему исчисления '))
print(convert(a, b))

print(hex(a))
