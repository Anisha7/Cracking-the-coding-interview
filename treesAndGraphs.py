from stacksAndQueues import Queue
import modules.linkedList

class Node(object):
    
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.adjacent = None # list of nodes it points to
        self.marked = None # if visited

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


# 1. Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.
# use breadth first search
def routeBetweenTwoNodes(A, B):
    Q = Queue()
    A.marked = True
    Q.enqueue(A)

    while (Q.isEmpty == False):
        r = Q.dequeue()
        # check if r = B
        if (r.data == B.data):
            return True
        # loop through each neighbor node 
        for n in r.adjacent:
            # if it is not marked:
            if (n.marked == False):
                # mark it
                n.marked = True
                # add it to the queue
                Q.enqueue(n)
    return False

# 2. Given a sorted (increasing order) array with unique integer elements, write an algorithm
# to create a binary search tree with minimal height.

class TreeNode(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.left = None 
        self.right = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

def minimalTree(L):
    if (len(L) == 0):
        return
    mid = len(L)/2
    root = TreeNode(L[mid])
    minimalTree(L[:mid], root.left)
    minimalTree(L[mid+1:], root.right)
    return root

# 3. Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
def listOfDepths(T, result = [], depth = 0):
    if (T == None):
        return result
    if (len(result) < depth):
        result.append(LinkedList())
    result[depth].append(T)
    result = listOfDepths(T.left, result, depth + 1)
    result = listOfDepths(T.right, result, depth + 1)
    return result

# 4. Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the 
# two subtrees of any node never differ by more than one.
def getHeight(T, height = 0):
    if (T == None):
        return height
    
    left = getHeight(T.left, height + 1)
    right = getHeight(T.right, height + 1)
    return max(left, right)

def checkBalanced(T):
    left = getHeight(T.left)
    right = getHeight(T.right)
    
    return abs(right - left) <= 1

# 5. Implement a function to check if a binary tree is a binary search tree.
def validateBST(T):
    if (T == None):
        return True
    # left is greater than root
    if (T.left != None and T.left.data > T.data):
        return False
    # right is smaller than root
    if (T.right != None and T.right.data < T.data):
        return False
        
    return validateBST(T.left) and validateBST(T.right)