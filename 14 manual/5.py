import heapq

def merge_list(array):
    merged_list = []
    heap = []

    for i, j in enumerate(array):
        if j:
            heapq.heappush(heap, (j[0], i, 0))
    
    while heap:
        el, index, element_index = heapq.heappop(heap)
        merged_list.append(el)
        
        if element_index + 1 < len(array[index]):
            next_el = array[index][element_index + 1]
            heapq.heappush(heap, (next_el, index, element_index + 1))
    return merged_list

list = [[1, 3, 5], [2, 4, 6],[0, 7, 8]]

result = merge_list(list)
print(result)
