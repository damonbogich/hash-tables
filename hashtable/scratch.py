### EX 1:

# #fibonacci -- memoization (caching)


# cache = {}

# def fib(n):
#     if n <= 1:
#         return n
    
#     if n not in cache:
#         cache[n] = fib(n - 1) + fib(n - 2)

#     return cache[n]

# for i in range(100):
#     print(f"{i}: {fib(i)}")





# ### EX 2:
# #sort dictionary values:

# d = {
#     'foo': 12,
#     'bar': 17,
#     'qux': 2
# }

# #sorts by key, then value (if keys are the same):
# i = list(d.items())

# i.sort()

# print(i)

# # def comp(e):
# #     return e[1]

# # i.sort(key = comp)

# #same as the function above
# #comparing the 2nd tuple value 
# i.sort(key=lambda e:e[1])
# print(i)



##### EX 3:

#Loopkup table

import math
"""
Build a lookup table for the inverse square root for numbers 1 - 1000.
"""

# inv_sqrt_table = {}

# def inv_sqrt(n):
#     return 1 / math.sqrt(n)

# def build_lookup_table():
#     for i in range(1, 1001):
#         inv_sqrt_table[i] = inv_sqrt(i)

# build_lookup_table()

# print(inv_sqrt_table[10])
# print(inv_sqrt_table[37])




### EX 4:
#count the number of occurences of a letter in a string

def letter_count(s):
    d = {}

    for c in s:
        if c.isspace():
            continue
        
        c = c.upper()
        
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
        
    return d

print(letter_count('Hello there!'))