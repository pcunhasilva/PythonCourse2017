# Define class Node
class Node:
    def __init__(self, _value = None, _next = None):
        self.value = _value
        self.next = _next

    def __str__(self):
        return str(self.value)

# Define class LinkedList
class LinkedList:

    def __init__(self, value):
        self.head = Node(value)

    def length(self):
        h = self.head
        size = 1
        while 'next' in dir(h.next):
            size += 1
            h = h.next
        return size

    def addNode(self, new_value):
        h = self.head
        while 'next' in dir(h.next):
            h = h.next
        else:
            h.next = Node(new_value)

    def addNodeAfter(self, new_value, after__node):
            count = 1
            h = self.head
            while count != after__node:
                h = h.next
                count += 1
            move_after = h.next
            h.next = Node(new_value)
            h.next.next = move_after

    def addNodeBefore(self, new_value, before_node):
        if before_node == 1:
            self.head = Node(new_value, self.head)
        else:
            self.addNodeAfter(new_value, before_node - 1)

    def __str__(self):
        listvalues = "%s" % self.head
        h = self.head
        while 'next' in dir(h.next):
            listvalues += ", %s" % (h.next)
            h = h.next
        return listvalues

    def removeNode(self, node__to__remove):
        if node__to__remove > self.length():
            raise ValueError("The LinkedList has length %s" % self.length())
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

    def removeNodesByValue(self, value):
        h = self.head
        count = 1
        while count <= self.length():
            try:
                if h.value == value:
                    if h.next != h:
                        h = h.next
                        next
                    self.removeNode(count)
                else:
                    count += 1
                    h = h.next
            except:
                break

    def reverse(self):
        listvalues = "%s" % self.head
        h = self.head
        while 'next' in dir(h.next):
            listvalues += ", %s" % (h.next)
            h = h.next
        count = 1
        for i in listvalues.split(",")[ : :-1]:
            try:
                print "Before"
                print self
                self.addNodeBefore(i, count)
                self.removeNode(count + 1)
                print "After"
                print self
                count +=1
            except:
                break



ll = LinkedList(2)
ll.addNode(6)
ll.addNode(5)
ll.addNode(5)
ll.addNode(5)
ll.addNode(9)
ll.addNode(7)
ll.addNode(5)
ll.addNode(1)
ll.addNode(5)
ll.length()
ll.addNodeBefore(999, 1)
ll.addNodeBefore(999, 4)
print ll
ll.length()
ll.removeNode(10)
print ll
ll.removeNodesByValue2(999)
print ll
ll.removeNode(5)
print ll
ll.length()
