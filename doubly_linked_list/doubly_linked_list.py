

class ListNode:
    """
    Each ListNode holds a reference to its previous node
    as well as its next node in the List.
    """

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        """
        Wrap the given value in a ListNode and insert it
        after this node.

        Note that this node could already
        have a next node it is point to.
        """
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        """
        Wrap the given value in a ListNode and insert it
        before this node. 

        Note that this node could already
        have a previous node it is point to.
        """
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        """
        Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode.
        """
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.prev = self.next = None


class DoublyLinkedList:
    """
    Our doubly-linked list class. It holds references to
    the list's head and tail nodes.
    """

    def __init__(self, node=None):
        self.__head = node
        self.__tail = node
        self.__length = 1 if node is not None else 0

    @property
    def length(self):
        return self.__length

    def __len__(self):
        return self.__length

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value):
        raise SyntaxError(
            "To assign a value to the head, use the add_to_head() method")

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, value):
        raise SyntaxError(
            "To assign a value to the tail, use the add_to_tail() method")

    def add_to_head(self, value):
        """
        Wraps the given value in a ListNode and inserts it 
        as the new head of the list. Don't forget to handle 
        the old head node's previous pointer accordingly.
        """
        if self.__head is None:
            # If our list is empty, create the head (and tail!)
            self.__head = ListNode(value)
            self.__tail = self.__head
        else:
            # Use the LinkNode method to create
            # a new previous node, and set the head
            self.__head.insert_before(value)
            self.__head = self.__head.prev
        self.__length += 1

    def remove_from_head(self):
        """
        Removes the List's current head node, making the
        current head's next node the new head of the List.

        Returns the value of the removed Node.
        """
        if self.__head is None:
            # If we don't have a head, remove nothing
            return None

        old_head = self.__head
        if self.__length == 1:
            # If our head and tail are the same,
            # Simply reset the head and tail
            self.__head = self.__tail = None
        else:
            # Otherwise, set the head's next
            # as our new head, and remove the old
            self.__head = old_head.next
            old_head.delete()

        self.__length -= 1
        return old_head.value

    def add_to_tail(self, value):
        """
        Wraps the given value in a ListNode and inserts it 
        as the new tail of the list. 

        Don't forget to handle 
        the old tail node's next pointer accordingly.
        """
        if self.__tail is None:
            # If our list is empty, create the head (and tail!)
            self.__head = ListNode(value)
            self.__tail = self.__head
        else:
            # Use the LinkNode method to create
            # a new previous node, and set the head
            self.__tail.insert_after(value)
            self.__tail = self.__tail.next
        self.__length += 1

    def remove_from_tail(self):
        """
        Removes the List's current tail node, making the 
        current tail's previous node the new tail of the List.

        Returns the value of the removed Node.
        """
        if self.__tail is None:
            # If we don't have a tail, remove nothing
            return None

        old_tail = self.__tail
        if self.__length == 1:
            # If our head and tail are the same,
            # Simply reset the head and tail
            self.__head = self.__tail = None
        else:
            # If we have a tail, set the tail's prev
            # as our new tail, and remove the old
            old_tail = self.__tail
            self.__tail = old_tail.prev
            old_tail.delete()
        
        self.__length -= 1
        return old_tail.value

    def move_to_front(self, node):
        """
        Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List.
        """
        if self.__length == 0 or self.__length == 1 or self.__head == node:
            # If:
            #  - Our list is empty
            #  - Our list only has one item
            #  - The head is the node we wish to move
            # do nothing
            return

        if self.__tail == node:
            # If the node we're moving to the end is the tail,
            # set the node's prev as the new tail
            self.__tail = node.prev

        # Delete the node to update the prev and next around it,
        node.delete()
        # and then add the node to the head of the list
        node.next = self.__head
        self.__head.prev = node
        self.__head = node

    def move_to_end(self, node):
        """
        Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List.
        """
        if self.__length == 0 or self.__length == 1 or self.__tail == node:
            # If:
            #  - Our list is empty
            #  - Our list only has one item
            #  - The tail is the node we wish to move
            # do nothing
            return

        if self.__head == node:
            # If the node we're moving to the end is the head,
            # set the node's next as the new head
            self.__head = node.next

        # Delete the node to update the prev and next around it,
        node.delete()
        # and then add the node to the tail of the list
        node.prev = self.__tail
        self.__tail.next = node
        self.__tail = node

    def delete(self, node):
        """
        Removes a node from the list and handles cases where
        the node was the head or the tail
        """
        if self.length == 0:
            # Our list is empty? Do nothing
            return

        if self.__head == node:
            # If we're deleting the head, set the next node as our head
            self.__head = node.next
        if self.__tail == node:
            # If we're deleting the tail, set the prev node as our tail
            self.__tail = node.prev
        # After
        node.delete()
        self.__length -= 1

    def get_max(self):
        """
        Returns the highest value currently in the list
        """
        if self.__length < 1:
            # If we have no nodes, return None
            return None

        # Set our initial node and max value
        check_node = self.__head
        max_val = check_node.value

        while check_node.next is not None:
            # As long as we have another node to check,
            # Check which value is higher
            check_node = check_node.next
            if max_val < check_node.value:
                max_val = check_node.value

        return max_val
