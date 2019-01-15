# 1. Describe how you could use a single array to implement three stacks.
# Track indices of starting points of each stack. 
# Insert at that index each time, and remove from that index.

# 2. How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.
# Use a OOP class and linked list to implement the stack. Track the front element
# of the linked list. For push and pop, add and remove from the front. As you add elements,
# keep track of the minimum element. Compare to the saved 'min' element in the class, and alter
# it as you add elements. The min function will just return that min element that we have been
# tracking. when an element is deleted, find the new min element, by adding everything to a list

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
        self.min = 0

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class Stack(object):
    def __init__(self,items=None):
        self.head = None
        self.size = 0
        self.min = None
        self.max = None
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
        
        if self.max is None or self.max < data:
            self.max = data

        self.size += 1

    def pop(self):
        self.size -= 1
        if self.head is None:
            return None
        temp = self.head.data
        self.head = self.head.next
        return temp

    def peek(self):
        return self.head.data

    def min(self):
        return self.min

    def max(self):
        return self.max

    def isEmpty(self):
        return self.size <= 0
    

class SetOfStacks(object):
    def __init__(self,items=None):
        self.head = None
        self.capacity = 15
        self.stacks = [Stack()]

        if items is not None:
            for item in items:
                self.push(item)

    def push(self, data):
        self.size += 1
        # capacity met
        if (self.stacks[-1].size > self.capacity):
            # add new stack
            self.stacks.append(Stack())
        
        # add element to the last stack
        self.stacks[-1].push(data)       

    def pop(self):
        self.size -= 1
        return temp

# 4. Implement a MyQueue class which implements a queue using two stacks.
class Queue(object):
    def __init__(self, items = None):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.size = 0
        
        if items is not None:
            for item in items:
                self.push(item)

    def enqueue(self, data):
        self.stack1.push(data)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        if (self.stack2.size <= 0):
            while (self.stack2.size > 0):
                self.stack2.push(self.stack2.pop())
        
        return self.stack2.pop()

    def peek(self):
        if (self.stack2.size <= 0):
            while (self.stack2.size > 0):
                self.stack2.push(self.stack2.pop())
        
        return self.stack2.peek()

    def isEmpty(self):
        return self.size == 0

# 5. Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.

def findMax(s):
    temp = Stack()
    maximum = None
    while (s.isEmpty() == False):
        data = s.pop()
        # pop from s, check if it is greater than max
        if maximum is None or maximum < data:
            maximum = data
        
        temp.push(data)

    while (temp.isEmpty() == False):
        s.push(temp.pop())
    
    return maximum

def addMax(s, result):
    temp = Stack()
    result = Stack()
    data = None
    maximum = findMax(s)
    found = False
    while (s.isEmpty() == False and found == False):
        if (data != maximum):
            temp.push(data)
            data = s.pop()
        else:
            result.push(data)
            found = True
    
    while (temp.isEmpty() == False):
        s.push(temp.pop())

    return (s,result)


def sortStack(s):
    result = Stack()
    while (s.isEmpty() == False):
        val = addMax(s, result)
        s = val[0]
        result = val[1]

    return result

# 6. An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linked list data structure.

# items are a tuple = (name, type) where type is a string 'dog' or 'cat'
class animalQueue(object):
    def __init__(self, items=None):
        self.dogs = Queue()
        self.cats = Queue()
        self.first = None # string tracks whether first was dog or cat
        self.size = 0
        self.count = 0
        if items is not None:
            for item in items:
                self.enqueue(item)

    def enqueue(self, data):
        if (self.size == 0):
            self.first = (data[1],self.count)
            self.count = 0
        if (data[1] == 'dog'):
            self.dogs.enqueue((data[1],self.count))
            self.last = 'dog'
        else if (data[1] == 'cat'):
            self.cats.enqueue((data[1],self.count))
            self.last = 'cat'
        
        self.size += 1
        self.count += 1

    def redefineFirst(self):
        cat = self.cats.peek()[1]
        dog = self.dogs.peek()[1]

        if cat < dog:
            self.first = 'cat'
        else:
            self.first = 'dog'

    def dequeueAny(self):
        self.size -= 1
        val = None
        if (self.last == 'dog'):
            val = self.dogs.dequeue()
        else if (self.last == 'cat'):
            val = self.cats.dequeue()
        
        self.redefineFirst()
        return val

    def dequeueCat(self):
        self.size -= 1
        val = self.cats.dequeue()[0]
        
        self.redefineFirst()
        return val
    
    def dequeueDog(self):
        self.size -= 1
        val = self.dogs.dequeue()[0]

        self.redefineFirst()
        return val

