class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, el):
        self.stack.append(el)
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed
    
    def empty(self):
        if len(self.stack) == 0:
            return f'Данный стек пустой, все выполнено верно!'


def brack(array):
    stack = Stack()
    for el in array:
        if el =='(':
            stack.push(el)
        elif el == ')':
            if stack.empty():
                return f'Данный стек некорректен'
            stack.pop()
    return stack.empty()

stroke_1 = '((dsasdas((das(d)das)d)asd)da)'
stroke_2 = '(f(gfhd((hgfdg((fghh)dads)das))ds)adddads())))'

print(f'Первый пример: {brack(stroke_1)}')
print(f'Второй пример: {brack(stroke_2)}')