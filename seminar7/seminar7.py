# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.


# import random as rnd

# MIN_NUMBER = -1000
# MAX_NUMBER = 1000

# def fun_gen(num_str: int, file_name: str):
#     with open(file_name, 'a', encoding='utf-8') as f:
#         for _ in range(num_str):
#             int_num = rnd.randint(MIN_NUMBER, MAX_NUMBER)
#             float_num = rnd.uniform(MIN_NUMBER, MAX_NUMBER)
#             f.write(f'{int_num}|{float_num:.2f}\n')

# if __name__ =='__main__':
#     fun_gen(5, 'new_file.txt')


# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.

# import random as rnd

# def func_name(num, new_file):
#     with open('new_file.txt', 'a', encoding='utf-8') as f:
#         for _ in range(num):
#             res = ''
#             for _ in range(rnd.randint(4,7)):
#                 a = chr(rnd.randint(1072, 1104))
#                 res += a
#                 glas = 'аяуюоеёэиы'
#                 res += glas[rnd.randint(0,len(glas) + 1)]
#                 f.write(f'{res.title()}\n')

# func_name(10, 'new_file.txt')


# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла, возвращайтесь в его начало.

# import random as rnd

# def func_name(num, new_file):
#     with open('new_file1.txt', 'a', encoding='utf-8') as f:
#         for _ in range(num):
#             res = ''
#             for _ in range(rnd.randint(4,7)):
#                 a = chr(rnd.randint(1072, 1104))
#                 res += a
#                 glas = 'аяуюоеёэиы'
#                 res += rnd.choice(glas)
#                 f.write(f'{res.title()}\n')

# if __name__ =='__main__':
#     func_name(5, 'new_file1.txt')


def func_sum(file1, file2):
    with (
        open(file1, 'r', encoding='utf-8') as f1,
        open(file2, 'r', encoding='utf-8') as f2,
        open('res.txt','w', encoding='utf-8') as res):
        
        digit = f1.readlines()
        name = f2.readlines()
        max_len = max(len(digit), len(name))
        min_len = min(len(digit), len(name))
        rate = max_len// min_len
        rate2 = max_len % min_len
        if len(digit) > len(name):
            name *= rate
            name += name[:rate2]
        else:
            digit *= rate
            digit += digit[:rate2]
        for i in range(max_len):
            a = eval(digit[i].replace('|', '*'))
            b = name[i].replace('\n', '')
            res.write(f'{b} = {a}\n')

if __name__ == '__main__':
    func_sum('new_file.txt', 'new_file1.txt')