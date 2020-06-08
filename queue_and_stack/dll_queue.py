import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.__size = 0
        # Why is our DLL a good choice to store our elements?
        self.__storage = DoublyLinkedList()

    def enqueue(self, value):
        self.__size += 1
        self.__storage.add_to_tail(value)

    def dequeue(self):
        if self.__size > 0:
            # If there's something in the queue, 
            # Decrease size and return the value
            self.__size -= 1
            return self.__storage.remove_from_head()

    def len(self):
        return self.__size

    def __len__(self):
        return self.__size
