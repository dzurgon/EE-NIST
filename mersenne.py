import random

def pyrand(count=1250000,start=0,end=255):
    return [random.randint(start,end) for _ in range(count)]
