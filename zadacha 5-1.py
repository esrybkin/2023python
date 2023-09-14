# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла.Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def parce_str(string_parce: str) -> tuple:
    len_ext = 4
    file_extension = string_parce.rsplit('.',  maxsplit=1)
    path_file_name = string_parce.rsplit('\\', maxsplit=1)
    
    tuple_res = (path_file_name[0], path_file_name[1][:-len_ext], file_extension[1])
    return tuple_res

path_str = 'H:\Recent\Star Trek Strange New Worlds 2 - [1080p]\Star.Trek.Strange.New.Worlds.S02E03.1080p.rus.mkv'
print(parce_str(path_str))