def l2d(s):
    s = [i.strip() for i in s.readlines()]
    keys = s[0].split()
    values = s[1].split()
    return dict(zip(keys, values))

def main():
    d = l2d(sys.stdin)
    for (k, v) in sorted(d.items()):
        print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()
