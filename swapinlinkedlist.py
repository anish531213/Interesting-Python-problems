from LinkedList import LinkedList

l = LinkedList()
l.add(5)
l.add(7)
l.add(10)
l.add(67)
SwapLinkedList(l)

def SwapLinkedList(l):
    current = self.head().get_next()
    previous = self.head()
    while current != None:
        previous.set_next() = current.get_next()
        current.set_next() = previous
        tmp = currrent.get_next()
        current = tmp.get_next()

