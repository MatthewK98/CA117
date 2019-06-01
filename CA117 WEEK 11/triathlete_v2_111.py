class Triathlete:
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}

    def add_time(self, sport, sec):
        self.d[sport] = sec

    def get_time(self, sport):
        return self.d[sport]

    def __str__(self):
        total = sum(self.d.values())
        return "Name: {}\nID: {}\nRace time: {}".format(self.name, self.tid, total)

def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)

if __name__ == '__main__':
    main()
