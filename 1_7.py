'''Есть два списка чисел: list1 - цены товаров в одном магазине - и list2 - цены товаров в другом магазине.
 Напишите функцию compare_prices(list1, list2), которая будет сравнивать средние цены (среднее берётся по всем товарам),
  минимальные и максимальные цены в магазинах. Если первое значение меньше, то надо вернуть 'First', если второе,
то 'Second', а если равны, то 'Equal
'''
from statistics import mean
def compare_prices(list1, list2):
    ans = []
    dic = {
        1 : 'First',
        2 : 'Second',
        3 : 'Equal'
    }
    mean_price1 = mean(list1)
    mean_price2 = mean(list2)
    if mean_price1 < mean_price2:
        ans.append(dic[1])
    elif mean_price1 > mean_price2:
        ans.append(dic[2])
    else:
        ans.append(dic[3])
    if min(list1) < min(list2):
        ans.append(dic[1])
    elif min(list1) > min(list2):
        ans.append(dic[2])
    else:
        ans.append(dic[3])
    if max(list1) < max(list2):
        ans.append(dic[1])
    elif max(list1) > max(list2):
        ans.append(dic[2])
    else:
        ans.append(dic[3])

    return ans

print(compare_prices([1, 2, 3], [2, 2, 2]))