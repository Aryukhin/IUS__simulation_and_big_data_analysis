
def limited_sum(my_list, n):
    ans = 0
    for i in my_list:
        if i <= n:
            ans += i
    return ans
print(limited_sum([1, 2, 3, 4, 5, 6, 3, 7], 7) == 31)