# Create class of Order, Order Detail, Items, State - Chaitanya
# Create class of Customer, Address, Contract Details - Anudeep
# Create class of Payment, Cash, Bank Transfers, Credit Card - Kamendu



class Payment:                                              # a class for payment as the 'parent class' 
    def __init__(self, amount):
        self.amount = amount        


class Cash(Payment):                                       # a child class for payment type as 'cash'               
    def __init__(self, amount, cash_tendered):
        super().__init__(amount)
        self.cash_tendered = cash_tendered                 

    def tender_cash(self):          #the amount that is received from the user
        return self.cash_tendered

    def return_change(self):        #received cash - amount of item = return change
        return self.cash_tendered - self.amount


class BankTransfere(Payment):                             # a child class for payment type as 'bank transfer'
	def init(self, amount, recipient_name, IBAN, BIC):     
		super().init(amount)
		self.recipient_name = recipient_name
		self.IBAN = IBAN
		self.BIC = BIC


	def authorized(self):           #only authorization to keep the bank details as hidden
   		return True

class CreditCard(Payment):                               # a chilld class for payment type as 'Credit card'
	def init(self, amount, number, type, cardholder_name, expiration_date):
        super().init(amount)
        self.number = number
        self.type = type
        self.cardholder_name = cardholder_name
        self.expiration_date = expiration_date


	def authorized(self):           #only authorization to keep the credit card details as hidden
    		return True

# Test the code - Jay
