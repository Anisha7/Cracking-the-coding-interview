from stacksAndQueues import Queue
import modules.linkedList
import random

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

# 6. Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.
# if there is no right node:
    # return parent node
# else:
    # go to right node
    # while left is not none, go left
    # return it
def successor(n):
    if (n == None):
        return None
    if (n.right == None):
        return n.parent
    # else
    temp = n.right
    while (temp.left != None):
        temp = temp.left
    return temp

# 7. You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c
class graphNode(object):
    def __init__(self, data, child=None):
        """Initialize this node with the given data."""
        self.data = data
        self.child = child 
        self.visited = False

def findNode(nodes, data):
    for i in range(len(nodes)):
        if (nodes[i].data == data):
            return nodes[i]
    return None

def search(root, n, path =[]):
    if (path == None):
        return None
    if (root == None):
        if (len(path) == n and n == len(set(path))):
            return path 
        return None;

    path.append(root.data)
    root.visited = True
    path = search(root.child, path)
    root.visited = False

    # check if solution is found
    if (len(path) == n and n == len(set(path))):
        return path
    return None

def buildOrder(projects, dependencies):
    # set up dict for dependencies
    dep = dict()
    for d in dependencies:
        dep[d[0]] = d[1]

    # set up graph
    nodes = []
    for proj in projects:
        nodes.append(graphNode(proj))
    
    for i in range(len(nodes)):
        if (dep.get(nodes[i].data)):
            child = findNode(nodes, dep[nodes[i].data])
            nodes[i].child = child

    # find a path
    for node in nodes:
        result = search(node)
        if (result != None):
            return result
    return None   
    

# 8. Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. 
# NOTE: This is not necessarily a binary search tree.
def firstCommonAncestor(node1, node2):
    


# 9. BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.

def bstSequences():


# 10. Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. 
# Create an algorithm to determine if T2 is a subtree of Tl. A tree T2 is a subtree of Tl 
# if there exists a node n in Tl such that the subtree of n is identical to T2. That is, if 
# you cut off the tree at node n, the two trees would be identical.
def checkSubtree(T1, T2):
    # find node in T1 that matches T2
    # check if all left and right nodes from that node are identical in both trees


# 11. Random Node: You are implementing a binary tree class from scratch which, in addition to
# insert, find, and delete, has a method getRandomNode() which returns a random node
# from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for getRandomNode, and explain how you would implement the rest of the methods.
def length(T,):
    if (T == None):
        return 0
    return 1 + length(T.left) + length(T.right)

def randomNode(T):
    n=random.randInt(length(T))
    return getRandomNode(T,n)

def getRandomNode(T, n):
    if (T == null):
        return None
    if (n == 0):
        return T.data

    l = getRandomNode(T.left, n-1)
    r = getRandomNode(T.right, n-2)
    if (l != None):
        return l
    if (r != None):
        return r
    return T.data


# 12. Paths with Sum: You are given a binary tree in which each node contains an integer value (which
# might be positive or negative). Design an algorithm to count the number of paths that sum to a
# given value. The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).
def pathsWithSum():
