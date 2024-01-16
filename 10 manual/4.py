f1 = open('file_6.1.4', mode = 'w')
f1.write('String1\nString2')
f1.close()
s = input('enter file name: ')
try:
    with open(s, 'r') as f:
        print(f.readline())
except FileNotFoundError:
    print('no such file exists')