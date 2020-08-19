class Node:
    def __init__(self, value="None", next_node=None):
        self.value = value
        self.next_node = next_node

    # def __repr(self):
    #     return

    def __str__(self):
        s = "("+str(self.value)+")"
        if self.next_node == None:
            s += "--|"
        else:
            s += "-->"
        return s

        # self.value

    def getItem(self): return self.value
    def getNext(self): return self.next_node

    def setItem(self, i):
        self.value = i

    def setNext(self, n):
        self.next_node = n


if __name__ == "__main__":
    n = Node()
    # print("Jeronimo", n.setItem("Jeronmi"))
    n1 = Node("jfeff")
    n2 = Node("Jonah")
    n3 = Node("broh")
    n1.setNext(n2)
    print(n1)
    print(n2)
    n2.setNext(n3)
    print(n2)


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


class Solution:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __str__(self):
        s = "head-->"
        curr = self.head
        for i in range(len(self.size)):
            s += "str(curr.get()"
            curr = curr.getNext()
        s += "<--tail"
        return s

    def push(self, value):
        self.size += 1
        self.storage.add_head(value)

    def printAll(self):
        # for i in range(len(self.storage)):
        if self.size == 0:
            print("It's empty")
        else:
            print("girl", self.storage)
            # for i in range(len(self.storage)):
            #     print("Something here")
            # print(self.storage[i])

    # def miminumIndex(self, list1, list2):
    #     print(list1)
    #     print(list2)
    #     for i in range(len(list1)):
    #         print()


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines",
         "Hungry Hunter Steakhouse", "Shogun"]

if __name__ == "__main__":

    s = Solution()
    s.push("Shogun")
    s.push("Piatti")
    # print(s)
    # print(s.printAll())
    # s.printAll()
# s.miminumIndex(list1, list2)
