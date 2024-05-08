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

    def remove(self, value):
        if self.size == 0:
            return False
        else:
            current = self.first
            while current.next:
                if current.next.value == value:
                    deleted_node = current.next
                    current.next = deleted_node.next
                    self.size -= 1
                    return deleted_node
                current = current.next
            return False

    def __len__(self):
        return self.size

    def __str__(self):
        string = "["
        current = self.first
        while current is not None:
            string += str(current)
            if current.next:
                string += " -> "
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

    def is_palindrome(self):
        if not self.first:
            return True

        # Find the middle of the linked list
        slow = fast = self.first
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Compare the first half with the reversed second half
        first_half = self.first
        second_half = prev
        while second_half:
            if first_half.value != second_half.value:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True



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
