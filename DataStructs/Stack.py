class Stack:
    
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

new_stack = Stack()
new_stack.push(3)
new_stack.push(1)
new_stack.pop()
print(new_stack.peek())
