class User:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def makeDeposit(self, amount):
        self.balance += amount
        print(f"Depositing {amount} into account {self.name}")
        print(f"Your balance is now {self.balance}")
    
    def makeWithdrawal(self, amount):
        self.balance -= amount
        print(f"Withdrawing {amount} from account {self.name}")
        print(f"Your balance is now {self.balance}")

    def displayBalance(self,balance):
        print(balance)


Jake = User("Jake", 300);
Jack = User("Jack", 200);
John = User("John", 100);

Jake.makeDeposit(100)
Jake.makeDeposit(200)
Jake.makeDeposit(400)
Jake.makeWithdrawal(200)
print(f"Jake's balance is now: " + str(Jake.balance))

print("------------------------------------------------------")

Jack.makeDeposit(1000)
Jack.makeDeposit(2000)
Jack.makeWithdrawal(500)
Jack.makeWithdrawal(500)
print(f"Jack's balance is now: " + str(Jack.balance))

print("------------------------------------------------------")

John.makeDeposit(5000)
John.makeWithdrawal(1000)
John.makeWithdrawal(1000)
John.makeWithdrawal(1000)