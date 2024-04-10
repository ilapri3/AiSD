def multi_all(*nums):
    ans = 1
    for i in nums:
        ans*=i
    return ans

print(multi_all(1, 2, 3, 4))
