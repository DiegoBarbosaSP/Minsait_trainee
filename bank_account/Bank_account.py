class bank_account:
    def __init__(self , nome , saldo):
        self.nome = nome
        self.saldo = saldo

    def withdrawal(self, amount):
        if amount < self.saldo:
            print("Insufficient founds")
        else:
            self.saldo -= amount
    def deposit(self, amount):
        self.saldo += amount               
        
    def check_balance(self):
         print("Current balance:",(self.saldo))


new_account = bank_account("Diego", 1200.0)
new_account.deposit(300.0)
new_account.check_balance()
