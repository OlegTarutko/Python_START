"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""

# Очень заманчиво было найти и посмотреть что это.
# expression = input("Введите математическое выражение не используя пробелы между символами: ")
# print(f'Выражение {expression}={eval(expression)}')


exp = input("Введите математическое выражение: ")

def find(exp, serch_operand):
    ind_start = 0
    ind_finish = 0
    ind_oper = 0
    operands_full = ['*', '/', '-', '+']
    operands = ['*', '/', '-', '+']
    for op in serch_operand:
        operands.remove(op)
    found = False
    for i, sym in enumerate(exp):
        if i == 0 and sym == '-':
            continue
        if not found and sym in operands:
            ind_start = i + 1
        elif found and sym in operands_full:
            ind_finish = i - 1
            return ind_start, ind_finish, ind_oper
        elif sym in serch_operand:
            found = True
            ind_oper = i
            ind_finish = len(exp) - 1
    return ind_start, ind_finish, ind_oper


def calc(exp):
    if '*' in exp or '/' in exp:
        ind_s, ind_f, ind_o = find(exp, ['*', '/'])
        if exp[ind_o] == '*':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o]) * float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f + 1:]
            exp = calc(exp)
        elif exp[ind_o] == '/':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o]) / float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f + 1:]
            exp = calc(exp)

    if '+' in exp or '-' in exp:
        ind_s, ind_f, ind_o = find(exp, ['+', '-'])
        if exp[ind_o] == '+':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o]) + float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f + 1:]
            exp = calc(exp)
        elif exp[ind_o] == '-':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o]) - float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f + 1:]
            exp = calc(exp)
    return exp

print(calc(exp))
