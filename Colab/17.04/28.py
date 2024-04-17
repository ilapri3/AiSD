array = [1,2,3,4,5]
y = 5
list_b = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
n = 0


list_2 = list(map(lambda x: (x ** 2), array))
list_3 = list(map(lambda x: (x ** 3), array))
list_4 = list(map(lambda x: (x * y), array))
list_5 = list(map(lambda x: (x[n]), list_b))


print(f'Все числа списка в квадрате: {list_2}')
print(f'Все числа списка в кубе: {list_3}')
print(f'Все числа списка умноженные на число: {list_4}')
print(f'Список Фамилий из кортежа: {list_5}')
