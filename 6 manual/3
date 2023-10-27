import re
str=input()
array=[]
ans=[]
words=re.findall(r'\b\w+\b',str)
for i in range(len(words)):
    if words[i].isdigit():
        array.append(int(words[i]))
    else:
        array.append(words[i])
if array[-2] == 'repeat':
    ans=(array[:-2])*array[-1]
    ans.append(array[-2])
    ans.append(array[-1])
    print(ans)
else:
    print(array)
