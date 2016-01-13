__author__ = 'Kyle DeRosa'

'''
A linked list is a linear data structure where each element is a separate object.
Each element (we will call it a node) of a list is comprising of two items -
    the data and
    a reference to the next node.
The last node has a reference to null.
'''


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    # empty linked list
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def length(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.get_next()
        return count

    def find(self, data):
        curr = self.head
        found = False
        while curr and not found:
            if curr.get_data() == data:
                found = True
            else:
                curr = curr.get_next()
        if curr is None:
            raise ValueError(str(data) + " not found in the linked list")

    def delete(self, data):
        curr = self.head
        previous = None
        found = False
        while curr and not found:
            if curr.get_data() == data:
                found = True
            else:
                previous = curr
                curr = curr.get_next()
        if curr is None:
            raise ValueError(str(data) + " not found in the linked list")
        if previous is None:
            self.head = curr.get_next()
        else:
            previous.set_next(curr.get_next())

# Big O test
# insert (1); insert into head of list
# insert (n); traverse list and insert at end
# delete (worst case, n); traverse list and remove final element
# search (worst case, n); traverse list and find at final element
# sorted search (worst case, n); still must traverse entire list,
#                               unless indexed O(logn) binary search
# sort (n^2),  insertion or selection sort, unless indexed
# sort (n lg n), if indexed, merge sort
