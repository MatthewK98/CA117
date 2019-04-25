class Score:
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def total(self):
        return self.goals * 3 + self.points

    def less_than(self, s2):
        return self.total() < s2.total()

    def greater_than(self, s2):
        return self.total() > s2.total()

    def equal_to(self, s2):
        return self.total() == s2.total()

    # def less_than(self, s2):
    #     return (self.points + self.goals * 3) < (s2.points + s2.goals * 3)

    # def greater_than(self, s2):
    #     return (self.points + self.goals * 3) > (s2.points + s2.goals * 3)

    # def equal_to(self, s2):
    #     return (self.points + self.goals * 3) == (s2.points + s2.goals * 3)

def main():

    score1 = Score()
    score2 = Score(3, 9)
    score3 = Score(4, 6)

    print(score1.less_than(score2))
    print(score3.less_than(score1))
    print(score1.greater_than(score2))
    print(score3.greater_than(score2))
    print(score1.greater_than(score1))
    print(score2.greater_than(score1))
    print(score2.equal_to(score1))
    print(score3.equal_to(score2))

if __name__ == '__main__':
    main()
