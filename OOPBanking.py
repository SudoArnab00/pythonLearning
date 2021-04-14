class mybank:
    def __init__(self, owner, cbal=0):
        self.owner = owner
        self.cbal = cbal
    
    def __str__(self):
        return f"{self.owner} has Rs.{self.cbal}"

    def credit_bal(self, give):
        self.cbal += give
        print(f"Added Rs.{give} to your account.")

    def debit_bal(self, take):
        if self.cbal >= take:
            self.cbal -= take
            print('Withdrawal Accepted')
            print('You have Rs.{} in your account'.format(self.cbal))
        else:
            print('Sorry, insufficient balance.')
    
myobj = mybank("Arnab",500)
print(myobj)                # Display accoutn details
myobj.credit_bal(700)       # Deposit money
myobj.debit_bal(500)        # Withdraw money
myobj.debit_bal(1600)       # Withdraw too much money