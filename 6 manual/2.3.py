import re
st = input()
new_st = re.findall(r'\d+',st)
print(new_st)