class Node(object):

    def __init__(self, item):
        """
        construct new node, with given item.
        next initially set to None.
        """
        self.item = item
        self.next = None

    def __str__(self):
        """return a string representation of the node"""
        s = "("+str(self.item)+")"
        if self.next == None:
            s += "--|"
        else:
            s += "-->"
        return s

    def getItem(self): return self.item
    def getNext(self): return self.next

    def setItem(self, i):
        """set node item to i"""
        self.item = i

    def setNext(self, n):
        """set node next to n"""
        self.next = n


if __name__ == "__main__":

    n1 = Node("jeff")
    n2 = Node("zach")
    n3 = Node("lauri")
    n4 = Node("rich")

    n1.setNext(n2)
    print(n1)
    n2.setNext(n3)
    print(n2)
    n3.setNext(n4)


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        s = "head-->"
        curr = self.head
        for i in range(self.size):
            s += "(%s)" % str(curr.getItem())
            curr = curr.getNext()
        s += "<--tail"
        return s

    def append(self, item):
        n = Node(item)
        if self.size == 0:
            self.head = n
        else:
            self.tail.setNext(n)
        self.tail = n
        self.size += 1


LL = LinkedList()
LL.append("A")
print(LL.tail)
# assert len(LL) == 0
# assert str(LL) == "head--><--tail"
# LL.append("A")
# LL.append("B")
# LL.append("C")
# assert len(LL) == 3
# assert str(LL) == "head-->(A)(B)(C)<--tail"
