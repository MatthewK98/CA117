import sys
def sumfac(d):
    total = 0
    a = int(d ** 0.5)
    for i in range(1, a + 1):
        if d % i == 0:
            total += i
            if i != d / i:
                total += d / i
    return total - d

def isPerfect(d):
    if d == sumfac(d):
        return True
    else:
        return False
def main():
    d = sys.stdin
    for i in d:
        i = i.strip()
        if i.isnumeric():
            print(isPerfect(int(i)))
if __name__ == '__main__':
    main()
