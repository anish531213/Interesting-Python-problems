class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, item):
        self.data = item
    def set_next(self, item):
        self.next = item

class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def add(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp
    def search(self, item):
        found = False
        current = self.head
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
        return count
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    
        