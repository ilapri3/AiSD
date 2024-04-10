import re
s = '''Yesterday All my troubles seemed so far away
but tomorrow will be better than yerterday
If we all believe in it'''
s1 = re.split('\n', s)
for i in range(0, len(s1)):
    print(re.findall(r'^\w+', s1[i]))