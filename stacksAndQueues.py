# 1. Describe how you could use a single array to implement three stacks.
# Track indices of starting points of each stack. 
# Insert at that index each time, and remove from that index.

# 2. How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.
# Use a OOP class and linked list to implement the stack. Track the front element
# of the linked list. For push and pop, add and remove from the front. As you add elements,
# keep track of the minimum element. Compare to the saved 'min' element in the class, and alter
# it as you add elements. The min function will just return that min element that we have been
# tracking.

# 3. Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).

class Node(object):
    
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.min = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class Stack(object):
    def __init__(self,items=None):
        self.head = None
        self.size = 0

        if items is not None:
            for item in items:
                self.push(item)
    
    def push(self,data):
        # First in first out
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

        if self.min is None or self.min > data:
            self.min = data

    def pop(self):
        if self.head is None:
            return None
        temp = self.head.data
        self.head = self.head.next
        return temp

    def peek(self):
        return self.head.data

    def min(self):
        return self.min
    

class SetOfStacks(object):
    def __init__(self,items=None):
        self.head = None
        self.capacity = 15
        self.stacks = [Stack()]
        self.min = 0

        if items is not None:
            for item in items:
                self.push(item)

    def push(self, data):
        # capacity met
        if (self.stacks[-1].size > self.capacity):
            # add new stack
            self.stacks.append(Stack())
        
        # add element to the last stack
        self.stacks[-1].push(data)

        if self.min is None or self.min > data:
            self.min = data        

    def pop(self):
        return self.stacks[-1].pop()
    
    def min(self):
        return self.min


# 4. Implement a MyQueue class which implements a queue using two stacks.
        