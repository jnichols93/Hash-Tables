# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0
        self.size = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # if capacity is full, resize
        if self.size == self.capacity:
            self.resize()
        # set the hashed key to a variable
        index = self._hash_mod(key)
        
        # if index, node = that index
        if self.storage[index]:
            node = self.storage[index]
        # while there is a next node and the node's key isn't the specified key, move to the next
            while node.next and node.key is not key:
                node = node.next
        # if the node's key is the specified key, set the node's value to specified value
            if node.key == key:
                node.value = value
        # if it the key doesn't exist, add a linked pair to the next node and increase count by 1
            else:
                node.next = LinkedPair( key, value)
                self.count += 1
        # otherwise add the linked pair to the indexed location and increase count by one
        else:
            self.storage[index] = LinkedPair( key, value )
            self.count += 1



    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        #hash the key
        index = self._hash_mod(key)

        #if there is no key, print error and return
        if not self.storage[index]:
            print("ERROR: No key found!")
            return
        
        #if there is, set that to variable node
        if self.storage[index]:
            node = self.storage[index]
        #if the node's key is the same as the specified key, if there's a next node, set index to that otherwise set it to none
            if node.key == key:
                if node.next:
                    self.storage[index] = node.next
                else:
                    self.storage[index] = None

        #while there is a next node, set variable of next_node to the following node
            while node.next:
                next_node = node.next
        # if the next_node's key is the specified key, do the same as above
                if next_node.key == key:
                    if next_node.next:
                        node.next = next_node.next
                    else:
                        node.next = None
                node = next_node

        self.count -= 1


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        #hash key
        index = self._hash_mod(key)

        # set node to the stored key
        if self.storage[index]:
            node = self.storage[index]
        #while the stored key isn't the specified key and there is another node to look at, move on
            while node.key != key and node.next:
                node = node.next
        # if the node's key is the specified key, return the value, otherwise return none
            if node.key == key:
                return node.value
            else:
                return None
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        #double capacity
        self.capacity = int(self.capacity * 2)
        #create new_storage and create a hashtable with current capacity
        new_storage = HashTable(self.capacity)

        #for each item in storage, add item.key and item.value to new_storage
        for item in self.storage:
            while item:
                new_storage.insert(item.key, item.value)
                item = item.next

        self.storage = new_storage.storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
