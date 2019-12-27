class Customer:
    discount = 0.00

    def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
        self.name = name
        self.balance = balance
        self.addr_line1 = addr_line1
        self.addr_line2 = addr_line2
        self.addr_line3 = addr_line3

    def owes(self,):
        sub = self.balance * (self.discount / 100)
        return self.balance - sub

    def __str__(self):
        return """{}
{}
{}
{}
Balance: {:.2f}
Discount: {:.0f}%
Amount due: {:.2f}""".format(self.name, self.addr_line1, self.addr_line2, self.addr_line3, self.balance, self.discount, self.owes())

class ValuedCustomer(Customer):
    discount = 10.00

def main():

    c1 = Customer('Jimmy', 100, '22 Main Street', 'Naas', 'Kildare')
    c2 = ValuedCustomer('Lucy', 100, '23 Main Street', 'Roosky', 'Roscommon')
    c3 = Customer('Fred', 200, '24 Main Street', 'Sneem', 'Kerry')

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
    main()