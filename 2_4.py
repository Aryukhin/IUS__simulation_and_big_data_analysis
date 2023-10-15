'''
Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется создать словарь, который в качестве
ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в
имеющейся последовательности. Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
'''
from collections import Counter
def count_it(sequence):
    result = {}
    lst_num = []
    for num in sequence:
        lst_num.append(int(num))
    res = Counter(lst_num).most_common(3)
    result.update(res)
    return result


print(count_it('007767757744331166554444'))