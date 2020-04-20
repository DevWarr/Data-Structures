import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.__size = 0
        # Why is our DLL a good choice to store our elements?
        self.__storage = DoublyLinkedList()

    def push(self, value):
        self.__size += 1
        self.__storage.add_to_head(value)

    def pop(self):
        if self.__size > 0:
            self.__size -= 1
            return self.__storage.remove_from_head()

    def len(self):
        return self.__size
