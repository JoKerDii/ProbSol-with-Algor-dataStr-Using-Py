
class Node:
    """A reference to None will denote the fact that there is no next node. 
    Note in the constructor that a node is initially created with next set to None."""

    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

# We create Node objects in the usual way.
# temp = Node(93)
# temp.getData()

class UnorderedList:
    """the UnorderedList class must maintain a reference to the first node. 
    Note that each list object will maintain a single reference to the head of the list"""

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
        
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    """The next methods that we will implement–size, search, and remove–are all based on a technique known as linked list traversal. 
    Traversal refers to the process of systematically visiting each node. """
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        # As long as there are more nodes to visit and we have not found the item we are looking for, 
        # we continue to check the next node. 
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False

        # traverse the list looking for the item we want to remove
        # If we do not find the item, previous and current must both be moved one node ahead.
        # previous must first be moved one node ahead to the location of current. At that point, current can be moved.
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # When found becomes True, current will be a reference to the node containing the item to be removed. 
        # In order to remove the node containing the item, we need to modify the link in the previous node so that it refers to the node that comes after current
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


# test


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))

