# I  am constructing a stack
class Stack:
    def __init__(self):
        self.item = []
    def Stack(self):
        self.item = []
    def push(self):
        return self.item.append()
    def pop(self):
        self.item.pop()
    def is_empty(self):
        return (len(self.item) > 0)
    def size(self):
        return (len(self.item))
    def peek(self):
        return safe.item[len(self.item) -1]
    
        
