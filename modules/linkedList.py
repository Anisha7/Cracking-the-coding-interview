#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        # O(1)
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Q1: Running time: O(1) Why and under what conditions?
        O(N) because needs to count all the elements, thus loop through entire list"""
        # Loop through all nodes and count one for each
        # curr = self.head
        # count = 0
        # while (curr != None):
        #     count += 1
        #     curr = curr.next
        
        # return count
        # (update) faster to track and return size
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Q1: Running time: O(???) Why and under what conditions?
        O(1) to add item at the end of the list because we track the end"""
        # Create new node to hold given item
        # Append node after tail, if it exists
        new_node = Node(item)
        self.size += 1
        # if empty linked list
        if (self.head == None):
            self.head = new_node
            self.tail = self.head
        # place in next empty location
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
            

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Q1: Running time: O(???) Why and under what conditions?"""
        # O(1) because we keep track of head
        # Create new node to hold given item
        # Prepend node before head, if it exists
        new_node = Node(item)
        self.size += 1
        if (self.head == None):
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Q1: Best case running time: O(???) Why and under what conditions?
        O(1) if first item meets requirements
        Q2: Worst case running time: O(???) Why and under what conditions?
        O(N) if last or no items meet requirements"""
        # Loop through all nodes to find item where quality(item) is True
        # Check if node's data satisfies given quality function

        curr = self.head
        while (curr != None):
            if (quality(curr.data)):
                return curr.data
            curr = curr.next
        
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Q1: Best case running time: O(???) Why and under what conditions?
        O(1) if item is the first element
        Q2: Worst case running time: O(???) Why and under what conditions?
        O(N) if item is the last element or not found"""
        # Loop through all nodes to find one whose data matches given item
        # Update previous node to skip around node with matching data
        # Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        self.size -= 1
        curr = self.head
        prev = None
        found = False
        while (curr != None):
            if (curr.data == item):
                found = True
                # if first element
                if (prev == None):
                    self.head = self.head.next
                else:
                    prev.next = curr.next
                    # if deleting last element, reset self.tail
                    if (prev.next == None):
                        self.tail = prev

                # if list had only one element
                if (self.tail != None and self.tail.data == item):
                    self.tail = None
                # break out of loop when item is deleted
                break

            prev = curr
            curr = curr.next
        
        # item not found
        if (found == False):
            raise ValueError('Item not found: {}'.format(item))

    def replace(self, item, new_item):
        # replace an item in linked list
        # O(N) worst case
        curr = self.head
        # iterate over list to find node holding item
        while (curr != None):
            # if node is found
            if (curr.data == item):
                # change its value
                curr.data = new_item
                # end function if item is replaced
                return
            # check next node
            curr = curr.next
        
        # item not found
        #raise ValueError('Item not found: {}'.format(item))
        return 

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
