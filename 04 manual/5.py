str=input()
ans_str=''
for i in range(1,len(str)-1):
    if len(str) % i == 0:
        ans_str = ans_str + str[i-1]
print(ans_str+str[-1])
