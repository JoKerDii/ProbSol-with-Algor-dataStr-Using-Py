
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop() # remove the last

    def removeRear(self):
        return self.items.pop(0) # remove the first

    def size(self):
        return len(self.items)
        

"""
An interesting problem that can be easily solved using the deque data structure is the classic palindrome problem. 
A palindrome is a string that reads the same forward and backward, for example, radar, toot, and madam. 
We would like to construct an algorithm to input a string of characters and check whether it is a palindrome.
"""
def palchecker(aString):

    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))