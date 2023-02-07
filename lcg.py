def random_number(start, end, c, m, seed):
    a = 1103515245
    while True:
        seed = (a * seed + c) % m
        if start <= seed <= end:
            return seed

def random_numbers(count=1250000, start=0, end=255, c=12345, m=2**13, seed=1):
    return [random_number(start, end, c, m, seed + i) for i in range(count)]
