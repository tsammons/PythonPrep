class Queue:
    
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        if (self.items == []):
            return True

    def size(self):
        return len(self.items)

new_q = Queue()
new_q.enqueue(5)
new_q.enqueue(1)
print(new_q.dequeue())
print(new_q.dequeue())
print(new_q.isEmpty())
