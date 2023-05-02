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

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        # create new Node
        # insert Node
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


ll1 = LinkedList(5)
ll1.append(10)
ll1.append(20)
ll1.append(30)
ll1.print_list()
print(ll1.length)