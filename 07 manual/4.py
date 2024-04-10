from sem_3 import dict
from sem_3 import evgen_o
count=0
array=list(dict.keys())
for i in range(len(array)):
    if array[i].islower():
        count+=dict[list(set(evgen_o))[i]]
print(count)
