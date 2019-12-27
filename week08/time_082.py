class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def time_to_seconds(self):
        h = self.hour * 3600
        m = self.minute * 60
        s = self.second
        total = h + m + s
        return total
        
    def __eq__(self, other):
        return self.time_to_seconds() == other.time_to_seconds()
        
    def __gt__(self, other):
        return self.time_to_seconds() > other.time_to_seconds()
        
    @classmethod    
    def seconds_to_time(cls, sec):
        h = sec // 3600
        m = sec % 3600 // 60
        s = sec % 3600 % 60
        if h >= 24:
            h = h % 24
        return Time(h,m,s)
        
    def __add__(self, other):
        total = self.time_to_seconds() + other.time_to_seconds()
        return self.seconds_to_time(total)
    
    def __iadd__(self, other):
        newtime = self + other
        self.hour=newtime.hour
        self.second=newtime.second
        self.minute=newtime.minute
        return self
    
    def __str__(self):
        return "The time is {:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)
        
        
        
        
def main():

    t1 = Time()
    t2 = Time(9,35,16)
    t3 = Time(0,0,4)
    t4 = Time(9,35,16)

    # Check string representation
    print('Printing times...')
    print(t1)
    print(t2)
    print(t3)

    # Check equality
    print('Checking equality...')
    print(t2 == t4)
    print(t1 == t3)

    # Check greater than/less than
    print('Checking greater than/less than...')
    print(t2 > t3)
    print(t2 < t3)
    print(t4 > t1)
    print(t4 < t1)

    # Check addition
    print('Checking addition...')
    t5 = t2 + t2 + t2
    print(t5)
    print(t5 > t2)

    # Check increment
    print('Checking increment...')
    t33 = t2
    t2 += t2
    t2 += t4
    print(t2)
    print(t33 is t2)
    print(t2 > t3)
    
    # Check class method
    print('Checking class method...')
    t6 = Time.seconds_to_time(123456)
    print(t6)
    print(t6 > t1)

if __name__ == '__main__':
    main()
# print(34536 // 3600)
# print(34536 % 3600 // 60)
# print(34536 % 3600 % 60)
