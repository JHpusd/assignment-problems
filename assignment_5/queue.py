class Queue():
    def __init__(self):
        self.data = []

    def enqueue(self, queue_value):
        self.data.append(queue_value)

    def dequeue(self):
        self.data = self.data[0:]

    def peek(self):
        return self.data[0]

print("Asserting that Queue() works...")
q = Queue()
assert q.data == []
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
assert q.data == ['a', 'b', 'c']
q.dequeue()
assert q.data == ['b', 'c']
assert q.peek() == 'b'
assert q.data == ['b', 'c']
