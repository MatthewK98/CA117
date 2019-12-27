class Triathlete:
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}

    def add_time(self, sport, sec):
        self.d[sport] = sec

    def total(self):
        return sum(self.d.values())

    def __eq__(self, other):
        return self.total() == other.total()

    def __gt__(self, other):
        return self.total() > other.total()

    def __lt__(self, other):
        return self.total() < other.total()

    def __str__(self):
        total = sum(self.d.values())
        return "Name: {}\nID: {}\nRace time: {}".format(self.name, self.tid, total)

class Triathlon(Triathlete):
    def __init__(self, d={}):
        self.d = d

    def add(self, athlete):
        self.d[athlete.name] = athlete

    def best(self):
        sorted_d = sorted((value, key) for (key, value) in self.d.items())
        return sorted_d[0][0]

    def worst(self):
        sorted_d = sorted((value, key) for (key, value) in self.d.items())
        return sorted_d[-1][0]

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()
