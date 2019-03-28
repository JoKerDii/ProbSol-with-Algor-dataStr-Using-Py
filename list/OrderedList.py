"""
OrderedList() creates a new ordered list that is empty. It needs no parameters and returns an empty list.

add(item) adds a new item to the list making sure that the order is preserved. 
It needs the item and returns nothing. Assume the item is not already in the list.

remove(item) removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.

search(item) searches for the item in the list. It needs the item and returns a boolean value.

isEmpty() tests to see whether the list is empty. It needs no parameters and returns a boolean value.

size() returns the number of items in the list. It needs no parameters and returns an integer.

index(item) returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.

pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.

pop(pos) removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list."""

class Node:
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


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item: # because the list is ordered
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item: # because the list is ordered
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

# test

mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
