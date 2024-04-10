class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.back = None

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.head = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        info = self.head.info
        self.head = self.head.next
        if self.head is None: 
            self.back = None
        return info

    def is_empty(self):
        return self.head is None

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(len(queue))  
print(queue.dequeue())
print(queue.dequeue()) 
print(queue.is_empty()) 
print(len(queue)) 
