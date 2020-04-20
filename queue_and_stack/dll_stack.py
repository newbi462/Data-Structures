import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        #pass
        return self.storage.add_to_head(value)

    def pop(self):
        #pass
        if self.len() > 0:
            return self.storage.remove_from_head()
        else:
            pass

    def len(self):
        #pass
        return self.storage.length

"""
test = Stack()
test.push(300)
test.push(400)
print(test.pop())

"""
