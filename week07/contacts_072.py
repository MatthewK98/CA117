import sys
class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return "{} {} {}".format(self.name,self.phone,self.email)




class ContactList:
    def __init__(self,d = {}):
        self.d = d
        
    def add_contact(self,contact):
        self.d[contact.name] = contact
    
    def del_contact(self,name):
        if name in self.d:
            del self.d[name]
            
    def get_contact(self, name):
        if name in self.d:
            return self.d[name]
        else:
            None
    def __str__(self):
        tup = sorted(self.d.items())
        output = "Contact list" + "\n" + '------------' + "\n"
        for k in tup:
            output += str(k[1]) + "\n"
        return output.strip()
        # for k in tup:
        #     return str(k[1])








def main():
    cl = ContactList() #{}
    for line in sys.stdin:
        [name, phone, email] = line.strip().split()
        c = Contact(name, phone, email)
        cl.add_contact(c)
        print(c)

    c = cl.get_contact('Jimmy')
    print(c)
    c = cl.get_contact('Mary')
    print(c)

    print(cl)
    cl.del_contact('Maggie')
    cl.del_contact('Maggie')

    c = Contact('Sue', '087-6442378', 'sue@eircom.net')
    cl.add_contact(c)
    c = Contact('Fred', '085-8776543', 'fred@yahoo.com')
    cl.add_contact(c)
    print(cl)

if __name__ == '__main__':
    main()