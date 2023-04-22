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
        return None
    
    # Creating a method to calculate the total weight of the order
    def calculate_total_weight(self):
        return None
    

# Creating a class named "Order detail" to represent the details of an order
class OrderDetail:
    def __init__(self, quantity, item):
        self.quantity = quantity
        self.item = item
    
    # Method to calulate subtotal of the order
    def calculate_subtotal(self):
        return None
    
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
# Create class of Payment, Cash, Bank Transfers, Credit Card - Kamendu
# Test the code - Jay
