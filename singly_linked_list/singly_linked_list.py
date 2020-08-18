class Node:
    def __init__(self, value="None", next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None  # beginning of a node, stores a node
        self.tail = None  # aend of a node in the list

    def add_head(self, value):  # append
        new_node = Node(value)
        # if its empty
        # head and tail point to the same node
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new node should point to current head
            new_node.next_node = self.head
            # moved head to new node
            self.head = new_node

    def add_tail(self, value):
        new_node = Node(value)
        # if its empty
        # head and tail point to the same node
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # we have to manipulate the tail
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next_node is None:  # if it has one element set head and tail to none
            head_val = self.head.value
            self.head = None
            self.tail = None
            return head_val

        # update head to the right node
        head_val = self.head.value
        self.head = self.head.next_node
        return head_val

    def contains(self, value):
        # see if element exists
        if self.head is None:
            print("Empty")
            return False
        else:
            # loop through eachnode, until we see the value or we cant go further
            current_node = self.head
            while current_node is not None:
                # CHECK if this is the node we are looking for
                if current_node.value == value:
                    return True

                # otherwise, go to the next node
                print(current_node.value, end="->")
                current_node = current_node.next_node
            print("None")
            return False  # we do not have anything in here


ll = LinkedList()
ll.add_head(0)
ll.add_tail(1)
ll.add_tail(2)
ll.remove_head()

print(ll.contains(0))
