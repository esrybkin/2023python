# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, 
# определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - 
# координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


import random as rnd

__all__ = ['check_queen_8x8', 'gen_positions']

_QUEEN_COUNT: int = 8
_SIZE_BOARD: int = 8


def check_queen_8x8(positions: list[tuple]) -> bool:
    result = True
    if len(positions) != _QUEEN_COUNT:
        result = False
    else:
        for i in range(_QUEEN_COUNT - 1):  
            if not result:
                break
            row_1, col_1 = positions[i]
            for j in range(i + 1, _QUEEN_COUNT):
                row_2, col_2 = positions[j]
                if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                    result = False
                    break
    return result


def gen_positions() -> list[tuple[int, int]]:
    result = []
    for i in range(_SIZE_BOARD):
        result.append((i, rnd.randint(0, _SIZE_BOARD - 1)))
    return result