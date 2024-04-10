s = input('')
l = list(s)
for i in range(1, len(l)-1):
    if l[i] == 's' or l[i] == 'S':
        l[i] = l[i-1]*2 + l[i+1]
print(l)
