class Customer(object):
    name = ""
    balance = "" 

    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def createAccount(self, amount):
         registration = "%s opened an account with the amount of %f" % (self.name, float(amount))
         self.balance = float(amount)
         return registration

    def deposit(self, amount):
        self.balance += amount
        receipt = "%s deposited an amount of %f" % (self.name, self.balance)
        return receipt 

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError("The amount you wish to withdraw exceeds your balance")
        elif amount == self.balance:
            raise RuntimeError("You cant withdraw the exact amount")
        self.balance -= amount
        receipt = "%s withdrew an amount of %f" % (self.name, self.balance)
        return receipt

    



declare = Customer("Hillary", 0.0)
#create Account
print declare.createAccount(30.00)

#deposit Money in Account
print declare.deposit(40.56)

#withdraw money from Account
print declare.withdraw(50.78)