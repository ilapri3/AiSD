import re
st = input()
new_st = re.findall(r'\w+\D',st)
print(new_st)