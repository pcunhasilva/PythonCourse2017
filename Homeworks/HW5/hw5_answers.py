# Regarding the complexity of the functions. I'm assuming worst case scenarios.

# Define class Node
class Node:
    def __init__(self, _value = None, _next = None):
        self.value = _value
        self.next = _next

    def __str__(self):
        return str(self.value)

# Define class LinkedList
class LinkedList:

    def __init__(self, value): # Class O(n)
        """ Initialize a LinkedList """
        if type(value) is not int: raise ValueError("Please, insert an integer")
        self.head = Node(value)

    def length(self): # Class O(n)
        """ Return the number of Nodes in a LinkedList """
        h = self.head
        size = 1
        while 'next' in dir(h.next):
            size += 1
            h = h.next
        return size

    def addNode(self, new_value): # Class O(n)
        """ Add a node at the end of the LinkedList """
        if type(new_value) is not int: raise ValueError("Please, insert an integer")
        h = self.head
        while 'next' in dir(h.next):
            h = h.next
        else:
            h.next = Node(new_value)

    def addNodeAfter(self, new_value, after__node): # Class O(n)
        """ Remove a node after a given position """
        if not isinstance(new_value, Node):
            if new_value % 1 != 0: raise ValueError("Please, insert an integer")
        if after__node > self.length(): raise ValueError("Invalid position")
        count = 1
        h = self.head
        while count != after__node:
            h = h.next
            count += 1
        move_after = h.next
        h.next = Node(new_value)
        h.next.next = move_after

    def addNodeBefore(self, new_value, before_node): # Class O(n)
        """ Add a node before a given position """
        if not isinstance(new_value, Node):
            if new_value % 1 != 0: raise ValueError("Please, insert an integer")
        if before_node > self.length(): raise ValueError("Invalid position")
        if before_node == 1:
            self.head = Node(new_value, self.head)
        else:
            self.addNodeAfter(new_value, before_node - 1)

    def __str__(self): # Class O(n)
        """ Print the LinkedList """
        listvalues = "%s" % self.head
        h = self.head
        while 'next' in dir(h.next):
            listvalues += ", %s" % (h.next)
            h = h.next
        return listvalues

    def removeNode(self, node__to__remove): # Class O(nlog2n)
    # This is clear the worst function. It goes to different if statements before
    # start the 'real' computation to replace the value
        """ Remove Nodes using their position as the criteria """
        if node__to__remove > self.length():
            raise ValueError("Invalid position. The LinkedList has length %s" % self.length())
        elif node__to__remove == 1:
            if self.length() == 1:
                raise ValueError("The LinkedList has only one node (the head)")
            if self.length() == 2:
                self.head = Node(self.head.next)
            else:
                self.head = Node(self.head.next, self.head.next.next)
        elif (self.length() - 1) == node__to__remove:
            h = self.head
            count = 1
            while count != (node__to__remove - 1):
                h = h.next
                count += 1
            h.next = Node(h.next.next)
        elif self.length() == node__to__remove:
            h = self.head
            count = 2
            while count != (node__to__remove - 1):
                h = h.next
                count += 1
            h.next = Node(h.next)
        else:
            h = self.head
            count = 2
            while count != node__to__remove:
                h = h.next
                count += 1
            h.next = Node(h.next.next, h.next.next.next)

    def removeNodesByValue(self, value): # Class O(nlog2n)
    # I'm assuming this classification because this function
    # calls removeNode()
        """ Remove Nodes by their value """
        h = self.head
        count = 1
        while count <= self.length():
            try:
                if h.value == value:
                    self.removeNode(count)
                    if h.next != h:
                        h = h.next
                        next
                else:
                    count += 1
                    h = h.next
            except:
                break

    def reverse(self): # Class O(nlog2n)
        # I'm assuming this classification because this function
        # calls removeNode() and addNodeAfter()
        """ Reverse the order of the LinkedList """
        listvalues = "%s" % self.head
        h = self.head
        l = self.length()
        count = 0
        while count <= l:
            try:
                self.addNodeAfter(h.value, l - count)
                self.removeNode(1)
                h = h.next
                count += 1
            except:
                break


##################################
############# Examples ###########
##################################

print "Initialize a LinkedList and print"
ll = LinkedList(2)
print ll
print "Add four nodes at the end of the LinkedList and print"
ll.addNode(6)
ll.addNode(2)
ll.addNode(5)
ll.addNode(9)
print ll
print "Add a node after the position 3 and print"
ll.addNodeAfter(99, 3)
print ll
print "Add a node before the position 4 and print"
ll.addNodeBefore(88, 4)
print ll
print "Print the size of the LinkedList"
print ll.length()
print "Remove the last element of the list and print"
ll.removeNode(ll.length())
print ll
print "Remove all nodes with value equal to 2 and print"
ll.removeNodesByValue(2)
print ll
print "Reverse the LinkedList and print"
ll.reverse()
print ll
print "Print the final length of the LinkedList"
print ll.length()
