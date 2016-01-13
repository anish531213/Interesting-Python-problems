
class Stack:
    def __init__(self):
        self.item = []
    def push(self, element):
        self.item.append(element)
    def peek(self):
        return self.item[len(self.item)-1]
    def size(self):
        return len(self.item)
    def is_empty(self):
        return (self.item == [])
    def pop(self):
        return self.item.pop()
