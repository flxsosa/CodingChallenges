'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named
both, which is an XOR of the next node and the previous node.

Implement an XOR linked list; it has an add(element) which adds the element to
 the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer
functions that converts between nodes and memory addresses.
'''

class XORList:
    def __init__(self, h,t=None):
        self.both = h,t

    def add(self,element):
        if self.both[1] == None:
            tail = XORList(element)
            self.both = self.both[0], tail
        else:
            self.both[1].add(element)

    def get(self, index):
        if index == 0:
            return self.both[0]
        else:
            return self.both[1].get(index-1)

head = XORList(1)
head.add(2)
print(head.get(4))
