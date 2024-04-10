# from collections import deque

# def generator(queue_1, queue_2):
#     while queue_1 or queue_2:
#         if queue_1:
#             yield queue_1.pop() #главный плюс вывода с помощью yeild в том, что мы не записываем в память наш выведеннный результат. Также можем выводить поочередно, только при вызове методы next()
#         if queue_2:
#             yield queue_2.pop()

# q_1 = deque([1,2,3,4,5])
# q_2 = deque([6,7,8,9,10])

# array = generator(q_1, q_2)

# for i in range(10):
#     print(next(array))

from collections import deque

def generator(queue_1, queue_2):
    count = 0
    while queue_1 or queue_2: #пока одна из очередей не пуста
        if count % 2 == 0:
            print(queue_1.pop()) #вывод конечного значения дека
        elif count % 2 == 1:
            print(queue_2.pop()) #вывод конечного значения дека
        count += 1

q_1 = deque([1,2,3,4,5])
q_2 = deque([6,7,8,9,10])

array = generator(q_1, q_2)
try:
    for el in array:
        print(next(el))
except Exception:
    print('')