class S():
    def __init__(self, max_length):
        self.stack = []
        self.max_length = max_length
    
    def push(self, el):
        if len(self.stack) >= self.max_length:
            return f'Произошел перегруз стека'
        self.stack.append(el)
    
    def pop(self):
        # if len(self.stack) == 0:
        #     return f'Стек пуст'
        self.is_empty()
        return self.stack.pop()
    
    def top(self):
        # if len(self.stack) == 0:
        #     return f'Стек пуст'
        self.is_empty()
        return self.stack[-1]
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def len(self):
        return len(self.stack)


stack = S(6)

stack.push(2)
stack.push(12)
stack.push(25)
stack.push(159)

print(stack.is_empty())

print(stack.top())
print(stack.len())
print(stack.pop())
print(stack.len())