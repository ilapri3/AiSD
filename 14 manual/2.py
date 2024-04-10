def selection_sort(array):
    n = len(array)
    for i in range(n):
        minimum_index = i
        for j in range(i+1, n):
            if array[j] < array[minimum_index]:
                minimum_index = j
        array[i], array[minimum_index] = array[minimum_index], array[i]
    return array

def stone_bubble_modified(array, sublist_size):
    n = len(array)
    for i in range(0, n, sublist_size):
        underlist = array[i:i+sublist_size]
        selection_sort(underlist)
        array[i:i+sublist_size] = underlist
    return array

array = [5, 3, 8, 6, 2, 7, 1, 4]
sublist_size = 3
sorted_array = stone_bubble_modified(array, sublist_size)
print(sorted_array)