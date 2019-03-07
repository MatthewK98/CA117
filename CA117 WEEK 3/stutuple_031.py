class Student:
    def __init__(self, firstname, surname, id):
        self.First = firstname
        self.Last = surname
        self.ID = id

def show_student(s):
    print("First name:", s.First)
    print("   Surname:", s.Last)
    print("        ID:", s.ID)
