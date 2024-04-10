import random

def quicksort(array):
    if len(array) < 2: #массивы с 0 и 1 эл уже отсортированы
        return array 
    else:
        pivot = random.choice(array)
        less = [i for i in array if i < pivot]
        equal = [i for i in array if i == pivot]
        greater = [i for i in array if i > pivot]
        return quicksort(less) + equal + quicksort(greater)
    
array = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(array))