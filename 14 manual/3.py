def quicksort(array):
    if len(array) < 2: #массивы с 0 и 1 эл уже отсортированы
        return array 
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
array = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(array))