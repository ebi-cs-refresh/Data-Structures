class Node:
    def __init__(self, value="None", next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None  # beginning of a node, stores a node
        self.tail = None  # aend of a node in the list

    # def __repr__(self):
    #     return str(self.head.value)

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


"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?


Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.append(value)
#         print(self.storage)
#         # return self.storage

#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         self.size -= 1
#         return self.storage.pop(0)


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __repr__(self):
        return str(self.storage)

    def __len__(self):
        return self.size

    def enqueue(self, value):  # we are adding to the tail
        self.size += 1
        print(self.storage)
        return self.storage.add_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        print(self.storage)
        return self.storage.remove_head()


if __name__ == '__main__':

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
#     # print(q.)
