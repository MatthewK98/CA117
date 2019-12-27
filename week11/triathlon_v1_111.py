class Triathlete:
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return "Name: {}\nID: {}".format(self.name, self.tid)

class Triathlon(Triathlete):
    def __init__(self, d={}):
        self.d = d

    def add(self, athlete):
        self.d[athlete.tid] = athlete

    def remove(self, key):
        del self.d[key]

    def lookup(self, key):
        return self.d.get(key)

def main():
    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    tn.add(t1)
    tn.add(t2)

    t = tn.lookup(21)
    assert(isinstance(t, Triathlete))
    assert(t.name == 'Ian Brown')
    assert(t.tid == 21)

    tn.remove(21)
    t = tn.lookup(21)
    assert(t is None)

if __name__ == '__main__':
    main()
