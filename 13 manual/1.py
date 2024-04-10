class Dar(object):
    def __init__(self): #создание конструктора класса
        self.array = []
    
    def append(self, e): #добавление элемента в динамический массив
        self.array.append(e)

    def output(self): #вывод динамического массива
        return self.array
    
    def get_el_ind(self, index): #получение элемента динамического массива по индексу
        return self.array[index]

    def set_new_value(self, index, value): #установка нового значения по индексу
        self.array[index] = value
    
    def delete_el(self, index): #удаление элемента в динамическом массиве по индексу
        self.array.pop(index)

    def lengt(self): #вывод длинны массива
        return len(self.array)

arr = Dar()

for i in range(1,10,2): #заносим значения в жинамический массив
    arr.append(i)

print(arr.output())
print(arr.get_el_ind(1))

arr.set_new_value(1,2)
print(arr.lengt())

arr.delete_el(1)
print(arr.output())

