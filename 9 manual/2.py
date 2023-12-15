def multi_2(x, y):
    return x * y

def multi_3(x, y, z):
    return x * y * z

array = [n for n in input().split()]
list_num = ' '.join(array)

if len(array) == 1:
    print(list_num)
elif len(array) == 2:
    print(multi_2(int(array[0]),int(array[1])))
elif len(array) == 3:
    print(multi_3(int(array[0]),int(array[1]),int(array[2])))