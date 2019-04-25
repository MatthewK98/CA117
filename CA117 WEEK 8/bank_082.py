class BankAccount:
    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, forename, surname, balance=0.00, account_number=0):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1
        BankAccount.total_lodgements += 1

    def __str__(self):
        return """Name: {} {}
Account number: {}
Balance: {:.2f}""".format(self.forename, self.surname, self.account_number, self.balance)

    def lodge(self, money):
        self.balance += money
        BankAccount.total_lodgements += 1

    def __iadd__(self, num):  # Overwrite
        self.balance += num
        return self

    #add is to create new thing

    def apply_interest(self):
        add_on = self.balance * BankAccount.interest_rate
        self.balance += add_on

def main():

    # Check class attributes
    print('Checking class attributes...')
    print(BankAccount.next_account_number)
    print(BankAccount.total_lodgements)
    print(BankAccount.interest_rate)

    # Create two accounts
    b1 = BankAccount('Persephone', 'Murphy')
    b2 = BankAccount('Jemima', 'O\'Reilly', 30)

    # Check string representation
    print('Printing bank accounts...')
    print(b1)
    print(b2)

    # Check lodge
    print('Checking lodgements...')
    b1.lodge(100)
    b2.lodge(100)
    print(b1)
    print(b2)

    # Check increment
    print('Checking increment...')
    b3 = b1
    b1 += 22
    b2 += 23
    print(b1)
    print(b3 is b1)
    print(b2)

    # Check interest
    b1.apply_interest()
    b2.apply_interest()
    print(b1)
    print(b2)

    # Check class attributes
    print('Checking class attributes...')
    print(BankAccount.next_account_number)
    print(BankAccount.total_lodgements)
    print(BankAccount.interest_rate)

if __name__ == '__main__':
    main()
