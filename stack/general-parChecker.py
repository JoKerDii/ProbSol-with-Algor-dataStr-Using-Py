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
    To solve the problem of "Balanced Symbols (A General Case)"
    The general problem of balancing and nesting different kinds of opening and closing symbols occurs frequently. 
    
    """
    s = Stack()
    
    balanced = True
    index = 0
    
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{": # in
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol): # "matches" nested function created below
                       balanced = False
        index = index + 1
        
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    """
    To check if the open symbol and close symbol match
    Input: open symbol and close cymbol
    Output: boolean "True" or "False" for match or not
    
    """
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))