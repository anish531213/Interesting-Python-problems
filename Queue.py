class Queue:
    def __init__(self):
        self.item = []
    def enqueue(self, items):
        self.item.insert(0, items)
    def dequeue(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
    def is_empty(self):
        return (self.item == [])
