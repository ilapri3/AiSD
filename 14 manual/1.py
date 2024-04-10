import random

class Generator(object):
    def __init__(self):
        self.list = []
    
    def sorted_list_up(self, length):
        self.list = list(range(length))
        return self.list
    
    def sorted_list_down(self, length):
        self.list = list(range(length))[::-1]
        return self.list
    
    def random_list(self, length):
        self.list = [random.randint(0,100) for _ in range(length)]
        return self.list
    
    def almost_sorted_list(self, length):
        self.list = list(range(length))
        random.shuffle(self.list)
        return self.list
    
arr = Generator()

print(f'Упорядоченный список по возрастанию: {arr.sorted_list_up(9)}')
print(f'Упорядоченный список по убыванию: {arr.sorted_list_down(12)}')
print(f'Список случайных чисел: {arr.random_list(5)}')
print(f'Почти упорядоченный список: {arr.almost_sorted_list(6)}')