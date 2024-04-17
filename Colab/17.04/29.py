from functools import reduce
bases = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
exponents = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_a = [15, 62, 2, 34, 11, 5, 8, 12]


result = list(map(lambda x, y: (x ** y), bases, exponents))
new_list_a = list(filter(lambda x: (x>10), list_a))
new_list_a_summ = reduce((lambda x, y: x + y), list_a)


print(result)
print(sorted(new_list_a))
print(new_list_a_summ)
