# Your code here
import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y) #v = x^y
    v = math.factorial(v) #v = v * (v-1) * (v-2)  etc....
    v //= (x + y)  #v = v // (x + y)
    v %= 982451653

    return v

cache = {}   #how come cache has to be in the global scope in order for this to work???
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    

    cache_key = (x, y)

    if cache_key not in cache:
        cache[cache_key] = slowfun_too_slow(x, y)
    
    return cache[cache_key]

    




# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
