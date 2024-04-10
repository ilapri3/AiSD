from collections import deque

class Pump:
    def __init__(self, queue, generator):
        self.queue = queue
        self.generator = generator

    def action(self):
        value = next(self.generator)
        self.queue.append(value)

class MultiAction:
    def __init__(self, n, action_class, *args, **kwargs):
        self.n = n
        self.action_a = [action_class(*args, **kwargs) for _ in range(n)]

    def action(self):
        for action_a in self.action_a:
            action_a.action()

class MultiPump:
    def __init__(self, queues, generator):
        self.queues = queues
        self.generator = generator
        self.queue_index = 0

    def action(self):
        value = next(self.generator)
        current_queue = self.queues[self.queue_index]
        current_queue.append(value)
        self.queue_index = (self.queue_index + 1) % len(self.queues)


generator = iter(range(12))


queue_a = deque()
pump = Pump(queue_a, generator)
pump.action()
print("Очередь 1:", queue_a)


queue = deque()
multi_action = MultiAction(3, Pump, queue, generator)
multi_action.action()
print("Очередь 2:", queue)


queue_1 = deque()
queue_2 = deque()
multi_pump = MultiPump([queue_1, queue_2], generator)
for _ in range(7):
    multi_pump.action()
print("Очередь 3:", queue_1)
print("Очередь 4:", queue_2)
