import time
import tracemalloc

## modules
import lcg
import mersenne
import fortuna
import bitstream


def runner(function_name):
    tracemalloc.start()
    t1 = time.perf_counter()
    
    if function_name == "mersenne":
        x = mersenne.pyrand()
    elif function_name == "lcg":
        x = lcg.random_numbers()
    elif function_name == "fortuna":
        x = fortuna.fortuna()

    t2 = time.perf_counter()
    print("\n>>> %s <<<\ntime: %f ms\nmemory: %d bytes" % (function_name,((t2-t1)*1000), tracemalloc.get_traced_memory()[1]))
    tracemalloc.stop()

    bitstream.inp(x, function_name+".txt")


for i in range(0,256):
    print(i)

runner("mersenne")
runner("lcg")
runner("fortuna")

inp = open("raw/raw_randomorg.txt", "r").read().split()
bitstream = ''

for i in inp:
	bitstream += bin(int(i))[2:].zfill(8)


with open('bit/bit_randomorg.txt', 'w') as f:
    f.write(bitstream)




# ## python random
# tracemalloc.start()
# t1 = time.perf_counter()
# x = mersenne.pyrand(0,255,100000)
# t2 = time.perf_counter()
# print("Python Random\ntime: %f ms\nmemory: %d bytes" % (((t2-t1)*1000), tracemalloc.get_traced_memory()[1]))
# tracemalloc.stop()
# # print(x)
# bitstream.inp(x)


# ## fortuna
# tracemalloc.start()
# t1 = time.perf_counter()
# x = fortuna.fortuna(0,255,100000)
# t2 = time.perf_counter()
# print("Fortuna\ntime: %f ms\nmemory: %d bytes" % (((t2-t1)*1000), tracemalloc.get_traced_memory()[1]))
# tracemalloc.stop()
# # print(x)


# ## lcg
# tracemalloc.start()
# t1 = time.perf_counter()
# x = lcg.random_numbers()
# t2 = time.perf_counter()
# print("Linear Congruential\ntime: %f ms\nmemory: %d bytes" % (((t2-t1)*1000), tracemalloc.get_traced_memory()[1]))
# tracemalloc.stop()
# # print(x)