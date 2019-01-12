import modules.linkedList


# removes duplicates from an unsorted linked list.
def removeDups(L):
    seen = set()
    curr = L.head
    while (curr != None and curr.data != None):
        seen.add(curr.data)
        curr = curr.next
    
    newList = modules.linkedList.LinkedList(list(seen))
    return newList

# finds the kth to last element of a singly linked list.
def findElements(L, k):
    n = L.size # length of list
    count = 0
    curr = L.head
    # find kth element
    while (curr != None and count < k):
        curr = curr.next
        count += 1

    # add elems to the list
    elems = []
    while (curr != None and count <= n):
        elems.append(curr.data)
        curr = curr.next
        count += 1
    
    return elems

# deletes a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list,
#  given only access to that node.
def delMiddleNode(node):
    # swap data of node and node->next
    # delete node->next
    node.data = node.next.data
    node.next = node.next.next
    return

# partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, 
# the values of x only need to be after the elements less than x (see below). 
# The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
def partition(L, x):
    curr = L.head
    found = False
    prev = None

    while (curr != None and curr != L.tail.next):
        if (found == True):
            # check if value is less than x
            # if it is, move it to the front of the list
            if (curr.data < x):
                # move node to the front
                node = Node(curr.data)
                node.next = L.head
                L.head = = node
                # delete node from other location
                if (curr.next != None):
                    delMiddleNode(curr)
                # if last node
                else:
                    prev.next = None
                    curr = None
                    break
        if (curr.data = x):
            found = True
        # track prev node in case we need to delete the last node
        prev = curr
    
    return L
    
# helper function for sumLists
# converts linked list digits to number
def listToNum(L):
    mult = 10*L.size # multiplier for each digit
    sums = 0
    curr = L.head
    while (curr != None and curr != L.tail.next):
        sums += curr.data * mult
        mult = mult/10
    return sums

# Given two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at 
# the head of the list. 
# This function adds the two numbers and returns the sum as a linked list.
def sumLists(L1, L2):
    result = []
    # convert
    num1 = listToNum(L1)
    num2 = listToNum(L2)
    sums = str(num1 + num2)

    # add to list first to last digit
    while (len(sums) != 0):
        value = sums[0]
        result.append(int(value))
        sums = sums[1:]
    
    return modules.linkedList.LinkedList(sums)

def listToString(L):
    curr = L.head
    s = ""
    while curr != None and curr != L.tail.next:
        s += curr.data
        curr = curr.next

    return s

def reverseString(s):
    reversedS = ""

    for i in range(len(s)-1, -1, -1):
        reversedS += s[i]
    
    return reversedS

# checks if a linked list is a palindrome.
def isPalindrome(L):
    s = listToString(L)
    reversedS = reverseString(s)
    return s == reversedS

#  Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
# node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.
def intersection(L1, L2):
    # node.isSameNode(other node)
    curr1 = L1.head
    while (curr1 != None and curr1 != L1.tail.next):
        curr2 = L2.head
        while (curr2 != None and curr2 != L2.tail.next):
            if (curr1.isSameNode(curr2)):
                return curr1
    return None

#  Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
def loopDetection(L):
    curr = L.head
    seen = set()
    while (curr != None):
        data = curr.data
        if data in seen:
            return curr
        seen.add(data)
    return curr


if __name__ == '__main__':
    # testing removeDups
    print("Testing removeDups...")
    # initialize list
    # test 1
    ll = modules.linkedList.LinkedList()
    for item in ['A', 'B', 'C', 'B']:
        ll.append(item)
    print("input list: ")
    print(ll.items())
    # remove duplicates
    ll = removeDups(ll)
    print("list after remove dups: ")
    print(ll.items())
    # check
    assert(ll.items().sort() == ['A', 'B', 'C'].sort())
    
    # test 2
    mm = modules.linkedList.LinkedList()
    # add more items
    for item in ['A', 'B', 'C', 'C', 'B', 'D', 'F', 'F']:
        mm.append(item)
    print("input list: ")
    print(mm.items())
    mm = removeDups(mm)
    print("list after remove dups: ")
    print(mm.items())
    assert(mm.items().sort() == ['A', 'B', 'C', 'D', 'F'].sort())
    print("PASSED")

    # testing find Elements
    print('Testing findElements...')
    assert(findElements(ll, 1).sort() == ['B', 'C'].sort())
    assert(findElements(mm, 3).sort() == ['D', 'F'].sort())
    print('Passed')


