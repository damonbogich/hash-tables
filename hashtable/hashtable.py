class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = MIN_CAPACITY
        
        self.table = [None] * self.capacity

        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.capacity/self.count

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #make it a hashtable entry:
        entry = HashTableEntry(key, value)
        #Get the index for the key
        index = self.hash_index(key)
        #Search the list for the key
        current = self.table[index]
        #if it already exists, overwrite the value
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        #Else, insert the [key, value] at the head of the LL if not
        current_head = self.table[index]
        
        self.table[index] = entry
        self.table[index].next = current_head
        self.count += 1

        if self.get_load_factor() > .7:
            new_capacity = self.capacity * 2

            self.resize(new_capacity)


        
        



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        #TODO: how could the key not be found? -- just for collisions?
        index = self.hash_index(key)
        #check the table for the key, if it matches, remove that value from given key
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = None
                self.count -= 1
                if self.capacity > 8:
                    if self.get_load_factor() < .2:
                        new_capacity = self.capacity / 2
                        self.resize(new_capacity)

                return
            current = current.next
        print('Warning, key not found')
        



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #Get the index for the key
        index = self.hash_index(key)
        #Search the LL at that index for the entry for that key
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None
        #Return the value (or None if not found)


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        previous_table = self.table

        # new_capacity = self.capacity * 2

        self.table = [None for i in range(new_capacity)]

        for entry in previous_table:
            if entry is not None:
                current = entry
                while current is not None:
                    self.put(current.key, current.value)
                    current = current.next







##### Monday:::


# class HashTableEntry:
#     """
#     Linked List hash table key/value pair
#     """
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None


# # Hash table can't have fewer than this many slots
# MIN_CAPACITY = 8


# class HashTable:
#     """
#     A hash table that with `capacity` buckets
#     that accepts string keys

#     Implement this.
#     """

#     def __init__(self, capacity):
#         self.capacity = MIN_CAPACITY
        
#         self.table = [None] * self.capacity


#     def get_num_slots(self):
#         """
#         Return the length of the list you're using to hold the hash
#         table data. (Not the number of items stored in the hash table,
#         but the number of slots in the main list.)

#         One of the tests relies on this.

#         Implement this.
#         """
        
#         return len(self.table)


#     def get_load_factor(self):
#         """
#         Return the load factor for this hash table.

#         Implement this.
#         """
#         # Your code here


#     def fnv1(self, key):
#         """
#         FNV-1 Hash, 64-bit

#         Implement this, and/or DJB2.
#         """

#         # Your code here


#     def djb2(self, key):
#         """
#         DJB2 hash, 32-bit

#         Implement this, and/or FNV-1.
#         """
        
#         hash = 5381
#         for c in key:
#             hash = (hash * 33) + ord(c)
#         return hash


#     def hash_index(self, key):
#         """
#         Take an arbitrary key and return a valid integer index
#         between within the storage capacity of the hash table.
#         """
#         #return self.fnv1(key) % self.capacity
#         return self.djb2(key) % self.capacity

#     def put(self, key, value):
#         """
#         Store the value with the given key.

#         Hash collisions should be handled with Linked List Chaining.

#         Implement this.
#         """
#         #find index where you put value:
#         index = self.hash_index(key)

#         #put value there
#         self.table[index] = value



#     def delete(self, key):
#         """
#         Remove the value stored with the given key.

#         Print a warning if the key is not found.

#         Implement this.
#         """
#         # Your code here
#         #TODO: how could the key not be found? -- just for collisions?
#         index = self.hash_index(key)

#         self.table[index] = None


#     def get(self, key):
#         """
#         Retrieve the value stored with the given key.

#         Returns None if the key is not found.

#         Implement this.
#         """
#         # Your code here
#         index = self.hash_index(key)

#         return self.table[index]


#     def resize(self, new_capacity):
#         """
#         Changes the capacity of the hash table and
#         rehashes all key/value pairs.

#         Implement this.
#         """
#         # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
