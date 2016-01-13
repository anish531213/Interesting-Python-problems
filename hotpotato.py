from Queue import Queue

def hot_potato(l, num):
    q = Queue()
    for i in l:
        q.enqueue(i)
    while q.size() > 1:
        for j in range(num):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()

z = hot_potato(["Bill", "David", "Susan", "Jane", "Kent","Brad"], 7)
print(z)

        
