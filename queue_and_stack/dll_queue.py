import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # AWNSER: This would never be the right size, by natuer a que is more a liked list where you are always changing the site in relation to the next nodethis would
        # self.storage = ?
        self.storage = DoublyLinkedList()
        # ????? Why? storage =?

    def enqueue(self, value):
        #pass
        return self.storage.add_to_head(value)
        # DoublyLinkedList(self, value) != storage

    def dequeue(self):
        #pass
        return self.storage.remove_from_tail()
        # ??? why does this not need (self)

    def len(self):
        #print(self.size)
        #return self.size
        return self.storage.length



test = Queue()
test.enqueue(5)
test.enqueue(3)
print(test.len())
print(test.dequeue())
print(test.len())
print(test.dequeue())
print(test.len())

print(test.dequeue())
print(test.len())

"""
I need to better understand what "storage" is
*is "storage" == "fopbar", or a reserver, or standard value like index or prams?

"""
