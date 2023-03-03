import math

r = 24
for i in range(r*r*4+r*4+1):
    if math.sqrt(((i%(r*2+1))-r)**2+((i//(r*2+1))-r)**2) <= r:
        print('O', end='')
    else:
        print(' ', end='')
    if (i%(r*2+1))-r == r:
        print('\n', end='')
