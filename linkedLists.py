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


