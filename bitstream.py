def inp(x, name='bits.txt'):
    bitstream = ''
    norm = ''
    sum = 0
    for i in x:
        bitstream += bin(int(i))[2:].zfill(8)
        norm += str(i) + '\n'
        sum += int(i)

    with open("bit/bit_"+name, 'w') as f:
        f.write(bitstream)
    
    with open("raw/raw_"+name, 'w') as f:
        f.write(norm)

    print("average:",sum/len(x))