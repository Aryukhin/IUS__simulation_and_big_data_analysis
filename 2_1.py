'''
Имеется список пар (фамилия, долг) my_list и число dept. Нужно написать функцию sorted_dept(my_list, dept), которая
 для каждой фамилии находит суммарный долг, сортирует фамилии в порядке уменьшения суммарного долга и выводит
 отсортированный список фамилий, у которых долг строго больше dept. Одна и та же фамилия может встречаться несколько
 раз, и тогда долги по ней суммируются.
'''


def sorted_dept(my_list, dept):
    res = {
    }
    result = []
    for surname in my_list:
        if surname[0] not in res:
            res.setdefault(surname[0], surname[1])
        else:
            res[surname[0]] += surname[1]


    sorted_dict = sorted(res.items(), key=lambda x: x[1], reverse=True)

    for deptor in sorted_dict:
        if deptor[1] > dept:
            result.append(deptor[0])

    return result


print(sorted_dept([('Ivanov', 1), ('Petrov', 2), ('Ivanov', 2), ('Sidorov', 4)], 1))