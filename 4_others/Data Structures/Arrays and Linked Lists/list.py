"""An Element has some value associated with it (which could be anything —
a number, a string, a character, et cetera), and it has a variable that 
points to the next element in the linked list. """
import pdb

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
"""This code is very similar — we're just establishing that a LinkedList is
something that has a head Element, which is the first element in the list.
If we establish a new LinkedList without a head, it will default to None."""

class LinkedList(object):
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
    def append(self, value):
        """adds a new Element to the end of our LinkedList"""
        cur = self.head
        if self.head:
            while (cur.next):
                cur = cur.next
            cur.next = Element(value)
        else:
            self.head = Element(value)
    
    def pop(self):
        cur = self.head
        if cur == None:
            return None
        if cur.next == None:
            val = cur.value
            self.head = None
            #pdb.set_trace()
            return val
        while cur.next:
            if (cur.next.next == None):
                val = cur.next.value
                cur.next = None
                return val
            cur = cur.next
        
    def get_position(self, position):
        """Get an Element from a particular position. Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position > 0:
            current = self.head
            counter = 1
            while current:
                if counter == position:
                    return current
                current = current.next
                counter += 1
            # position too large
            return None
        else:
            # position too small
            return None
    
    def insert(self, value, position):
        """Insert a new node at the given position. Assume the first position is "1".
        Inserting at position 3 means between the 2nd and 3rd elements."""
        i = position - 1
        cur = self.head
        new_element = Element(value)
        if position > 0:
            if i == 0:
                new_element.next = cur
                self.head = new_element
            else:
                while(i == 2):
                    #pdb.set_trace()
                    cur = cur.next
                    i -= 1
                new_element.next = cur.next
                cur.next = new_element


    def delete(self, value):
        """Delete the first node with a given value."""
        cur = self.head
        if cur.value == value:
            self.head = cur.next
        else:
            while cur.next:
                if cur.next.value == value:
                    cur.next = cur.next.next
                    break
    def size(self):
        """Return the size of list"""
        n = 1
        cur = self.head
        if cur == None:
            return 0
        while cur.next:
            cur = cur.next
            n+=1
            
        return n
    def reverse(self):
        cur = self.head
        new_list = LinkedList()
        prev_node = None
        while cur:
            new_node = Element(cur.value)
            new_node.next = prev_node
            prev_node = new_node
            cur = cur.next
        
        new_list.head = prev_node
        return new_list
                
def reverse_recursion(head):
    if head is None or head.next is None:
        return head
    	
    new_head = reverse_recursion(head.next)
    pdb.set_trace()
    head.next.next = head
    head.next = None
    
    return new_head

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
my_ll = LinkedList(e1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
print("Should size is 4: ", my_ll.size())

# Test get_position
print("Should print 4: ", my_ll.head.next.next.value)
print("Should also print 4: ", my_ll.get_position(3).value)

# Test insert
e8 = Element(8)
my_ll.insert(8,3)
print("Should print 3 now: ", my_ll.get_position(3).value)
#pdb.set_trace()
print("Should size is 5: ", my_ll.size())

# Test delete
my_ll.delete(1)
print("Should print 2 now: ", my_ll.get_position(1).value)
print("Should print 3 now: ", my_ll.get_position(2).value)
print("Should print 4 now: ", my_ll.get_position(3).value)
print("Should print 4 now: ", my_ll.get_position(4).value)
print("Should size is 4: ", my_ll.size())

#flipped = my_ll.reverse()
flipped = reverse_recursion(my_ll.head)
