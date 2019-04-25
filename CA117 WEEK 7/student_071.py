class Student:
    def __init__(self, surname, forename, sid, modlist=[]):
        self.sid = sid
        self.surname = surname
        self.forename = forename
        self.modlist = modlist

    def add_module(self, module):
        self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)

    def print_details(self):
        print("ID:", self.sid)
        print("Surname:", self.surname)
        print("Forename:", self.forename)
        modules = self.modlist
        output = ""
        for i in modules:
            output += i + " "
        print("Modules:", output.strip())

def main():

    student1 = Student('Murphy', 'Jimmy', 15234654)
    student1.add_module('CA117')
    student1.add_module('CA116')
    student1.add_module('CA114')
    student1.print_details()

    student2 = Student('Lannister', 'Cersei', 15876123, ['CA115', 'CA216'])
    student2.del_module('CA216')
    student2.del_module('CA117')
    student2.del_module('CA216')
    student2.add_module('CA117')
    student2.print_details()

if __name__ == '__main__':
    main()
