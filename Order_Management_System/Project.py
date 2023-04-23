# Create class of Order, Order Detail, Items, State - Chaitanya

# Creating a class named "State" to represent different states of an order
class State:
    PENDING = "Order is Pending"
    ACCEPTED = "Order is Accepted"
    REJECTED = "Order is Rejected"
    PROCESSING = "Order is Processing"
    SHIPPING = "Order is Shipping"
    CLOSED = "Order is Closed"

# Creating a class named "Order" to represent an order placed by a customer 
class Order:
    def __init__(self, date, customer, order_details, state):
        self.date = date
        self.customer = customer
        self.order_details = order_details
        self.state = state
    
    # Method to cancel an order by changing its state to "Order is Closed"
    def cancel(self):
        self.state = State.CLOSED
    
    # Method to set an order to state to "Order is Processing"
    def process(self):
        self.state = State.PROCESSING
    
    # Method to set an order to state to "Order is Shipping"
    def dispatch(self):
        self.state = State.SHIPPING
    
    # Creating a method to calculate the total cost of the order
    def calculate_total(self):
        # Using a list comprehension to calculate subtotal of each order detail, then sum the subtotals
        return sum([order_detail.calculate_weight() for order_detail in self.order_details])
    
    # Creating a method to calculate the total weight of the order
    def calculate_total_weight(self):
        # Using a list comprehension to calculate the weight of each order detail, then sum the weights
        return sum([order_detail.calculate_weight() for order_detail in self.order_details])
    

# Creating a class named "Order detail" to represent the details of an order
class OrderDetail:
    def __init__(self, quantity, item):
        self.quantity = quantity
        self.item = item
    
    # Method to calulate subtotal of the order
    def calculate_subtotal(self):
        return self.quantity * self.item.get_price_for_quantity()
    
    # Method to calculate the weight per item
    def calculate_weight(self):
        return self.quantity * self.item.weight

# Creating a class named "Item" to represent  an item that can be ordered
class Item:
    def __init__(self, price, weight, description):
        self.price = price
        self.weight = weight
        self.description = description
    
    # Method to get price of the item for certain quantity
    def get_price_for_quantity(self):
        return self.price
    
    # Method to check an item is in stock 
    def in_stock(self):
        return True
# Create class of Customer, Address, Contract Details - Anudeep

#A Customer class which has the attributes of contact details, Address and Orders of a Customer
class Customer:
    def __init__(self, contact_details, address, orders):
        self.contact_details = contact_details
        self.address = address
        self.orders = orders

    def get_contact_details(self):
        return self.contact_details   # Function to return the contact details to customer class

    def get_address(self):   
        return self.address           # Function to return the address details to customer class

    def get_orders(self):
        return self.orders            #  Function to return the order details to customer class

 #A Address  class which has the attributes of country, city, postalcode, street and number details   

class Address:
    def __init__(self, country, city, postalcode, street, number):
        self.country = country
        self.city = city
        self.postalcode = postalcode
        self.street = street
        self.number = number

    def get_country(self):    
        return self.country          # Function to return the Country details to Address class

    def get_city(self):
        return self.city               # Function to return the City details to Address class

    def get_postalcode(self):
        return self.postalcode        # Function to return the postalcode details to Address class

    def get_street(self):
        return self.street            # Function to return the street details to Address class

    def get_number(self):
        return self.number           # Function to return the Country details to Address class

    def get_full_address(self):
        return f"{self.number} {self.street}, {self.postalcode} {self.city}, {self.country}"
    
 #A ContactDetails  class which has the attributes of firstname, lastname, email and phone number of a customer   

class ContactDetails:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def get_first_name(self):
        return self.first_name          # Function to return the first_name details to ContactDetails class

    def get_last_name(self): 
        return self.last_name           # Function to return the last_name details to ContactDetails class

    def get_email(self):
        return self.email               #  Function to return the email details to ContactDetails class

    def get_phone_number(self):
        return self.phone_number        #  Function to return the phone_number details to ContactDetails class

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

