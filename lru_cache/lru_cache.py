import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache:

    def __init__(self, limit=10):
        """
        Our LRUCache class keeps track of:
            -   the max number of nodes it can hold
            -   a doubly-linked list that holds the key-value entries in the correct order
            -   a storage dict that provides fast access to every node stored in the cache.
        """
        self.__max = limit
        self.__storage = DoublyLinkedList()
        self.__accessor = {}

    def get(self, key):
        """
        Retrieves the value associated with the given key.

        Also moves the key-value pair to the end of the order
        such that the pair is considered most-recently used.

        Returns 
            -   value associated with the key
            -   None if the key-value pair doesn't exist
        """
        node = self.__accessor.get(key, None)

        if node is None:
            # If there's no node associated with our key,
            # return None
            return None
        else:
            # Move the node to the head, and return the value
            self.__storage.move_to_front(node)
            return node.value

    def set(self, key, value):
        """
        Adds the given key-value pair to the cache.
        The newly- added pair should be considered the most-recently used
        entry in the cache.

        If the cache is already at max capacity
        before this entry is added, then the oldest
        entry in the cache needs to be removed to make room. 

        Additionally, in the case that the key already
        exists in the cache, we simply want to overwrite
        the old value associated with the key with
        the newly-specified value.
        """
        node = self.__accessor.get(key, None)
        if node is not None:
            # if there's already a node associated with
            # this key, simply overwrite the value
            node.value = value
        else:
            if len(self.__storage) >= self.__max:
                # If we hit our max, we must remove an item!
                node_to_remove = self.__storage.tail

                for k, node in self.__accessor.items():
                    # Loop through our dictionary values
                    # To find the node we wish to remove.
                    # Once found, pop it from the dictionary
                    # and leave the loop
                    if node == node_to_remove:
                        self.__accessor.pop(k)
                        break
                # Remove from linkedlist
                self.__storage.remove_from_tail()
            
            # Add new value to the head of our storage,
            # And add it to our accessor dictionary
            self.__storage.add_to_head(value)
            self.__accessor[key] = self.__storage.head
