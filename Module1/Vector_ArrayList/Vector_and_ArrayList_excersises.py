"""
In this python file we will review to different types of data structures:
ArrayList and Vector. A class will be modeled with both datastructures methods to
understand the underlying working mechanisms of each type.
"""

import threading


# Let's remember that an ArrayList is not synchronized, that means multiple threads can access and modify it
class ArrayList:
    # Initializing the instance with a max capacity at 10 as default,
    # as we know ArrayList have a set capacity when first created.
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity

    def __getitem__(self, index):
        # Checking if the index is outbounds and raising an error if it is
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        # Returning the item at the passed index
        return self.array[index]

    def __setitem__(self, index, value):
        # Checking if the index is outbounds and raising an error if it is
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        # Setting the new value of the item at the index passed
        self.array[index] = value

    def append(self, value):
        if self.size == self.capacity:
            # Accessing protected method
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def _resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def __len__(self):
        return self.size


# Let us remember that Vector are synchronized, only one thread at a time can access a vector
# meaning that they are thread safe because multiple access to it wil no occur.
class Vector:
    # Initializing the instance with a max capacity at 10 as default,
    # as we know ArrayList have a set capacity when first created.
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity
        self.lock = threading.Lock()

    def __getitem__(self, index):
        # Checking if the index is outbounds and raising an error if it is
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        # Returning the item at the passed index
        return self.array[index]

    def __setitem__(self, index, value):
        # Checking if the index is outbounds and raising an error if it is
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        # Setting the new value of the item at the index passed
        self.array[index] = value

    def append(self, value):
        if self.size == self.capacity:
            # Accessing protected method
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def _resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def __len__(self):
        return self.size


array = ArrayList()
for i in range(array.capacity):
    array.append(i+1)
    print(f"Array index {i}: {array[i]}")


vector = Vector()
for i in range(vector.capacity):
    vector.append(i+1)
    print(f"Vector index {i}: {vector[i]}")