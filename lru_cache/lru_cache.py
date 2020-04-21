from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        #pass
        self.cache = DoublyLinkedList()
        self.limit = limit
        self.storage = {} #Hint: Since our cache is going to be storing key-value pairs, we might want to use a structure that is adept at handling those.

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        pass

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #pass
        if key in self.storage:  # if move to head as recent
            node = self.storage[key]
            node.value = (key, value)
            self.cache.move_to_front(node)
        else:
            if self.limit == self.cache.length: #max
                self.storage.pop(self.cache.tail.value[0])
                self.cache.remove_from_tail() # LRU

            # add new
            self.cache.add_to_head( (key, value) )
            self.storage[key] = self.cache.head

        print(self.storage)



"""
When used move to add_to_head

when full remove tail

based on Readme hint and need for key value sets use a {} for the sets/storage
"""
