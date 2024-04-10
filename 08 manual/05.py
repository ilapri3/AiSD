l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]
print([l2[el] if l2[el]>0 else el+1 for el in range(len(l2))])
