class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def append(self, value):
        mynode = Node(value)

        if self.size == 0:
            self.first = mynode
        else:
            current = self.first
            while current.next is not None:
                current = current.next
            current.next = mynode

        self.size += 1
        return mynode

    # Exercise 1: Deleting a node from a linked list: Given a linked list and a value,
    # write a function to delete all nodes containing that value.
    def remove(self, value):
        if self.size == 0:
            return False
        else:
            current = self.first
            while current.next.value != value:
                if current.next is None:
                    return False
                else:
                    current = current.next
            deleted_node = current.next
            current.next = deleted_node.next

        self.size -= 1
        return deleted_node

    def __len__(self):
        return self.size

    def __str__(self):
        string = "["
        current = self.first
        while current is not None:
            string += str(current)
            string += str(" -> ")
            current = current.next
        string += "]"
        return string

    def reverse(self):
        prev = None
        current = self.first
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.first = prev


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
print(my_list)
my_list.remove(3)
print(my_list)
my_list.reverse()
print(my_list)