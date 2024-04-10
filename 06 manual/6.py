s1 = ['один', 'два', 'три']
s2= ['альфа', 'бетта', 'гамма']
len_max = max(len(s1),len(s2))
ans= []
for i in range(len_max):
    ans.append(s1[i])
    ans.append(s2[i])
print(ans)
