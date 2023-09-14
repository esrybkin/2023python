# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

def gen_dict(my_name: str, my_salary: int, my_bonus: str) -> dict:
    new_dic = {round(salary * (1+ bonus/100), 2) for name, salary, bonus in zip(my_name, my_salary, my_bonus)}
    return new_dic

def clear_str(m_list):
    for i in range(len(m_list)):
        m_list[i]= float(m_list[i].replace('%',""))
    return None

names = ['Сергей', 'Дмитрий', 'Стас']
salary = [100000, 20000, 30000]
bonus = ['10.25%', '25.30%', '40.45%']

clear_str(bonus)
print('\n', gen_dict(names, salary, bonus))