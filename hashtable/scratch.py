table = [None] * 8


def hashf(s):
    b = s.encode()

    total = 0
    for i in b:
        total += i

    return total


def get_index(key):
    index_value = hashf(key)
    index_value %= len(table)

    return index_value

def put(key, value):
    #which slot in table is the value going?
    index = get_index(key)
    #store value at that spot
    table[index] = value

def get(key):
    index = get_index(key)

    return table[index]

def delete(key):
    index = get_index(key)

    table[index] = None
    



#GET with collisions:
    #Get the index for the key
    #Search the LL at that index for the entry for that key
    #Return the value (or None if not found)

#PUT WITH COLLISIONS:
    #Get the index for the key
    #Search the list for the key
    #if it already exists, overwrite the value
    #Else, insert the [key, value] at the head of the LL if not

