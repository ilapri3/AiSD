#1
def multi_2(x, y):
    return x * y

def multi_3(x, y, z):
    return x * y * z

a1 = [15, 10 ,5]
a2 = [3, 1]
a3 = [2, 35, 55]
a4 = [5, 10 ,15, 20]

print(multi_3(int(a1[0]),int(a1[1]),int(a1[2])))
print(multi_2(int(a2[0]),int(a2[1])))
print(multi_3(int(a3[0]),int(a3[1]),int(a3[2])))
print(multi_3(int(a4[0]),int(a4[1]),int(a4[2])), multi_3(int(a4[-3]),int(a4[-2]),int(a4[-1])))
#2
def multi(*nums):
    ans = 1
    for i in nums:
        ans*=i
    return ans
a1 = [15, 10 ,5]
a2 = [3, 1]
a3 = [2, 35, 55]
a4 = [5, 10 ,15, 20]

print(multi(*a1))
print(multi(*a2))
print(multi(*a3))
print(multi(*a4[0:3]),multi(*a4[1:]))
