class Triathlete:
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}

    def __str__(self):
        return "Name: {}\nID: {}".format(self.name, self.tid)

class Triathlon:
    def __init__(self, d={}):
        self.d = {}

    def add(self, athlete):
        self.d[athlete.name] = athlete

    def __str__(self):
        output = ""
        for (k, v) in sorted(self.d.items()):
            output += str(v) + "\n"
        return output.strip()

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn)

if __name__ == '__main__':
    main()
