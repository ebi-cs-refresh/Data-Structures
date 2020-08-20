"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.

*Question: What's the difference between the delete in  118and119 and 138
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next  # self.prev.nex  is current
        if self.next:
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        newnode = ListNode(value, None, None)

        self.length += 1
        if not self.head and not self.tail:
            self.head = newnode
            self.tail = newnode

        newnode.next = self.head
        # the old node with the head pointer didn't have a previous pointer, so we're defining that
        self.head.prev = newnode
        # new  head to deal with
        self.head = newnode

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if not self.head:
            return None
        value = self.head.value  # save the head value before deleting
        # if self.head is None and self.tail is None:
        #     return None
        self.delete(self.head)
        return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        newnode = ListNode(value)
        self.length += 1

        if not self.tail and not self.head:
            self.tail = newnode
            self.head = newnode
        else:
            newnode.prev = self.tail
            # we're doing this again, but from the perspective of the tail
            self.tail.next = newnode
            self.tail = newnode

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.tail == 0:
            return None
        current = self.tail.value
        self.delete(self.tail)
        return current

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):

        if node is self.head:
            return
        currentNode = node.value
        if currentNode is self.tail:
            self.remove_from_tail()
        else:
            # self.delete(node)
            node.delete()
            self.length -= 1

        # once we remove the target node
        self.add_to_head(currentNode)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return
        currentNode = node.value
        if currentNode is self.head:
            self.remove_from_head()
        else:
            # node.delete()
            # self.length -= 1
            self.delete(node)

        # once we remove the target node
        self.add_to_tail(currentNode)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail is None:
            return

        # if only node
        if self.head is self.tail:
            self.head = None
            self.tail = None

        # if node is in the head
        currentnode = node
        if currentnode is self.head:
            # move pointer to the next node
            self.head = currentnode.next

            # delete node
            node.delete()
        if currentnode is self.tail:
            self.tail = currentnode.prev
            currentnode.delete()
        else:
            currentnode.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):

        if self.head is None:
            return None
        currentNode = self.head
        max_val = self.head.value

        while currentNode:
            if currentNode.value > max_val:
                # reassign val to the head
                max_val = currentNode.value
            # move pointer to the next node
            currentNode = currentNode.next
        return max_val
