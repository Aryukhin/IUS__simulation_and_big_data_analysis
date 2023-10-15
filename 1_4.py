'''
Написать функцию is_prime(num), принимающую 1 аргумент num — число от 0 до 1000, и возвращающую True, если оно простое,
 и False - иначе.
'''

def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if num == 1:
        return False
    if counter <= 2:
        return True
    else:
        return False
print(is_prime(2))