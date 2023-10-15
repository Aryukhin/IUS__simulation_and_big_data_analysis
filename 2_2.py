'''
На входе имеем список строк разной длины. Необходимо написать функцию all_eq(my_list),
которая вернет новый список из строк одинаковой длины. Длину итоговой строки определяем исходя из самой большой из них.
Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края до требуемого
количества символов. Расположение элементов начального списка не менять.
'''


def all_eq(my_list):
    result = []
    lenght = max(my_list, key = len)
    for word in my_list:
        if len(word) < len(lenght):
            rword = word + (len(lenght) - len(word))*"_"
            result.append(rword)
        else:
            result.append(word)
    return result

print(all_eq(['крот', 'белка', 'выхухоль']) == ['крот____', 'белка___', 'выхухоль'])