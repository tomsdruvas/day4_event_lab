class Customer:
    def __init__(self, name, wallet, favourite_performer):
        self.name = name
        self.wallet = wallet
        self.favourite_performer = favourite_performer
    
    def check_wallet(self):
        return self.wallet
    
    def reduce_wallet(self, amount):
        self.wallet -= amount
        


    