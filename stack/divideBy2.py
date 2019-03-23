class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def divideBy2(decNumber):
    """
    Converting Decimal Numbers to Binary Numbers
    
    """
    remstack = Stack()

    # In remstack, the rems are stored in an order of "10010111"
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    
    # The order is correct by pop() in Stack, it is the reverse order of them in remstack "11101001"
    # That's nature of Stack, which is "last in first out (LIFO)"
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(233))