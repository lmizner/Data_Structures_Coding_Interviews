class HashEntry:
    def __init__(self, key, data):
        # key of the entry
        self.key = key
        # data to be stored
        self.value = data
        # reference to new entry
        self.nxt = None

    def __str__(self):
        return str(self.key) + ", " + self.value


#####################################################################


class HashTable:
    # Constructor
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket = [None] * self.slots
        self.threshold = 0.6

    # Helper Functions
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    # Hash Function
    def get_index(self, key):
        # hash is a built in function in Python
        hash_code = hash(key)
        index = hash_code % self.slots
        return index

    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots
        # rehash all items into new slots
        for item in self.bucket:
            head = item
            while head is not None:
                new_index = hash(head.key) % new_slots
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key is head.key:
                            node.value = head.value
                            node = None
                        elif node.nxt is None:
                            node.nxt = HashEntry(head.key, head.value)
                            node = None
                        else:
                            node = node.nxt
                head = head.nxt
        self.bucket = new_bucket
        self.slots = new_slots

    def insert(self, key, value):
        # Find the node with the given key
        b_index = self.get_index(key)
        if self.bucket[b_index] is None:
            self.bucket[b_index] = HashEntry(key, value)
            print(key, "-", value, "inserted at index:", b_index)
            self.size += 1
        else:
            head = self.bucket[b_index]
            while head is not None:
                if head.key == key:
                    head.value = value
                    break
                elif head.nxt is None:
                    head.nxt = HashEntry(key, value)
                    print(key, "-", value, "inserted at index:", b_index)
                    self.size += 1
                    break
                head = head.nxt

        load_factor = float(self.size) / float(self.slots)
        # Checks if 60% of the entries in table are filled, threshold = 0.6
        if load_factor >= self.threshold:
            self.resize()
        
    # Return a value for a given key
    def search(self, key):
        # Find the node with the given key
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        # Search key in the slots
        while head is not None:
            if head.key == key:
                return head.value
            head = head.nxt
        # If key not found
        return None

    # Remove a value based on a key
    def delete(self, key):
        # Find index
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        # If key exists at first slot
        if head.key == key:
            self.bucket[b_index] = head.nxt
            print(key, "-", head.value, "deleted")
            # Decrease the size by one
            self.size -= 1
            return self
        # Find the key in slots
        prev = None
        while head is not None:
            # If key exists
            if head.key == key:
                prev.nxt = head.nxt
                print(key, "-", head.value, "deleted")
                # Decrease the size by one
                self.size -= 1
                return
            # Else keep moving in chain
            prev = head
            head = head.nxt

        # If key does not exist
        print("Key not found")
        return



# Time Complexity = O(1)
# Space Complexity = O(n)



#####################################################################



ht = HashTable()
ht.insert(2, "London")
ht.insert(7, "Paris")
ht.insert(8, "Cairo")
print("size:", ht.get_size())
ht.delete(2)
print("size:", ht.get_size())
ht.search(2)



table = HashTable()  # Create a HashTable
print(table.is_empty())
table.insert("This", 1)
table.insert("is", 2)
table.insert("a", 3)
table.insert("Test", 4)
table.insert("Driver", 5)
print("Table Size: " + str(table.get_size()))
print("The value for 'is' key: " + str(table.search("is")))
table.delete("is")
table.delete("a")
print("Table Size: " + str(table.get_size()))
