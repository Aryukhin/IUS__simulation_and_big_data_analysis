'''
Предоставлен список натуральных чисел. Требуется сформировать из них множество. Если какое-либо число
повторяется, то преобразовать его в строку по образцу: например, если число 4 повторяется 3 раза, то
в множестве будет следующая запись: само число 4, строка «44» (второе повторение, т.е. число дублируется в строке),
строка «444» (третье повторение, т.е. строка множится на 3). Реализуйте вывод множества через функцию set_gen(my_list).
'''


def set_gen(my_list):
    counter = 1
    my_list.sort()
    result = set()
    for num in my_list:
        if num not in result:
            result.add(num)
            counter = 1
        else:
            counter += 1
            result.add(counter * str(num))
    return result



print(set_gen([1, 1, 3, 3, 1]) == {1, 3, '111', '33', '11'})

#Можно сделать через counter из collections