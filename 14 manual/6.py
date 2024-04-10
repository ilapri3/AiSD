def shell(n, k):
    move = 2 * (n // (2 ** k) + 1) + 1
    return move

n = 100
k = 3
result = shell(n, k)
print(result)