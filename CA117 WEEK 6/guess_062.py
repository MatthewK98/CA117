from random import randint

top = 1000000
bottom = 0
z = randint(bottom, top)

def guess(g):
    if g == z:
        return 0
    elif g < z:
        return -1
    else:
        return 1

def find():
    g = 5
    low = bottom
    high = top
    while low < high:
        mid = (low + high) // 2
        g = guess(mid)
        if g == 0:
            return mid
        if g == -1:
            low = mid + 1
        else:
            high = mid
    return low
'''
def find():
    while True:
        g = 0
        if guess(g) == 0:
            break
        elif guess(g) == -1:
            g += 1
        elif guess(g) == 1:
            g -= 1
    return g
'''
def main():
    a = find(0, 1000000)
    # a = find(0, 1000000)
    if a == z:
        print('Correct!')
    else:
        print('Incorrect!')
    print('You said {:d} and answer is {:d}'.format(a, z))

if __name__ == '__main__':
    main()
