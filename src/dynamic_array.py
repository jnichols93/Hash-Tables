class DynamicArray:
    #my_array = [4]
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity
    
    def insert(self, index, value):
        # make sure we have open space
        if self.count >= self.capacity:
            # TODO: make array dynamically resize
            print("ERROR: Array is full")
            return
        # make sure the index is in range
        if index >= self.count:
            print("Error: Index out of range")
            return
        # if so shift everything right
        # start with the last one, move it to the right
        for i in range(self.count, index, -1)
        self.storage[i] = self.storage[i-1]
        # insert our value
        self.storage[index] = value
        self.count += 1 