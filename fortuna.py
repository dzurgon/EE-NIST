import Fortuna

def fortuna(count=1250000,start=0,end=255):
    return [Fortuna.random_int(start,end) for _ in range(count)]
