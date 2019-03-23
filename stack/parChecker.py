
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



def parChecker(symbolString):
    """
    Solve the problem of 'Simple Balanced Parentheses'
    Input: symbolString must contain only '(' or ')'
    Output: boolean "True" or "False" for balanced or not

    """
    s = Stack()
    
    balanced = True
    index = 0
    
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        # If there is a "(", push it into s, if it is not "(",it must be ")", then pop "(" from s 
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty(): # for the first loop, if symbolString is empty, return false
                balanced = False
            else:
                s.pop()

        index = index + 1
        
    # After finishing iterating all parentheses in symbolString, 
    # it is balanced(balanced = true) and s is empty (there is not single "("), return true
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))