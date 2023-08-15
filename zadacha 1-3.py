# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать "больше" или "меньше" после каждой попытки.

from random import randint

i = 0
LIFE = 10
LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print('Угадаешь какое число загадано?')

while i < LIFE:
    num_user = int(input('Введи число '))
    if num == num_user:
        print('Верно!')       
        break
    elif num > num_user:
        print('Больше')
    else:
        print('Меньше')
    i += 1 
    print('Осталось попыток =', LIFE - i)
print('Загаданное число ', num)
