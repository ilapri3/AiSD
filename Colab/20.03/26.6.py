class list_array(object):
    def __init__(self, n):
        self.array = []
        self.n = n
    
    def input_array(self):
        for i in range(self.n):
            number = int(input())
            self.array.append(number)

    def show_array(self):
        return self.array
    
    def find_max(self):
        max_number = max(self.array)
        max_index = self.array.index(max_number)
        return {f'максимальное число {max_number}',f'под индексом {max_index}'}
    
    def find_min(self):
        min_number = min(self.array)
        min_index = self.array.index(min_number)
        return {f'минимальное число {min_number}',f'под индексом {min_index}'}

    def check_down_sorted(self):
        if self.array == sorted(self.array)[::-1]:
            return 'Список упорядочен по убыванию'
        else:
            return 'Список не упорядочен по убыванию'
    
    def multiply_on_scalar(self, scalar):
        self.scalar = ''
        return [mosn * self.scalar for mosn in self.array]
    

our_array = list_array(5)
our_array.input_array()

print(f'Заданный список: {our_array.show_array()}')
print(our_array.find_max())
print(our_array.find_min())
print(our_array.check_down_sorted())
print(our_array.multiply_on_scalar(int(input('Введите '))))