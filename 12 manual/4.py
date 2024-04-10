class Node():
    def __init__(self, info):
        self.info = info
        self.prev = None
        self.next = None

class TwoList():
    def __init__(self):
        self.head = None
        self.back = None

    def add(self, info):
        new_node = Node(info)
        if self.head is None: 
            self.head = new_node
            self.back = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def show_front_to_back(self):
        current = self.head
        while current:
            print(current.info)
            current = current.next
        print('Конец списка')

    def show_back_to_front(self):
        current = self.back
        while current:
            print(current.info)
            current = current.prev
        print('Конец списка')



array = TwoList()
array.add(1)
array.add(2)
array.add(3)
array.show_front_to_back() 
array.show_back_to_front()
