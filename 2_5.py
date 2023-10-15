'''
Вам известны количество продаж разных товаров. Они представлены в виде списка my_list: первое значение - число
продаж первого товара, второе значение - второго, и так далее. Напишите функцию get_most_popular(my_list, n, threshold),
которая будет выдавать список из порядковых номеров самых популярных товаров (порядковые номера - 0, 1, 2 и т.д.),
чей объём продаж выше заданного числа threshold. Длина такого списка должна быть не более n, т.е. нужно выдать номера
n самых популярных товаров.
'''
'''
def get_most_popular(my_list, n, threshold):
    res = []
    r_lst = sorted(my_list, reverse=True)
    print(r_lst)
    for i in range(n):
        if r_lst[i] > threshold:

            res.append(my_list.index(r_lst[i]))

    return res


print(get_most_popular([1, 2, 3, 4, 5, 6, 3, 7], 7, 1))
'''
def get_most_popular(my_list, n, threshold):
    d_prices = {}
    res = []
    for i in range(len(my_list)):
        d_prices.setdefault(i, my_list[i])
    print(d_prices)
    sorted_dict = sorted(d_prices.items(), key=lambda x: x[1], reverse=True)
    for j in range(n):
        if sorted_dict[j][1] >= threshold:
            res.append(sorted_dict[j][0])
    print(sorted_dict)
    return res
print(get_most_popular([1, 2, 3, 4, 5, 6, 3, 7], 7, 2))