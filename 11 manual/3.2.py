def mul(*nums):
    ans = 1
    for i in nums:
        ans*=i
    return ans

numbers = input('Введите ваши числа:').split()
print('Сумма введенных чисел ',sum([int(el) for el in numbers]))
print('Произведение введенных чисел ',mul(*[int(el) for el in numbers]))
