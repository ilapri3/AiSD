def mul(*nums):
    ans = 1
    for i in nums:
        ans*=i
    return ans

numbers = input('Введите ваши числа:').split()
action = input('Введите тип действия над числами:')
if len(action) == 1:
    if action == '+':
        print('Сумма введенных чисел ',sum([int(el) for el in numbers]))
    elif action == '*':
        print('Произведение введенных чисел ',mul(*[int(el) for el in numbers]))
else:
    print('Неверный ввод')