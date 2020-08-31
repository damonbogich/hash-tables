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
    

