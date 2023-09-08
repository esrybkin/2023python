# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def function(**kwargs):
    return {v if v.__hash__ is not None else str(v):k for k,v in kwargs.items()}

print(function(a=1, b=[1,2]))

print(function(arg1="Help", arg2=5, arg3="12312"))

