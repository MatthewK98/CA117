class Score:
    def __init__(self,goals=0,points=0):
        self.goals = goals
        self.points = points
        
    def total(self):
        return self.goals * 3 + self.points 
    
    def __str__(self):
        return "{} goals(s) and {} point(s)".format(self.goals,self.points) 
        
    def __gt__(self,other):
        return self.total() > other.total()
        
    def __mul__(self,number):
        g = self.goals * number
        p = self.points * number
        return Score(g,p)
        
    def  __rmul__(self,number):
       return  self * number
    
    def __imul__(self,number):
        self.goals = self.goals * number
        self.points = self.points
        return self
       
def main():

    # Create some instances of Score
    s1 = Score()
    s2 = Score(3, 12)
    s3 = Score(4, 9)
    s4 = Score(2, 11)
    s5 = Score(1, 1)

    # Display
    print('Display...')
    print(s1)
    print(s2)
    print(s3)
    print(s4)

    # Multiplication
    print('Multiplication...')
    s2 = s2 * 2
    print(s2)
    print(s2 > s3)

    # Right multiplication
    print('Right multiplication...')
    s2 = 2 * s2
    print(s2)
    print(s2 > s3)

    # In-place multiplication
    print('In-place multiplication...')
    s2alias = s2
    s2 *= 2
    print(s2)
    print(s2alias)
    print(s2 == s2alias)

if __name__ == '__main__':
    main()