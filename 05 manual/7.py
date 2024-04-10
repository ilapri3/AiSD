import re
s = '123@edu.fa.ru Ilya_ivanovich ILYA.I@mail.ru ILYA123@gmail.com finashka@fa.ru '
print(re.findall(r'@(\S*)', s))