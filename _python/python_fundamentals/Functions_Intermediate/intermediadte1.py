# #1
import random

def random_integer(start=0, end=100):
    return random.randint(start, end)

print(random_integer())


# #2
import random

def random_integer(start=None, end=None):
    if start is None and end is None:
        return random.randint(0, 100)
    elif end is None:
        return random.randint(0, start)
    else:
        return random.randint(start, end)

print(random_integer(50)) 


# #3
import random

def random_integer(start=None, end=None):
    if start is None and end is None:
        return random.randint(0, 100)
    elif end is None:
        return random.randint(0, start)
    else:
        return random.randint(start, end)

print(random_integer(50))


#4
import random

def random_integer(start=None, end=None):
    if start is None and end is None:
        return random.randint(0, 100)
    elif end is None:
        return random.randint(0, start)
    else:
        return random.randint(start, end)

print(random_integer(30, 50)) 
