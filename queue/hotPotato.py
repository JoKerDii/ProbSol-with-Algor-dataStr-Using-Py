"""
Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
size() returns the number of items in the queue. It needs no parameters and returns an integer.
"""
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
"""
Simulation: Hot Potato

In this game children line up in a circle and pass an item from neighbor to neighbor as fast as they can. 
At a certain point in the game, the action is stopped and the child who has the item (the potato) is removed from the circle. 
Play continues until only one child is left.

"""
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue()) # take away the first one, add it to the end, then a loop forms

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
