class Node():
    def __init__(self, info):
        self.info = info
        self.next = None

class OneList():
    def __init__(self):
        self.head = None

    def add(self, info):
        new_node = Node(info)
        new_node.next = self.head
        self.head = new_node

    def show_list(self):
        current = self.head
        while current:
            print(current.info)
            current = current.next
        print('Конец однонаправленного списка')


array = OneList()

array.add(1)
array.add(2)
array.add(3)
array.show_list()  
