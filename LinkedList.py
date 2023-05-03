class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # create new Node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        add_node = Node(value)
        if self.head is None:
            self.head = add_node
            self.tail = add_node
        else:
            self.tail.next = add_node
            self.tail = add_node

        self.length += 1
        return True

    def pop_v1(self):
        if self.head is None:
            return False
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return True
        temp = self.head
        while temp is not None:
            if temp.next.next is None:
                self.tail = temp
                self.tail.next = None
                self.length -= 1
                return True
            temp = temp.next
        return False

    def pop(self):
        # if self.head is None:
        #    return None

        # Can check length as well
        if self.length == 0:
            return None

        if self.head is self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        pre = self.head
        temp = self.head

        while temp.next is not None:  # while (temp.next)
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length != 0:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def insert(self, index, value):
        # create new Node
        # insert Node
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


ll1 = LinkedList(1)
ll1.append(2)
ll1.append(3)

ll1.pop()
ll1.pop()
ll1.pop()

ll1.prepend(0)
ll1.print_list()
print(ll1.length)