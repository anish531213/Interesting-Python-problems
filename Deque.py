class Deque:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return (self.item == [])
    def add_front(self, items):
        self.item.insert(0, items)
    def add_rear(self, items):
        self.item.append(items)
    def remove_front(self):
        return self.item.pop(0)
    def remove_rear(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
    
